from celery import Celery

app = Celery('tasks',backend='redis://localhost:6379',broker='redis://localhost:6379') #backend redis added for saving funcs results 


@app.task
def add(x,y):
    return x + y


@app.task
def divide(x,y):
    return x/y



"""commands to run worker and so on """
# turn on redis on ur pc then actvie venv
# celery -A tasks worker --loglevel=INFO --pool=solo
