from datetime import datetime
from random import shuffle

from django.http import HttpResponse
from django.shortcuts import render

from .models import Event, TeamMember, TeamMemberAssignment, Speaker, AboutUsCarouselPhoto, getTicketsNumber


def getTeamAndTeamMembers(event):
	teams = event.team_set.order_by('Name')
	teamsList = []
	for team in teams:
		teamMembersAssignment = list(
			TeamMemberAssignment
				.objects
				.filter(Team=team)
				.only('TeamMember')
				.order_by('TeamMember__Position', 'TeamMember__Name', 'TeamMember__Surname')
		)
		teamsList.append({
			'Name': team.Name,
			'Photo': team.Photo.url,
			'PhotoDescription': team.PhotoDescription,
			'TeamMembersAssignment': teamMembersAssignment
		})
	return teamsList


def homeView(request):
	events = Event.objects.order_by('-StartDateTime')
	return render(request=request, template_name='TEDx2018/home.html', context={'events': events})


def currentEventView(request):
	return render(request=request, template_name='TEDx2018/404.html')


def upcomingEventsView(request):
	events = Event.objects.filter(EndDateTime__gte=datetime.now().astimezone()).order_by('-StartDateTime')
	return render(request=request, template_name='TEDx2018/eventsListView.html', context={'events': events, 'eventType': 'Upcoming'})


def previousEventsView(request):
	events = Event.objects.filter(EndDateTime__lte=datetime.now().astimezone()).order_by('-StartDateTime')
	return render(request=request, template_name='TEDx2018/eventsListView.html', context={'events': events, 'eventType': 'Previous'})


def eventView(request, eventName):
	eventName = eventName.replace('_', ' ')
	event = Event.objects.filter(Name=eventName).first()
	teams = getTeamAndTeamMembers(event)
	return render(request=request, template_name='TEDx2018/event.html', context={'event': event, 'teams': teams})


def talksView(request):
	events = Event.objects.order_by('-StartDateTime')
	return render(request=request, template_name='TEDx2018/talks.html', context={'events': events})


def speakersView(request):
	events = Event.objects.order_by('-StartDateTime')
	return render(request=request, template_name='TEDx2018/speakers.html', context={'events': events})


def speakerProfileView(request, fullName):
	name, surname = fullName.split('_')
	speaker = Speaker.objects.filter(Name=name, Surname=surname).first()
	return render(request=request, template_name='TEDx2018/speakerProfile.html', context={'speaker': speaker})


def partnersView(request):
	events = []
	eventstmp = Event.objects.exclude(AnnouncementDateTime__gt=datetime.now().astimezone()).order_by('-StartDateTime')
	for event in eventstmp:
		partnersList = []
		hasPartners = False
		for partnerLevel in event.partnerlevel_set.all().order_by('Level'):
			partners = list(event.partner_set.filter(PartnerLevel=partnerLevel))
			if len(partners):
				partnersList.append({'Name': partnerLevel.Name, 'partners': partners})
				hasPartners = True
		if hasPartners:
			events.append({'Name': event.Name, 'partnerLevels': partnersList})
	return render(request=request, template_name='TEDx2018/partners.html', context={'events': events})


def becomeAPartnerView(request):
	return render(request=request, template_name='TEDx2018/becomeAPartner.html')


def communityView(request):
	return render(request=request, template_name='TEDx2018/community.html')


def joinAsAMemberView(request):
	return render(request=request, template_name='TEDx2018/joinAsAMember.html')


def donorsView(request):
	return render(request=request, template_name='TEDx2018/donors.html')


def becomeADonorView(request):
	return render(request=request, template_name='TEDx2018/becomeADonor.html')


def aboutView(request):
	photos = list(AboutUsCarouselPhoto.objects.all())
	shuffle(photos)
	teams = getTeamAndTeamMembers(Event.objects.order_by('-StartDateTime').first())
	return render(request=request, template_name='TEDx2018/about.html', context={'photos': photos, 'teams': teams})


def teamMemberProfileView(request, fullName):
	name, surname = fullName.split('_')
	teamMember = TeamMember.objects.filter(Name=name, Surname=surname).first()
	return render(request=request, template_name='TEDx2018/teamMemberProfile.html', context={'teamMember': teamMember})


def ourTeamView(request):
	events = Event.objects.order_by('-StartDateTime')
	eventsTmp = []
	for event in events:
		teams = getTeamAndTeamMembers(event)
		eventsTmp.append({'event': event, "teams": teams})
	return render(request=request, template_name='TEDx2018/ourTeam.html', context={'events': eventsTmp})


def contactUsView(request):
	return render(request=request, template_name='TEDx2018/contactUs.html')


def becomeAVolunteerView(request):
	return render(request=request, template_name='TEDx2018/becomeAVolunteer.html')


def faqView(request):
	return render(request=request, template_name='TEDx2018/faq.html')


def custom_404View(request, path):
	return render(request=request, template_name='TEDx2018/404.html', context={'path': path})


def handler404(request):
	return render(request=request, template_name='TEDx2018/404.html')


def custom_500(request):
	return render(request=request, template_name='TEDx2018/500.html')


def googleConfirmation(request):
	return render(request=request, template_name='TEDx2018/google21f2e05779fa0f76.html')


def ticketsCounterView(request):
	return HttpResponse(getTicketsNumber())
