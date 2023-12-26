# Generated by Django 5.0 on 2023-12-26 10:05

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_customuser_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='code',
            field=models.ImageField(default=1, upload_to='images/', verbose_name='Код товара'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ServicesDetail',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.services')),
            ],
        ),
    ]
