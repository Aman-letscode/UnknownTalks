# Generated by Django 4.1 on 2022-08-13 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_blogcomments'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogComments',
        ),
    ]
