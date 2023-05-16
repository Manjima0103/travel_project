# Generated by Django 4.1.7 on 2023-05-14 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('des', models.TextField()),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
