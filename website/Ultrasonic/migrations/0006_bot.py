# Generated by Django 3.0.5 on 2020-06-15 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ultrasonic', '0005_auto_20200614_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
