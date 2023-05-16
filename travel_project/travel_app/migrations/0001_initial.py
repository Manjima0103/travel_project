# Generated by Django 4.1.7 on 2023-05-14 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('des', models.TextField()),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]