# Generated by Django 2.0.4 on 2018-04-30 15:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
	dependencies = [
		('TEDx2018', '0031_auto_20180420_1157'),
	]

	operations = [
		migrations.CreateModel(
			name='Workshop',
			fields=[
				('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('ProfileImage', models.ImageField(blank=True, default='TEDx2018/Shared/XWhite.svg', upload_to='TEDx2018/SpeakerProfilePictures/')),
				('Title', models.CharField(blank=True, max_length=100)),
				('Description', models.TextField(blank=True)),
				('AnnouncementDateTime', models.DateTimeField(blank=True, default=None, null=True)),
				('Facebook', models.CharField(blank=True, max_length=100)),
				('GitHub', models.CharField(blank=True, max_length=100)),
				('GooglePlus', models.CharField(blank=True, max_length=100)),
				('Instagram', models.CharField(blank=True, max_length=100)),
				('LinkedIn', models.CharField(blank=True, max_length=100)),
				('Pinterest', models.CharField(blank=True, max_length=100)),
				('Reddit', models.CharField(blank=True, max_length=100)),
				('Twitter', models.CharField(blank=True, max_length=100)),
				('YouTube', models.CharField(blank=True, max_length=100)),
				('InternetLink', models.CharField(blank=True, max_length=100)),
			],
		),
		migrations.AddField(
			model_name='event',
			name='HasAnnouncedWorkshops',
			field=models.BooleanField(default=False),
		),
		migrations.AddField(
			model_name='workshop',
			name='Event',
			field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TEDx2018.Event'),
		),
	]
