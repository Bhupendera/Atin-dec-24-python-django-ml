cd day-3\mini-project\hands-on\bookmarks
python -m venv venv
venv\Scripts\activate.bat
#set PIP_DISABLE_PIP_VERSION_CHECK=1
#set PYTHONDONTWRITEBYTECODE=1
#set PYTHONUNBUFFERED=1
pip install -r requirements.txt
#pip install psycopg[binary]

python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations account
python manage.py makemigrations images
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000


## For Docker:
docker compose up -d

# Optional commands
docker compose logs
docker compose logs
docker compose logs -f
#docker compose exec web_run bash
docker compose ps
docker compose exec web_run python /code/bookmarks/manage.py migrate
docker compose exec web_run python /code/bookmarks/manage.py createsuperuser
docker compose stop
docker compose restart
docker compose down
docker images
