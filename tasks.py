from celery import Celery

app = Celery('tasks') 
app.config_from_object('celeryconfig')#configuring celery from celeryconfig.py testing >>> python -m configcelery




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
