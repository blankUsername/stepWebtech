ln -sf /home/box/stepWebtech/1.9/web /home/box/web
sudo unlink /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/gunicorn.hello.py /etc/gunicorn/hello.py
sudo /etc/init.d/nginx restart
sudo gunicorn -c /etc/gunicorn/hello.py  hello:app
