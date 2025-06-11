from __future__ import absolute_import , unicode_literals # used while using proj folder 
from .celery import app



""" Tasks Functions """
@app.task
def add(x,y):
    return x + y


@app.task
def divide(x,y):
    return x/y

@app.task
def zarb(x,y):
    return x*y


""" tip => if u added newtask restart celery"""

"""commands to run worker and so on """
# turn on redis on ur pc then actvie venv
# celery -A proj worker --loglevel=INFO --pool=solo
