# Generated by Django 3.1.7 on 2021-06-14 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20210615_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='dance_name',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='state',
            name='food_name',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
