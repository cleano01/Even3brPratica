from django.db import models

# Create your models here.


class Certificado(models.Model):
    image=models.FileField( blank = True)

