# Generated by Django 2.0.2 on 2018-03-06 23:46

from django.db import migrations, models


class Migration(migrations.Migration):
	dependencies = [
		('TEDx2018', '0007_auto_20180306_2344'),
	]

	operations = [
		migrations.AlterField(
			model_name='speaker',
			name='PresentationReleaseDateTime',
			field=models.DateTimeField(blank=True, default=None),
		),
	]