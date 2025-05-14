# 🧮 Calculator App

A simple and beautiful web-based calculator that performs basic arithmetic operations. This application is containerized using Docker and orchestrated using Docker Compose as part of a practical DevOps assignment.

---

## 🎯 Project Objective

The main goals of the project are:

- Develop a simple, functional web application.
- Gain hands-on experience using Docker to containerize an application.
- Use Docker Compose to orchestrate and run services together.
- Push the Docker image to DockerHub.

---

## ⚙️ Features

1. Perform basic math operations: addition, subtraction, multiplication, division.
2. Stylish, responsive user interface using HTML and CSS.
3. Operation history to track previously performed calculations.

---

## 🧰 Tech Stack

- HTML, CSS, JavaScript
- Docker
- Docker Compose

---

## 🐳 Docker Container

### Dockerfile

A `Dockerfile` was created to:

- Use a lightweight `nginx` server to serve the app.
- Copy the project files into the `nginx/html` directory.

### DockerHub

The Docker image was built and pushed using:

```bash
docker build -t mariam1999/calculator-app .
docker push mariam1999/calculator-app
