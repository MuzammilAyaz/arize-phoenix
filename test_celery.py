from app.celery import  something

# creating a celery 
results = something.delay()
print(results)
print(results.status)


# checking results
# results =  something.AsyncResult("91f6a861-d8e1-4320-b17d-ae7ac91bbe6f")
# print(results.status)
