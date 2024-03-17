Sure, here's the updated content with the MIT License included:

# Flask MySQL Application

## Overview

This repository contains a Flask application that interacts with a MySQL database. Follow the instructions below to set up and run the application using Docker.

## Setup Instructions

### Step 1: Build Docker Image

Build the Docker image using the following command:

```bash
docker build -t flask-mysql-app .
```

### Step 2: Run MySQL Docker Container

Run a MySQL Docker container with the required configurations:

```bash
docker run -d --name mysql -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=sys mysql:latest
```

### Step 3: Run Flask Application

Run the Flask application Docker container, linking it to the MySQL container and exposing port 5000:

```bash
docker run -d --name flask-app -p 5000:5000 --link mysql:mysql flask-mysql-app
```

## Accessing the Application

Once the containers are up and running, you can access the Flask MySQL application through port 5000 on your localhost.

```plaintext
http://localhost:5000
```