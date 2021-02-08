# Generated by Django 3.1 on 2021-02-07 15:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reglog', '0019_product_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
            ],
            options={
                'db_table': 'reviewproduct',
            },
        ),
    ]