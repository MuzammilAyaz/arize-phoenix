
from app.celery import  something
results =  something.AsyncResult("5ed05f37-dbb3-436a-b6f6-d146c457134d")
print(results.status)