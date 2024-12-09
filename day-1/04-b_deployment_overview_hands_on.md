# Hands-On: Deployment Overview of Python Projects

## Prerequisites
1. Install Python (3.x) and Django on your machine.
2. Install additional tools like `Gunicorn` and `NGINX` as required.

---

## Task 1: Deploy Locally Using Gunicorn
1. Install Gunicorn:
   ```bash
   pip install gunicorn
   ```
2. Run the Django project using Gunicorn:
   ```bash
   gunicorn myproject.wsgi:application
   ```
3. Access the application at `http://127.0.0.1:8000`.

---

## Task 2: Configure Static Files for Production
1. Update `settings.py`:
   ```python
   STATIC_ROOT = BASE_DIR / "staticfiles"
   ```
2. Collect static files:
   ```bash
   python manage.py collectstatic
   ```
3. Verify that the static files are in the `staticfiles` directory.

---

## Task 3: Set Up a Reverse Proxy with NGINX
1. Install NGINX:
   ```bash
   sudo apt install nginx
   ```
2. Create an NGINX configuration file for your project:
   ```bash
   sudo nano /etc/nginx/sites-available/myproject
   ```
   Add the following content:
   ```nginx
   server {
       server_name your-domain.com;

       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
       }

       location /static/ {
           alias /path/to/staticfiles/;
       }
   }
   ```
3. Enable the configuration and restart NGINX:
   ```bash
   sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
   sudo systemctl restart nginx
   ```

---

## Task 4: Deploy to Heroku
1. Install the Heroku CLI:
   ```bash
   curl https://cli-assets.heroku.com/install.sh | sh
   ```
2. Create a `Procfile` in your project directory:
   ```bash
   echo "web: gunicorn myproject.wsgi:application" > Procfile
   ```
3. Login to Heroku and create a new app:
   ```bash
   heroku login
   heroku create myproject
   ```
4. Deploy your project:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   heroku git:remote -a myproject
   git push heroku main
   ```

---

## Additional Exercises
1. Deploy your project to AWS Elastic Beanstalk or DigitalOcean.
2. Configure HTTPS using an SSL certificate with NGINX.
3. Experiment with scaling your application using Gunicorn workers:
   ```bash
   gunicorn --workers 3 myproject.wsgi:application
   ```
```

---