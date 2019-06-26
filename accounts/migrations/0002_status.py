# Generated by Django 2.1 on 2019-06-12 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SIG', models.CharField(choices=[('CO', 'Code'), ('GD', 'Gadget'), ('GR', 'Garage'), ('SR', 'Script'), ('VR', 'Vriddhi'), ('RO', 'Robotics'), ('CA', 'Capital'), ('ME', 'Media')], max_length=2, null=True)),
                ('status', models.CharField(choices=[('WR', 'Written Round'), ('TE', 'Technical'), ('HR', 'HR')], max_length=2)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Account')),
            ],
        ),
    ]