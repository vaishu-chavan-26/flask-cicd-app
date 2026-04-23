import boto3
from datetime import datetime, timedelta

ec2 = boto3.client('ec2')
cloudwatch = boto3.client('cloudwatch')

def lambda_handler(event, context):
    instances = ec2.describe_instances()

    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            state = instance['State']['Name']

            # ✅ Skip already stopped instances
            if state != 'running':
                continue

            end = datetime.utcnow()
            start = end - timedelta(days=1)

            metrics = cloudwatch.get_metric_statistics(
                Namespace='AWS/EC2',
                MetricName='CPUUtilization',
                Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
                StartTime=start,
                EndTime=end,
                Period=86400,
                Statistics=['Average']
            )

            # ✅ Check if data exists
            if not metrics['Datapoints']:
                print(f"No CPU data for {instance_id}")
                continue

            avg_cpu = metrics['Datapoints'][0]['Average']
            print(f"Instance {instance_id} CPU: {avg_cpu}%")

            # ✅ Stop only if idle
            if avg_cpu < 10:
                print(f"Stopping instance: {instance_id}")
                ec2.stop_instances(InstanceIds=[instance_id])