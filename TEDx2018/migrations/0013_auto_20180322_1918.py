# Generated by Django 2.0.2 on 2018-03-22 17:18

from django.db import migrations, models


class Migration(migrations.Migration):
	dependencies = [
		('TEDx2018', '0012_auto_20180321_1825'),
	]

	operations = [
		migrations.AddField(
			model_name='event',
			name='Reddit',
			field=models.CharField(blank=True, max_length=100),
		),
		migrations.AddField(
			model_name='speaker',
			name='Reddit',
			field=models.CharField(blank=True, max_length=100),
		),
		migrations.AddField(
			model_name='teammember',
			name='Reddit',
			field=models.CharField(blank=True, max_length=100),
		),
	]
