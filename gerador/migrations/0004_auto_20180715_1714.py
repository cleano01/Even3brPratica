# Generated by Django 2.0.6 on 2018-07-15 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerador', '0003_auto_20180715_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificado',
            name='image',
            field=models.FileField(blank=True, upload_to='%Y/%m/%d/'),
        ),
    ]
