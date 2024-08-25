# Generated by Django 5.1 on 2024-08-25 03:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        ('retailer', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Briefing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('responsible', models.CharField(max_length=255)),
                ('release_date', models.DateField()),
                ('available', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
                ('retailer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retailer.retailer')),
            ],
        ),
    ]
