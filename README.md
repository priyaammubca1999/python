# Python EC2 API

A simple Python Flask REST API for AWS EC2 deployment.

## Endpoints

- GET /
- GET /api/health
- GET /api/users
- GET /api/users/1

## Local setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

## Production

```bash
gunicorn --bind 0.0.0.0:5000 app:app
```

## AWS EC2 - Amazon Linux 2023

```bash
sudo dnf update -y
sudo dnf install python3 python3-pip -y
python3 --version
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

For testing, allow TCP port 5000 in the EC2 Security Group.
