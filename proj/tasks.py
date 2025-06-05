from __future__ import absolute_import , unicode_literals # used while using proj folder 
from .celery import app



""" Tasks Functions """
@app.task
def add(x,y):
    return x + y


@app.task
def divide(x,y):
    return x/y



"""commands to run worker and so on """
# turn on redis on ur pc then actvie venv
# celery -A tasks worker --loglevel=INFO --pool=solo
