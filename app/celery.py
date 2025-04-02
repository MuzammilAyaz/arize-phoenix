from celery import Celery
from time import sleep
app = Celery('celery', 
             broker='redis://localhost:6380', 
             backend='redis://localhost:6380'
            )

# app.conf.update(
#     result_backend='redis://localhost:6379/1',  # Ensure it's set
#     task_ignore_result=False,  # Force Celery to store results
#     result_extended=True,  # Store additional metadata
#     result_expires=3600  # Keep results for 1 hour
# )


@app.task
def something():
    sleep(5)
    return True
