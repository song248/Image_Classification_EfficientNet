# Generated by Django 3.1.3 on 2020-11-17 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]