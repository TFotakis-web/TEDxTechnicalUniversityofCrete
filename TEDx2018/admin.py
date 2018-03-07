from django.contrib import admin

from .models import *

admin.site.register([Team, Position, TeamMember, TeamMemberAssignment, Speaker, SponsorLevel, Sponsor])
