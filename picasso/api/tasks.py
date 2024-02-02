from time import sleep

from picasso.celery import app

from .models import File


@app.task()
def handling(pk):
    file = File.objects.get(id=pk)
    print(file)
    file.processed = True
    file.save()
