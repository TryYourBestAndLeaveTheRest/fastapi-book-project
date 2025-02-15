# FastAPI Book Project

## Overview

This project is a FastAPI application that provides an API for managing books. It includes a CI/CD pipeline using GitHub Actions and is deployed on an AWS EC2 instance with Nginx as a reverse proxy.

## Features

- Retrieve books by ID
- CI pipeline for automated testing
- CD pipeline for automated deployment
- Deployed on an AWS EC2 instance
- Served using Nginx as a reverse proxy

## Setup Instructions

### Prerequisites || Technology Used

Ensure you have the following installed:

- Python 3.8+
- Virtualenv
- Git
- Uvicorn
- Nginx (for deployment)

### Clone the Repository

```bash
git clone https://github.com/TryYourBestAndLeaveTheRest/fastapi-book-project.git
cd fastapi-book-project
```

### Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate  # For Windows
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application Locally

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The application should now be accessible at `http://127.0.0.1:8000`.

## Implemented Endpoint

### Get Book by ID

- **Endpoint:** `GET /api/v1/books/{book_id}`
- **Response:**
  - `200 OK`: Returns book details in JSON format.
  - `404 Not Found`: If the book does not exist.

## CI/CD Setup

### CI Pipeline (Testing)

- Runs on pull requests to the `main` branch.
- Executes `pytest` to run automated tests.
- Workflow file: `.github/workflows/test.yml`

### CD Pipeline (Deployment)

- Runs on merging to the `main` branch.
- Deploys the latest code to the EC2 instance.
- Workflow file: `.github/workflows/deploy.yml`

## Deployment on AWS EC2

### Install Dependencies on EC2

```bash
sudo apt update && sudo apt install -y python3-pip python3-venv nginx
```

### Setup FastAPI Service

```bash
sudo nano /etc/systemd/system/fastapi.service
```

**Paste the following:**

```ini
[Unit]
Description=FastAPI Application
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/path/to/the/project/folder
ExecStart=/path/to/the/project/folder/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
```

Save and exit, then run:

```bash
sudo systemctl daemon-reload
sudo systemctl enable fastapi
sudo systemctl start fastapi
```

### Configure Nginx

```bash
sudo nano /etc/nginx/sites-available/fastapi
```

**Paste the following:**

```nginx
server {
    listen 80;
    server_name YOUR_EC2_PUBLIC_IP;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

Save and exit, then run:

```bash
sudo ln -s /etc/nginx/sites-available/fastapi /etc/nginx/sites-enabled/
sudo systemctl restart nginx
```

## Links

- **Base URL:** `http://ec2-16-170-211-208.eu-north-1.compute.amazonaws.com`
- **GitHub Repository:** `https://github.com/TryYourBestAndLeaveTheRest/fastapi-book-project`


## Useful links

-**Fast Api Docs:** `https://fastapi.tiangolo.com/`
-**Nginx Docs:** `https://nginx.org/en/docs/`
-**Github Actions:** `https://docs.github.com/en/actions`
## License

This project is licensed under the MIT License.
