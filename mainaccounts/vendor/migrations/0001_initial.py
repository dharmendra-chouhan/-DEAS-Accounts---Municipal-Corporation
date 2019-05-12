# Generated by Django 2.0 on 2019-03-17 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vid', models.CharField(max_length=20)),
                ('vname', models.CharField(max_length=100)),
                ('vaddress', models.CharField(max_length=200)),
                ('vemail', models.EmailField(max_length=254)),
                ('vcontact', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'vendor',
            },
        ),
    ]
