# Generated by Django 3.0.5 on 2020-06-15 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ultrasonic', '0007_delete_bot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ultrasonic',
            name='body',
        ),
        migrations.AddField(
            model_name='ultrasonic',
            name='file',
            field=models.FileField(default='default.pdf', upload_to=''),
        ),
    ]
