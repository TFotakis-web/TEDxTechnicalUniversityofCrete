"""TEDxTechnicalUniversityofCrete URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

urlpatterns = [
	path('', views.homeView, name='home'),
	path('events/', views.currentEventView, name='currentEvent'),
	path('events/upcoming/', views.upcomingEventsView, name='upcomingEvents'),
	path('events/previous/', views.previousEventsView, name='previousEvents'),
	path('events/<str:eventName>/', views.eventView, name='event'),
	path('talks/', views.talksView, name='talks'),
	path('speakers/', views.speakersView, name='speakers'),
	path('speakers/<str:fullName>/', views.speakerProfileView, name='speakerProfile'),
	path('partners/', views.partnersView, name='partners'),
	path('partners/becomeAPartner', views.becomeAPartnerView, name='becomeAPartner'),
	path('community/', views.communityView, name='community'),
	path('community/joinAsAMember/', views.joinAsAMemberView, name='joinAsAMember'),
	path('community/donors/', views.donorsView, name='donors'),
	path('community/donors/becomeADonor/', views.becomeADonorView, name='becomeADonor'),
	path('about/', views.aboutView, name='about'),
	path('about/ourTeam/', views.ourTeamView, name='ourTeam'),
	path('about/contactUs/', views.contactUsView, name='contactUs'),
	path('about/becomeAVolunteer/', views.becomeAVolunteerView, name='becomeAVolunteer'),
	path('about/faq/', views.faqView, name='faq'),
	path('about/<str:fullName>/', views.teamMemberProfileView, name='teamMemberProfile'),
	path('google21f2e05779fa0f76.html', views.googleConfirmation, name='googleConfirmation'),
	path('ticketsCounter/', views.ticketsCounterView, name='ticketsCounter'),
	# path(r'^404/$', views.custom_404, name='custom404'),
]
