# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
#from modeltranslation.admin import TranslationAdmin

from .models import CheckIn, FeedbackSheet, Meeting, Meetingroom, Member, Organizer, Positioning, Seating

# Register your models here.
admin.site.register(CheckIn)
admin.site.register(FeedbackSheet)
admin.site.register(Meeting)
admin.site.register(Meetingroom)
admin.site.register(Organizer)
admin.site.register(Positioning)
admin.site.register(Seating)
admin.site.register(Member)

	


