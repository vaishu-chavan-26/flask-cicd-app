# 🚀 CI/CD Pipeline for Flask Application (AWS DevOps Project)

![AWS](https://img.shields.io/badge/AWS-Cloud-orange?logo=amazon-aws)
![CI/CD](https://img.shields.io/badge/CI%2FCD-Automated-blue?logo=githubactions)
![Flask](https://img.shields.io/badge/Flask-Python-black?logo=flask)
![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![DevOps](https://img.shields.io/badge/DevOps-AWS%20Pipeline-red?logo=amazon-aws)

---

## 📌 Project Overview
This project demonstrates a fully automated CI/CD pipeline using AWS services. The pipeline automatically builds and deploys a Flask web application whenever code is pushed to GitHub.

It follows a real-world DevOps workflow used in production environments.

---

## 🎯 Objective
To implement an end-to-end CI/CD pipeline that:
- Automates application deployment
- Integrates GitHub with AWS services
- Enables continuous integration and delivery
- Eliminates manual deployment steps

---

## 🧰 AWS Services Used
- AWS CodePipeline
- AWS CodeBuild
- AWS CodeDeploy
- Amazon EC2
- IAM Roles
- GitHub (Source Control)

---

## 🏗️ Architecture Diagram
![Architecture](Screenshots/06-architecture/architecture.png)

---

## 🔁 CI/CD Workflow

1. Developer pushes code to GitHub repository  
2. AWS CodePipeline detects changes automatically  
3. CodeBuild installs dependencies and builds the application  
4. CodeDeploy deploys the application to EC2 instance  
5. Application is automatically updated and live  

---

## ⚙️ Tech Stack
- Flask (Python Web Framework)
- AWS CI/CD Services
- Linux EC2 Server
- GitHub Version Control

---

## 📸 Screenshots

### 🔹 GitHub Repository
![GitHub](Screenshots/01-github/repo-home.png)

### 🔹 CodePipeline Execution
![Pipeline](Screenshots/02-codepipeline/pipeline-success.png)

### 🔹 CodeBuild Process
![Build](Screenshots/03-codebuild/build-success.png)

### 🔹 CodeDeploy Status
![Deploy](Screenshots/04-codedeploy/deploy-success.png)

### 🔹 Final Application Output
![App](Screenshots/05-final-output/app-live.png)

---


---

## 🚀 Key Features
- Fully automated CI/CD pipeline
- Continuous integration and deployment
- No manual deployment required after setup
- Real-time updates from GitHub commits
- Production-level DevOps architecture

---

## 📈 What I Learned
- AWS CI/CD pipeline architecture
- CodeBuild automation process
- CodeDeploy deployment workflow
- GitHub integration with AWS services
- Real-world DevOps pipeline implementation

---

## 🔥 Real-World Use Case
This project simulates how modern companies deploy applications:
- Every code push triggers automatic deployment
- Reduces human error
- Improves deployment speed and reliability
- Enables continuous delivery

---

## 👩‍💻 Author
Vaishnavi Chavan

