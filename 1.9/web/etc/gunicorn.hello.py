workers = 3
bind = '0.0.0.0:8000'
pidfile = '/var/run/gunicorn/hello.pid'
user = 'www-data'
daemon = True
errorlog = '/var/log/gunicorn/error-hello.log'
accesslog = '/var/log/gunicorn/access-hello.log'
proc_name = 'gunicorn-hello'
