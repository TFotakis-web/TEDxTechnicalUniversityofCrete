from django.db import models


class TeamMember(models.Model):
	Name = models.CharField(max_length=100)
	Surname = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	Telephone = models.IntegerField()
	University = models.CharField(max_length=100)
	School = models.CharField(max_length=100)
	EducationalLevel = models.CharField(max_length=100)
	ProfileImage = models.ImageField(max_length=100)
	Bio = models.TextField()
	Facebook = models.CharField(max_length=100)
	GitHub = models.CharField(max_length=100)
	GooglePlus = models.CharField(max_length=100)
	Instagram = models.CharField(max_length=100)
	LinkedIn = models.CharField(max_length=100)
	Pinterest = models.CharField(max_length=100)
	Twitter = models.CharField(max_length=100)

	@property
	def FullName(self):
		return self.Name + self.Surname

	def __str__(self):
		return self.FullName
