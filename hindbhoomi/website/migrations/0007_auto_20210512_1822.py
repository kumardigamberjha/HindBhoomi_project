# Generated by Django 3.1.7 on 2021-05-12 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20210512_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='messages',
            name='message',
            field=models.TextField(default=''),
        ),
    ]
