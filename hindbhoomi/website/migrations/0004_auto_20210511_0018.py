# Generated by Django 3.1.7 on 2021-05-10 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_state_capital'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='history',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='state',
            name='imag2',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='state',
            name='imag3',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='state',
            name='imag4',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='state',
            name='imag5',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='state',
            name='imag6',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='state',
            name='imag7',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='state',
            name='imag8',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='state',
            name='img1',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
