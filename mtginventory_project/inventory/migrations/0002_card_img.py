# Generated by Django 2.2.5 on 2020-03-27 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='img',
            field=models.URLField(default=0, max_length=400),
            preserve_default=False,
        ),
    ]
