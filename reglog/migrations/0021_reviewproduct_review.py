# Generated by Django 3.1 on 2021-02-07 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reglog', '0020_reviewproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewproduct',
            name='review',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
