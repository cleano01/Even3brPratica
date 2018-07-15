from django.db import models

# Create your models here.


class Certificado(models.Model):
    image=models.FileField(upload_to='%Y/%m/%d/', blank = True)

