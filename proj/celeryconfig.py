
broker_url='redis://localhost:6379'
result_backend='redis://localhost:6379'     #backend 
include=['proj.tasks']   #used for haing proj folder to include tasks


task_serializer='json'
result_serializer='json'

accept_content=['json']
time_zone='Asia/Tehran'