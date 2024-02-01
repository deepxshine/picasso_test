from django.db import models


class File(models.Model):
    file = models.FileField(upload_to='files')
    uploaded_at = models.DateTimeField(auto_now_add=True, )
    processed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'file №{self.id}'
