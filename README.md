# 🐍 My Flask App

A simple Python Flask web application containerised with Docker and hosted on GitHub.

---

## 📋 Table of Contents

- [About](#about)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Run Locally (without Docker)](#run-locally-without-docker)
  - [Run with Docker](#run-with-docker)
- [API Endpoints](#api-endpoints)
- [Docker Commands](#docker-commands)
- [GitHub](#github)

---

## About

This is a beginner-friendly Flask web application that demonstrates:
- A basic Python web server using Flask
- Containerisation using Docker
- Version control and hosting on GitHub

---

## Prerequisites

Make sure you have the following installed:

| Tool | Download |
|------|----------|
| Python 3.x | https://python.org/downloads |
| Git | https://git-scm.com/download/win |
| Docker Desktop | https://www.docker.com/products/docker-desktop |

---

## Project Structure

```
my-flask-app/
├── app.py               # Main Flask application
├── Dockerfile           # Docker configuration
├── .dockerignore        # Files to exclude from Docker image
├── .gitignore           # Files to exclude from Git
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## Getting Started

### Run Locally (without Docker)

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/my-flask-app.git
   cd my-flask-app
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # Windows (Command Prompt)
   venv\Scripts\activate.bat
   # Windows (PowerShell)
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   python app.py
   ```

5. Open your browser at **http://localhost:5000**

---

### Run with Docker

1. **Build the Docker image**
   ```bash
   docker build -t my-flask-app .
   ```

2. **Run the container**
   ```bash
   docker run -p 5000:5000 my-flask-app
   ```

3. Open your browser at **http://localhost:5000**

> 💡 To run in the background (detached mode):
> ```bash
> docker run -d -p 5000:5000 my-flask-app
> ```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home page |
| GET | `/health` | Health check — returns `{"status": "ok"}` |

---

## Docker Commands

| Command | Description |
|---------|-------------|
| `docker build -t my-flask-app .` | Build the Docker image |
| `docker run -p 5000:5000 my-flask-app` | Run the container |
| `docker run -d -p 5000:5000 my-flask-app` | Run in background |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers |
| `docker stop <container_id>` | Stop a container |
| `docker rm <container_id>` | Remove a container |

---

## GitHub

To push updates to GitHub:

```bash
git add .
git commit -m "Your commit message"
git push origin main
```

---

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| Flask | 3.1.3 | Web framework |
| Jinja2 | 3.1.6 | HTML templating |
| Werkzeug | 3.1.8 | Flask core utilities |
| click | 8.3.3 | CLI support |
| itsdangerous | 2.2.0 | Session security |
| MarkupSafe | 3.0.3 | Safe HTML rendering |

---

## 👩‍💻 Author

**Bhaamini**  
GitHub: [@Bhaamini](https://github.com/Bhaamini)