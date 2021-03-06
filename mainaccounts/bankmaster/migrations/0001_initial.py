# Generated by Django 2.1.7 on 2019-05-29 12:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lookup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bankmaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bankcode', models.CharField(max_length=20)),
                ('bankname', models.CharField(max_length=100)),
                ('branch', models.TextField(max_length=200)),
                ('bankaddress', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Bankmasterdet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bankaccountno', models.CharField(max_length=25)),
                ('nameofaccount', models.CharField(max_length=200)),
                ('narration', models.CharField(max_length=200)),
                ('accountopeningdate', models.DateField(default=datetime.datetime.today)),
                ('statusofaccount', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], default='Y', max_length=1)),
                ('bankaccounttype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BANKTYPE', to='lookup.Lookupdet')),
            ],
        ),
    ]
