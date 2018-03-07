from django.db import models


class Position(models.Model):
	Name = models.CharField(max_length=100)

	def __str__(self): return self.Name


class TeamMember(models.Model):
	Name = models.CharField(max_length=100)
	Surname = models.CharField(max_length=100)
	Position = models.ForeignKey(Position, on_delete=models.SET_DEFAULT, default=1)
	email = models.CharField(max_length=100)
	Telephone = models.IntegerField()
	University = models.CharField(max_length=100)
	School = models.CharField(max_length=100)
	EducationalLevel = models.CharField(max_length=100)
	ProfileImage = models.ImageField(default='TEDx2018/Shared/defaultProfile.png', blank=True, upload_to='TEDx2018/TeamMemberProfilePictures/')
	Bio = models.TextField(blank=True)
	Facebook = models.CharField(max_length=100, blank=True)
	GitHub = models.CharField(max_length=100, blank=True)
	GooglePlus = models.CharField(max_length=100, blank=True)
	Instagram = models.CharField(max_length=100, blank=True)
	LinkedIn = models.CharField(max_length=100, blank=True)
	Pinterest = models.CharField(max_length=100, blank=True)
	Twitter = models.CharField(max_length=100, blank=True)
	YouTube = models.CharField(max_length=100, blank=True)

	@property
	def FullName(self): return self.Name + ' ' + self.Surname

	def __str__(self): return self.FullName


class Team(models.Model):
	Name = models.CharField(max_length=100)

	def __str__(self): return self.Name


class TeamMemberAssignment(models.Model):
	TeamMember = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
	Team = models.ForeignKey(Team, on_delete=models.CASCADE, default=1)

	def __str__(self): return str(self.TeamMember) + ' - ' + str(self.Team)


class Speaker(models.Model):
	Name = models.CharField(max_length=100)
	Surname = models.CharField(max_length=100)
	email = models.CharField(max_length=100, blank=True)
	Telephone = models.IntegerField(blank=True, null=True)
	ProfileImage = models.ImageField(default='TEDx2018/Shared/defaultProfile.png', blank=True, upload_to='TEDx2018/SpeakerProfilePictures/')
	Bio = models.TextField(blank=True)
	AnnouncementDateTime = models.DateTimeField(default=None, blank=True, null=True)
	Announced = models.BooleanField(default=False)
	Presentation = models.FileField(blank=True, upload_to='TEDx2018/SpeakerPresentations/')
	PresentationReleaseDateTime = models.DateTimeField(default=None, blank=True, null=True)
	PresentationRelease = models.BooleanField(default=False)
	Facebook = models.CharField(max_length=100, blank=True)
	GitHub = models.CharField(max_length=100, blank=True)
	GooglePlus = models.CharField(max_length=100, blank=True)
	Instagram = models.CharField(max_length=100, blank=True)
	LinkedIn = models.CharField(max_length=100, blank=True)
	Pinterest = models.CharField(max_length=100, blank=True)
	Twitter = models.CharField(max_length=100, blank=True)
	YouTube = models.CharField(max_length=100, blank=True)
	InternetLink = models.CharField(max_length=100, blank=True)

	@property
	def FullName(self): return self.Name + ' ' + self.Surname

	def __str__(self): return self.FullName


class SponsorLevel(models.Model):
	Name = models.CharField(max_length=100)

	def __str__(self): return self.Name


class Sponsor(models.Model):
	CompanyName = models.CharField(max_length=100)
	SponsorLevel = models.ForeignKey(SponsorLevel, on_delete=models.CASCADE, default=1)
	Name = models.CharField(max_length=100, blank=True)
	Surname = models.CharField(max_length=100, blank=True)
	email = models.CharField(max_length=100, blank=True)
	Telephone = models.IntegerField(blank=True, null=True)
	Logo = models.ImageField(default='TEDx2018/Shared/defaultSponsorLogo.png', blank=True, upload_to='TEDx2018/SponsorLogos/')
	AnnouncementDateTime = models.DateTimeField(default=None, blank=True, null=True)
	Announced = models.BooleanField(default=False)
	InternetLink = models.CharField(max_length=100, blank=True)

	def __str__(self): return self.CompanyName + ' - ' + str(self.SponsorLevel)
