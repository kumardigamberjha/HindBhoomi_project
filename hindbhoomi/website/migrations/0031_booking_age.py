# Generated by Django 3.1.7 on 2021-06-26 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0030_auto_20210626_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
