# Generated by Django 3.2.7 on 2021-09-21 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_content_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]