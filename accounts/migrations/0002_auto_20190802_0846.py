# Generated by Django 2.1 on 2019-08-02 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.IntegerField(choices=[(1, 'Admin'), (2, 'Member'), (3, 'Candidate'), (4, 'Aux SIG Admin')], default=0),
        ),
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(choices=[('RE', 'Application Accepted'), ('WR', 'Written Round'), ('TE', 'Technical'), ('HR', 'HR')], max_length=2),
        ),
    ]