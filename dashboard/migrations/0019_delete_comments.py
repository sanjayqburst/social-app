# Generated by Django 3.2.7 on 2021-09-29 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_remove_comments_commented_by'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
