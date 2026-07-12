# ?? Production-Ready AWS DevOps Deployment

A production-style DevOps project demonstrating the deployment, automation, monitoring, and performance testing of a Flask web application on AWS.

## ?? Project Overview

This project showcases an end-to-end DevOps workflow using AWS Free Tier services. A Flask web application is deployed on an Amazon EC2 instance using Gunicorn and Nginx, automated through GitHub Actions CI/CD, monitored with Amazon CloudWatch, backed up to Amazon S3, and performance tested using k6.

---

## ??? Architecture

```
Developer
    ³
    GitHub Repository
    ³
    GitHub Actions (CI/CD)
    ³
    Amazon EC2 (Ubuntu)
    ³
 ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿
 ³     Nginx     ³
 ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ
        ³
           Gunicorn Server
        ³
         Flask Web Application
        ³
 ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿
 ³ CloudWatch    ³
 ³ Logs & Metrics³
 ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ
        ³
         Amazon S3 (Backups)
```

---

## ?? Technologies Used

- AWS EC2
- Amazon S3
- AWS IAM
- Amazon CloudWatch
- Ubuntu Linux
- Nginx
- Gunicorn
- Python 3
- Flask
- Git
- GitHub
- GitHub Actions
- k6 Load Testing

---

## ? Features

- Flask web application deployment on AWS EC2
- Reverse proxy configuration using Nginx
- Gunicorn application server
- Automated CI/CD pipeline with GitHub Actions
- CloudWatch monitoring and centralized logging
- IAM role with least privilege permissions
- Amazon S3 backup with versioning
- Performance testing using k6
- Health check endpoint for monitoring

---

## ?? Project Structure

```
devops-aws/
³
ÃÄÄ .github/
³   ÀÄÄ workflows/
³       ÀÄÄ deploy.yml
³
ÃÄÄ app/
³   ÃÄÄ app.py
³   ÃÄÄ requirements.txt
³   ÃÄÄ templates/
³   ³   ÀÄÄ index.html
³   ÀÄÄ venv/
³
ÃÄÄ loadtest.js
ÃÄÄ README.md
ÀÄÄ .gitignore
```

---

## ?? Application Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Home Page |
| `/health` | Health Check |
| `/about` | About Page |
| `/users` | Sample User Data |

---

## ?? CI/CD Workflow

The deployment pipeline is triggered automatically whenever code is pushed to the **main** branch.

Workflow Steps:

1. Checkout repository
2. Configure SSH
3. Connect to EC2
4. Pull latest code
5. Install dependencies
6. Restart Flask service
7. Deploy updated application

---

## ?? Monitoring

Amazon CloudWatch is configured to monitor:

- CPU Utilization
- Network In
- Network Out
- Disk Read Bytes
- Disk Write Bytes

Additional features:

- CloudWatch Dashboard
- CloudWatch Logs
- CPU Utilization Alarm

---

## ?? S3 Backup

Amazon S3 is used for application backup.

Bucket:

```
aryen-devops-backup-2026
```

Features:

- Versioning Enabled
- Secure IAM Access
- Backup using AWS CLI

---

## ?? Security

- IAM Role attached to EC2
- Least Privilege Access
- Security Groups
- SSH Key Authentication
- Nginx Reverse Proxy
- CloudWatch Agent

---

## ?? Load Testing Results

Tool Used:

```
k6
```

Configuration:

- Virtual Users: **20**
- Duration: **30 seconds**

Results:

| Metric | Result |
|---------|--------|
| Total Requests | 600 |
| Success Rate | 100% |
| Failed Requests | 0 |
| Average Response Time | 24.42 ms |
| P95 Response Time | 27.73 ms |
| Throughput | 19.48 req/sec |
| Peak CPU Utilization | 17.9% |

---

## ?? Screenshots

Screenshots of the following components are included in the project report:

- EC2 Deployment
- Flask Application
- Nginx Service
- GitHub Actions Pipeline
- CloudWatch Dashboard
- CloudWatch Logs
- IAM Role
- Amazon S3 Backup
- k6 Load Testing

---

## ?? Future Improvements

- HTTPS using SSL/TLS
- Application Load Balancer
- Auto Scaling Group
- Docker Containerization
- Amazon ECS/EKS Deployment
- Terraform Infrastructure as Code
- AWS CodePipeline Integration
- AWS Secrets Manager
- Custom Domain with Route 53

---

## ????? Author

**Aryen Garg**

B.Tech Computer Science Engineering

GitHub:
https://github.com/AryenSGarg

Project Repository:
https://github.com/AryenSGarg/devops-aws

---

## ?? License

This project was developed for educational and learning purposes as part of a DevOps technical assignment.
