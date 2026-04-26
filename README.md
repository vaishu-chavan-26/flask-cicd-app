# 🚀 CI/CD Pipeline Project (AWS DevOps)

## 📌 Overview
This project demonstrates a fully automated CI/CD pipeline using AWS services. The pipeline automatically builds and deploys a web application whenever code is pushed to GitHub.

It follows a real-world DevOps workflow used in production systems.

---

## 🎯 Objective
To build an automated CI/CD pipeline that:
- Integrates GitHub with AWS
- Automates build and deployment
- Deploys application to EC2 without manual intervention

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
![Architecture](architecture/architecture.png)

---

## 🔁 CI/CD Workflow

1. Developer pushes code to GitHub repository
2. CodePipeline detects the change automatically
3. CodeBuild installs dependencies and builds the application
4. CodeDeploy deploys the application to EC2 instance
5. Application is live and accessible via public IP

---

## ⚙️ Tech Stack
- Node.js / Flask (Application)
- AWS CI/CD Services
- Linux (EC2 Server)
- GitHub (Version Control)

---

## 📸 Screenshots

### 🔹 CodePipeline Execution
![Pipeline](screenshots/pipeline-success.png)

### 🔹 CodeBuild Process
![Build](screenshots/build-success.png)

### 🔹 Deployment Status
![Deploy](screenshots/deployment-success.png)

### 🔹 Final Application Output
![App](screenshots/app-output.png)

---

## 📁 Project Structure
