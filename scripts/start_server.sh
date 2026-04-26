#!/bin/bash

pkill gunicorn

cd /home/ec2-user/flask-cicd-app
/home/ec2-user/.local/bin/gunicorn -b 0.0.0.0:5000 app:app
