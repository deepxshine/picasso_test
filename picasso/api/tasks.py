from time import sleep

from celery import shared_task

from .models import File


class HandlingErorr(BaseException):
    pass


@shared_task()
def handling(serializer):
    sleep(10)
    pk = serializer.data['id']
    file = File.objects.get(id=(int(pk)+10))
    file.update(processed=True)