Запуск: 
pip install requirements.txt
python manage.py runserver 0.0.0.0:8001
или
uwsgi --socket mysite.sock --module mysite.wsgi--chmod-socket=666
админка:
admin
admin