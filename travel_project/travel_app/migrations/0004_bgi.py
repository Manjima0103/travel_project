# Generated by Django 4.1.7 on 2023-05-14 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0003_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='bgi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
