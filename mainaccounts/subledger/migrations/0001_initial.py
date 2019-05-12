# Generated by Django 2.2 on 2019-05-03 15:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accountcode', '0001_initial'),
        ('lookup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subledger_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opening_bal', models.DecimalField(decimal_places=2, max_digits=15)),
                ('opening_bal_date', models.DateField(default=datetime.datetime.today)),
                ('subledger_code', models.CharField(max_length=20)),
                ('subledger_desc', models.CharField(max_length=200)),
                ('budget_provion_required', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Lookupdet_budget', to='lookup.Lookupdet')),
                ('function_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Function', to='accountcode.Function_master')),
                ('lookupdet_bug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Budget', to='lookup.Lookupdet')),
                ('lookupdet_opening_drcr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Lookupdet', to='lookup.Lookupdet')),
                ('object_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Object', to='accountcode.Object_master')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Lookupdet_status', to='lookup.Lookupdet')),
            ],
        ),
    ]
