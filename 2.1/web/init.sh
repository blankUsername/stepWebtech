ln -sf /home/box/stepWebtech/2.1/web /home/box/web
sudo unlink /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/gunicorn.hello.py /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/gunicorn.ask.py /etc/gunicorn.d/ask.py
sudo mkdir /var/run/gunicorn && chmod a+x+w /var/run/gunicorn
sudo mkdir /var/log/gunicorn && chmod a+x+w /var/log/gunicorn
sudo /etc/init.d/nginx restart
sudo gunicorn -c /etc/gunicorn.d/hello.py  hello:app
sudo gunicorn -c /etc/gunicorn.d/ask.py  ask.ask.wsgi:application
