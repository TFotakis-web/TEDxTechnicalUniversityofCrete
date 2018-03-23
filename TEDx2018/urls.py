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
	path('', views.home, name='home'),
	path('events/', views.currentEvent, name='currentEvent'),
	path('events/upcoming/', views.upcomingEvents, name='upcomingEvents'),
	path('events/previous/', views.previousEvents, name='previousEvents'),
	path('events/<str:eventName>/', views.event, name='event'),
	path('talks/', views.talks, name='talks'),
	path('speakers/', views.speakers, name='speakers'),
	path('speakers/<str:fullName>/', views.speakerProfile, name='speakersProfile'),
	path('partners/', views.partners, name='partners'),
	path('partners/becomeAPartner', views.becomeAPartner, name='becomeAPartner'),
	path('community/', views.community, name='community'),
	path('community/joinAsAMember/', views.joinAsAMember, name='joinAsAMember'),
	path('community/donors/', views.donors, name='donors'),
	path('community/donors/becomeADonor/', views.becomeADonor, name='becomeADonor'),
	path('about/', views.about, name='about'),
	path('about/ourTeam/', views.ourTeam, name='ourTeam'),
	path('about/contactUs/', views.contactUs, name='contactUs'),
	path('about/becomeAVolunteer/', views.becomeAVolunteer, name='becomeAVolunteer'),
	path('about/faq/', views.faq, name='faq'),
	path('about/<str:fullName>/', views.teamMemberProfile, name='teamMemberProfile'),
]
