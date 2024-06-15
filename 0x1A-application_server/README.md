0x1A-application_server


gunicorn --bind 0.0.0.0:5003 web_dynamic.2-hbnb:app


sudo vi
sudo systemctl daemon-reload
/etc/systemd/system/gunicorn.service
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo systemctl status gunicorn


$ pwd
/home/ubuntu/AirBnB_clone_v4
$ touch /tmp/airbnb-access.log
$ touch /tmp/airbnb-error.log
$ chmod 666 /tmp/airbnb-access.log
$ chmod 666 /tmp/airbnb-error.log
