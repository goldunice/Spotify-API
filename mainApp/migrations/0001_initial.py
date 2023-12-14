# Generated by Django 5.0 on 2023-12-11 06:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('sana', models.DateField(blank=True, null=True)),
                ('rasm', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Qoshiqchi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=255)),
                ('tugilgan_yil', models.DateField(blank=True, null=True)),
                ('davlat', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Qoshiq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('janr', models.CharField(max_length=255)),
                ('davomiylik', models.DurationField(blank=True, null=True)),
                ('fayl', models.FileField(null=True, upload_to='')),
                ('albom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.albom')),
            ],
        ),
        migrations.AddField(
            model_name='albom',
            name='qoshiqchi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.qoshiqchi'),
        ),
    ]
