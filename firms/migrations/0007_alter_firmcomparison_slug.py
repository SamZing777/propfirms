# Generated by Django 3.2.9 on 2021-11-29 08:54

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firms', '0006_auto_20211128_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firmcomparison',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='firmA, firmB', unique=True),
        ),
    ]
