export FLASK_APP=bluehat.py
heroku ps:scale web=1
web: gunicorn --worker-class eventlet -w 1 bluehat:app
