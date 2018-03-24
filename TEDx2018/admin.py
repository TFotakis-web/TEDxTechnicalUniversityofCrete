from django.contrib import admin

from .models import *

admin.site.register([Event, Ticket, Team, Position, TeamMember, TeamMemberAssignment, Session, Speaker, PartnerLevel, Partner, AboutUsCarouselPhoto])
