# Generated by Django 2.0.2 on 2018-03-06 23:47

from django.db import migrations, models


class Migration(migrations.Migration):
	dependencies = [
		('TEDx2018', '0008_auto_20180306_2346'),
	]

	operations = [
		migrations.AlterField(
			model_name='speaker',
			name='AnnouncementDateTime',
			field=models.DateTimeField(blank=True, default=None),
		),
		migrations.AlterField(
			model_name='sponsor',
			name='AnnouncementDateTime',
			field=models.DateTimeField(blank=True, default=None),
		),
	]