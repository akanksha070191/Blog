# Generated by Django 5.1.6 on 2025-03-04 06:34

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_commentpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
