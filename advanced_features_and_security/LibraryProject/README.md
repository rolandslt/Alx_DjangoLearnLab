# LibraryProject – Security & Deployment Guide

## 1. Project Objective
Enhance the security of the Django application and deploy it with HTTPS support, enforcing secure connections and protecting user data.

---

## 2. HTTPS Deployment Configuration

### Web Server
- Use **Nginx** as a reverse proxy.
- Run Django with **Gunicorn**.

### SSL/TLS Certificates
- Install Certbot:
```bash
sudo apt install certbot python3-certbot-nginx
