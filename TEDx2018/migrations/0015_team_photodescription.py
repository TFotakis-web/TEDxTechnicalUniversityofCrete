# Generated by Django 2.0.2 on 2018-03-23 22:52

from django.db import migrations, models


class Migration(migrations.Migration):
	dependencies = [
		('TEDx2018', '0014_team_photo'),
	]

	operations = [
		migrations.AddField(
			model_name='team',
			name='PhotoDescription',
			field=models.CharField(blank=True, max_length=100),
		),
	]