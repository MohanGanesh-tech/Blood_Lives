# Generated by Django 3.0.4 on 2020-10-08 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodlivesapp', '0007_auto_20201008_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]