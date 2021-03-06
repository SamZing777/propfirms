# Generated by Django 3.2.9 on 2021-11-29 10:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firms', '0009_firmcomparison_rules'),
    ]

    operations = [
        migrations.RenameField(
            model_name='firmcomparison',
            old_name='rules',
            new_name='firm_a_rules',
        ),
        migrations.AddField(
            model_name='firmcomparison',
            name='firm_b_rules',
            field=models.SmallIntegerField(default=4, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
