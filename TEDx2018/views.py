from random import shuffle

from django.shortcuts import render

from TEDx2018.models import *


def getTeamAndTeamMembers(event):
	teams = event.team_set.order_by('Name')
	teamsList = []
	for team in teams:
		teamMembersAssignment = list(TeamMemberAssignment.objects.filter(Team=team).only('TeamMember').order_by('TeamMember__Position', 'TeamMember__Name', 'TeamMember__Surname'))
		teamsList.append({'Name': team.Name, 'Photo': team.Photo.url, 'PhotoDescription': team.PhotoDescription, 'TeamMembersAssignment': teamMembersAssignment})
	return teamsList


def home(request):
	events = Event.objects.order_by('-StartDateTime')
	return render(request=request, template_name='TEDx2018/home.html', context={'events': events})


def currentEvent(request):
	return render(request=request, template_name='TEDx2018/404.html')


def upcomingEvents(request):
	return render(request=request, template_name='TEDx2018/404.html')


def previousEvents(request):
	return render(request=request, template_name='TEDx2018/404.html')


def event(request, eventName):
	eventName = eventName.replace('_', ' ')
	event = Event.objects.filter(Name=eventName).first()
	teams = getTeamAndTeamMembers(event)
	return render(request=request, template_name='TEDx2018/event.html', context={'event': event, 'teams': teams})


def talks(request):
	events = Event.objects.order_by('-StartDateTime')
	return render(request=request, template_name='TEDx2018/talks.html', context={'events': events})


def speakers(request):
	events = Event.objects.order_by('-StartDateTime')
	return render(request=request, template_name='TEDx2018/speakers.html', context={'events': events})


def speakerProfile(request, fullName):
	name, surname = fullName.split('_')
	speaker = Speaker.objects.filter(Name=name, Surname=surname).first()
	return render(request=request, template_name='TEDx2018/speakerProfile.html', context={'speaker': speaker})


def partners(request):
	events = []
	eventstmp = Event.objects.exclude(AnnouncementDateTime__gt=datetime.now().astimezone()).order_by('-StartDateTime')
	for event in eventstmp:
		partnersList = []
		for partnerLevel in event.partnerlevel_set.all().order_by('Level'):
			partnersList.append({'Name': partnerLevel.Name, 'partners': event.partner_set.filter(PartnerLevel=partnerLevel)})
		events.append({'Name': event.Name, 'partnerLevels': partnersList})
	return render(request=request, template_name='TEDx2018/partners.html', context={'events': events})


def becomeAPartner(request):
	return render(request=request, template_name='TEDx2018/becomeAPartner.html')


def community(request):
	return render(request=request, template_name='TEDx2018/community.html')


def joinAsAMember(request):
	return render(request=request, template_name='TEDx2018/joinAsAMember.html')


def donors(request):
	return render(request=request, template_name='TEDx2018/donors.html')


def becomeADonor(request):
	return render(request=request, template_name='TEDx2018/becomeADonor.html')


def about(request):
	photos = list(AboutUsCarouselPhoto.objects.all())
	shuffle(photos)
	teams = getTeamAndTeamMembers(Event.objects.order_by('-StartDateTime').first())
	return render(request=request, template_name='TEDx2018/about.html', context={'photos': photos, 'teams': teams})


def teamMemberProfile(request, fullName):
	name, surname = fullName.split('_')
	teamMember = TeamMember.objects.filter(Name=name, Surname=surname).first()
	return render(request=request, template_name='TEDx2018/teamMemberProfile.html', context={'teamMember': teamMember})


def ourTeam(request):
	return render(request=request, template_name='TEDx2018/ourTeam.html')


def contactUs(request):
	return render(request=request, template_name='TEDx2018/contactUs.html')


def becomeAVolunteer(request):
	return render(request=request, template_name='TEDx2018/becomeAVolunteer.html')


def faq(request):
	return render(request=request, template_name='TEDx2018/faq.html')


def custom_404(request):
	return render(request=request, template_name='TEDx2018/404.html')


def custom_500(request):
	return render(request=request, template_name='TEDx2018/500.html')
