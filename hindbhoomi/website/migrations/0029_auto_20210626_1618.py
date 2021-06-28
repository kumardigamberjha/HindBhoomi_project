# Generated by Django 3.1.7 on 2021-06-26 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0028_auto_20210622_2223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='source_name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='source_number',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='total_ticket',
        ),
        migrations.AddField(
            model_name='booking',
            name='contact_gender',
            field=models.CharField(default='male', max_length=10),
        ),
        migrations.AddField(
            model_name='booking',
            name='return_date',
            field=models.DateField(auto_now=True),
        ),
    ]