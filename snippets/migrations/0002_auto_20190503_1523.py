# Generated by Django 2.1.7 on 2019-05-03 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='highlighted',
            field=models.TextField(default=''),
        ),
    ]
