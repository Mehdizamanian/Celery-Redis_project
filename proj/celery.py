from __future__ import absolute_import , unicode_literals # used while using proj folder 
from celery import Celery

app = Celery('proj')
app.config_from_object('proj.celeryconfig')#configuring celery from celeryconfig.py testing >>> python -m configcelery

# checked if proj folder exsists 
if __name__ == '__main__':
    app.start()