# Generated by Django 3.2.9 on 2021-11-28 19:58

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('firms', '0005_alter_cashrebate_expects'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cashrebate',
            options={'ordering': ['user']},
        ),
        migrations.AlterModelOptions(
            name='propfirm',
            options={'ordering': ['name']},
        ),
        migrations.CreateModel(
            name='FirmComparison',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=('firmA', 'firmB'), unique=True)),
                ('comment', models.CharField(blank=True, max_length=200, null=True)),
                ('date_updated', models.DateField()),
                ('firmA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='firm_A', to='firms.propfirm')),
                ('firmB', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='firm_B', to='firms.propfirm')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['firmA'],
            },
        ),
    ]
