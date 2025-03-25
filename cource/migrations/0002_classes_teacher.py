# Generated by Django 5.0.2 on 2025-03-25 11:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cource', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cource.teacher', verbose_name='Преподаватель'),
            preserve_default=False,
        ),
    ]
