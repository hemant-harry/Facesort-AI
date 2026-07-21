# 🚀 FaceSort AI - Dockerized FastAPI Application on AWS EC2

A production-style DevOps project demonstrating how to containerize and deploy a FastAPI-based AI application using Docker and Docker Compose on AWS EC2.

This project focuses on real-world deployment practices, Linux troubleshooting, Docker containerization, cloud deployment, and production debugging.

---

# 📌 Project Overview

FaceSort AI is an AI-powered face recognition application built with FastAPI. The application has been containerized using Docker and deployed on an AWS EC2 instance using Docker Compose.

The deployment includes production-level troubleshooting such as:

- Docker containerization
- Docker Compose deployment
- AWS EC2 deployment
- Linux swap memory configuration
- Out Of Memory (OOM) troubleshooting
- Docker networking
- Production debugging

---

# ✨ Features

- AI Face Recognition
- FastAPI Backend
- Dockerized Application
- Docker Compose Support
- AWS EC2 Deployment
- Production-ready Dockerfile
- Linux Swap Memory Configuration
- Port Mapping
- Easy Deployment

---

# 🛠 Tech Stack

- Python 3.12
- FastAPI
- Uvicorn
- Docker
- Docker Compose
- AWS EC2
- Amazon Linux 2023
- InsightFace
- ONNX Runtime
- OpenCV
- Git
- GitHub

---


# 🎯 What Does FaceSort AI Do?

FaceSort AI is an AI-powered face recognition web application that automatically sorts images based on a reference person's face.

### Workflow

1. Upload a **Reference Image** containing the face you want to identify.
2. Upload a folder containing multiple photos.
3. The AI analyzes every image using **InsightFace** and compares each detected face with the reference image.
4. Matching photos are automatically grouped into a separate folder.
5. Download the sorted images with a single click.

This eliminates the need to manually search through hundreds or thousands of photos, making it useful for photographers, event organizers, media teams, and personal photo management.

---

## 🚀 How It Works

```text
Reference Image
        │
        ▼
AI Extracts Face Embedding
        │
        ▼
Upload Folder (100+ Images)
        │
        ▼
AI Compares Every Face
        │
        ▼
Matching Images
        │
        ▼
Download Sorted Photos
```


# 🏗️ Architecture Diagram

```text
                     👤 User
                        │
                        ▼
                🌍 Web Browser
          http://AWS_PUBLIC_IP:8000
                        │
                        ▼
              ☁️ AWS EC2 Instance
                Amazon Linux 2023
                        │
                Docker Compose
                        │
        ┌─────────────────────────┐
        │     FaceSort AI         │
        │-------------------------│
        │ FastAPI                 │
        │ Uvicorn                 │
        │ InsightFace             │
        │ ONNX Runtime            │
        │ OpenCV                  │
        └─────────────────────────┘
                        │
                        ▼
             AI Face Recognition
```

---

# 📁 Project Structure

```text
FaceSort-AI/
│
├── app/
├── static/
├── templates/
├── screenshots/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .dockerignore
```

---

# 🐳 Docker Commands

### Build Image

```bash
docker build -t facesort-ai .
```

### Run Container

```bash
docker run -d -p 8000:8000 facesort-ai
```

### View Running Containers

```bash
docker ps
```

### View Images

```bash
docker images
```

---

# 🐳 Docker Compose

Run the complete application

```bash
docker compose up -d --build
```

Stop containers

```bash
docker compose down
```

View running services

```bash
docker compose ps
```

---

# ☁️ AWS Deployment

The application was deployed on an AWS EC2 Amazon Linux 2023 instance.

Deployment Steps:

- Launch EC2 Instance
- Install Docker
- Install Docker Compose
- Clone GitHub Repository
- Build Docker Image
- Run Docker Compose
- Expose Port 8000
- Access Application via Public IP
  

---

# ⚡ Production Challenges Solved

During deployment several real-world production issues were encountered and resolved.

### Docker Container Restart Issue

The container repeatedly restarted because the application exhausted available memory.

Solution:

- Configured Linux Swap Memory
- Optimized Docker deployment

---

### Out Of Memory (OOM)

The EC2 instance had only 1 GB RAM which caused the Linux OOM Killer to terminate the application.

Solution:

- Created a 2 GB Swap File
- Enabled Swap Memory
- Verified memory usage using Linux tools

---

### Disk Space Issue

Docker images consumed most of the available storage.

Solution:

- Removed unused Docker images
- Cleared build cache
- Deleted unused Docker volumes

---

### Docker Networking

Configured proper port mapping between host and container.

```
Host Port 8000
      │
      ▼
Container Port 8000
```

---

# 📚 What I Learned

- Docker Image Creation
- Dockerfile Best Practices
- Docker Compose
- Linux Memory Management
- Swap Memory Configuration
- AWS EC2 Deployment
- Docker Networking
- Docker Debugging
- Production Troubleshooting
- Git & GitHub Workflow

---

# 🚀 Future Improvements

- Nginx Reverse Proxy
- HTTPS using Let's Encrypt
- CI/CD using GitHub Actions
- Kubernetes Deployment
- Monitoring with Prometheus & Grafana
- Load Balancing

---

# 👨‍💻 Author

**Hemant Saini**

DevOps & Cloud Enthusiast

GitHub: https://github.com/hemant-harry

---

⭐ If you found this project useful, don't forget to give it a star.
