# Generated by Django 5.1.3 on 2024-11-24 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='auto_renew',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='expire_date',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='start_date',
        ),
    ]
