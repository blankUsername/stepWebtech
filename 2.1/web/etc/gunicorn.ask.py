workers = 2
bind = '0.0.0.0:8000'
pidfile = '/var/run/gunicorn/ask.pid'
user = 'www-data'
daemon = True
errorlog = '/var/log/gunicorn/error-ask.log'
accesslog = '/var/log/gunicorn/access-ask.log'
proc_name = 'gunicorn-ask'
