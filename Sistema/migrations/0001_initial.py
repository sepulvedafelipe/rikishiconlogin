# Generated by Django 2.1.2 on 2019-05-08 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut', models.CharField(blank=True, max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=30)),
                ('apellido', models.CharField(blank=True, max_length=30)),
                ('telefono', models.CharField(blank=True, max_length=20)),
                ('correo', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]