# Generated by Django 5.1.3 on 2024-11-24 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='classes/image')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('instructor', models.CharField(max_length=100)),
                ('hold_on', models.DateTimeField()),
                ('duration', models.DurationField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('difficulty_level', models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], max_length=50)),
                ('online_meeting_link', models.URLField()),
                ('status', models.CharField(choices=[('upcoming', 'Upcoming'), ('running', 'Running'), ('completed', 'Completed'), ('canceled', 'Canceled')], max_length=20)),
                ('category', models.CharField(max_length=100)),
            ],
        ),
    ]
