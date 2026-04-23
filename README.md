# Automated AWS Cost Optimizer

## 🎯 Purpose
This project automatically reduces AWS costs by stopping idle EC2 instances based on CPU utilization.

## 🧰 AWS Services Used
- AWS Lambda
- Amazon EC2
- Amazon CloudWatch
- Amazon EventBridge

## ⚙️ How It Works
1. Lambda function fetches EC2 instances
2. Retrieves CPU utilization from CloudWatch
3. If CPU usage is less than 10%, instance is stopped
4. EventBridge triggers Lambda daily

## 📌 Features
- Automatic cost optimization
- Serverless architecture
- Logging using CloudWatch
- Scalable and efficient

## 🚀 Setup Steps
1. Create EC2 instance
2. Create IAM role with EC2 & CloudWatch access
3. Create Lambda function
4. Deploy Python code
5. Schedule using EventBridge

## 📊 Output
- Idle EC2 instances are automatically stopped
- Logs available in CloudWatch

## 📷 Screenshots (Add your own)
- EC2 instance stopped
- Lambda execution logs
- EventBridge rule

## 👩‍💻 Author
Vaishnavi Chavan