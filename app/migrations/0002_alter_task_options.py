# Generated by Django 5.1.1 on 2024-09-25 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['done', '-created_at']},
        ),
    ]
