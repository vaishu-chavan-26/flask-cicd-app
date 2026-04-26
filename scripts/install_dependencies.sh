#!/bin/bash

cd /home/ec2-user/flask-cicd-app
pip3 install --user -r requirements.txt
pip3 install --user gunicorn
