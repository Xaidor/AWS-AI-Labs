# 🧠 AWS AI Playground: Building with Bedrock

Welcome! This repo is my hands-on exploration of AWS Bedrock and GenAI services — combining my cloud engineering background with my passion for machine learning and real-world problem solving.

## 📚 Projects

### 1. `PromptPlay`
*Simple Flask app to interact with foundational models on AWS Bedrock.*

- Tools: Flask, Python, boto3, Bedrock
- Concepts: Prompt engineering, API integration, IAM roles
- [Code →](./PromptPlay)

---

### 2. `SmartAssist`
*Document-based AI assistant using S3 + DynamoDB to store and summarize uploaded content.*

- Tools: AWS Lambda, S3, DynamoDB, Bedrock
- Concepts: Document ingestion, vector storage, summarization
- [Code →](./SmartAssist)

---

### 3. `InsightFlow`
*End-to-end event-driven architecture for content analysis + user alerting.*

- Tools: EventBridge, Step Functions, Bedrock, SNS
- Concepts: Event-driven design, orchestration, notifications
- [Code →](./InsightFlow)

---

## 🛠️ Tech Stack

- AWS Bedrock (Titan)
- Python, Flask
- S3, Lambda, DynamoDB, EventBridge, SNS
- IAM, boto3, API Gateway
- HTML/CSS 

---


[📬 Connect with me on LinkedIn](https://www.linkedin.com/in/kaylenanderson)

---

## 🧭 Roadmap

- [x] Project 1: Build & test Bedrock prompt app
- [ ] Project 2: Add document summarization pipeline
- [ ] Project 3: Build full event-driven architecture

---

## ⚡ Setup Instructions

```bash
git clone https://github.com/yourusername/aws-ai-lab.git
cd promptplay
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
