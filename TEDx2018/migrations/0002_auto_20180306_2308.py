# Generated by Django 2.0.2 on 2018-03-06 23:08

from django.db import migrations, models


class Migration(migrations.Migration):
	dependencies = [
		('TEDx2018', '0001_initial'),
	]

	operations = [
		migrations.AlterField(
			model_name='teammember',
			name='ProfileImage',
			field=models.ImageField(blank=True, default='defaultProfile.png', upload_to=''),
		),
	]