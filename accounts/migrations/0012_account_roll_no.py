# Generated by Django 2.1 on 2019-08-03 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20190802_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='roll_no',
            field=models.CharField(max_length=10, null=True),
        ),
    ]