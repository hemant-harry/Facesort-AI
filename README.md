# 🚀 FaceSort AI

A production-style AI web application built with **FastAPI** and **Docker**, deployed on **AWS EC2** using **Docker Compose**.

This project was created to learn real-world DevOps practices including containerization, cloud deployment, debugging, and production troubleshooting.

---

## 📌 Features

- AI-based Face Recognition Application
- FastAPI Backend
- Dockerized Application
- Docker Compose Support
- AWS EC2 Deployment
- Production-ready Container Setup

---

## 🛠️ Tech Stack

- Python 3.12
- FastAPI
- Docker
- Docker Compose
- AWS EC2
- Uvicorn
- Git & GitHub

---

## 📂 Project Structure

```
Facesort-AI/
│
├── app/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md
```

---

## 🚀 Run Locally

Clone the repository

```bash
git clone <repository-url>
```

Move into project

```bash
cd Facesort-AI
```

Build Docker Image

```bash
docker build -t facesort-ai .
```

Run Container

```bash
docker run -d -p 8000:8000 facesort-ai
```

---

## 🐳 Run using Docker Compose

```bash
docker compose up -d --build
```

Stop Application

```bash
docker compose down
```

---

## ☁️ AWS Deployment

This application has been successfully deployed on AWS EC2 using Docker Compose.

Deployment steps included:

- Launch EC2 Instance
- Install Docker & Docker Compose
- Clone Repository
- Build Docker Image
- Run Containers
- Expose Application on Port 8000

---

## 🔧 Production Issues Solved

During deployment, several real-world production issues were diagnosed and resolved:

- Fixed missing OpenCV runtime libraries
- Resolved Docker container restart loop
- Diagnosed Exit Code 137
- Identified Linux OOM Killer
- Created Swap Memory on EC2
- Fixed Disk Space Issues
- Cleaned Docker Build Cache & Volumes

---

## 📸 Screenshots

### Application

(Add Screenshot Here)

### Docker Containers

(Add Screenshot Here)

### AWS EC2

(Add Screenshot Here)

---

## 📚 What I Learned

- Docker
- Docker Compose
- AWS EC2 Deployment
- Linux Troubleshooting
- Docker Networking
- Production Debugging
- Memory Management
- Container Optimization

---

## 👨‍💻 Author

Hemant Saini

DevOps & Cloud Enthusiast
