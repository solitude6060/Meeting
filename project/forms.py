from django import forms
from .models import CheckIn, FeedbackSheet, Meeting, Meetingroom, Member, Organizer, Positioning, Seating
from .models import AuthUser


class userForm(forms.ModelForm):
	class Meta:
		model = AuthUser
		fields = ['username','password','email']

class CheckInForm(forms.ModelForm):
	class Meta:
		model = CheckIn
		fields = ['member_email','meeting_id', 'login_time', 'logout_time', 'seat_xid', 'seat_yid']

class FeedbackSheetForm(forms.ModelForm):
	class Meta:
		model = FeedbackSheet
		fields = ['meeting_id', 'member_email','time_feedback', 'location_feedback', 'itinerary_feedback', 'suggestions']

class MeetingForm(forms.ModelForm):
	class Meta:
		model = Meeting
		fields = ['meeting_id', 'meeting_name','meetingroom_id', 'meeting_date', 'meeting_starttime', 'meeting_endtime', 'administrator', 'organizer', 'speaker', 'participants', 'content', 'fare', 'pictures', 'address', 'attendance', 'savefilm']

class MeetingroomForm(forms.ModelForm):
	class Meta:
		model = Meetingroom
		fields = ['room_id', 'meetingroom_ssid','mac_address']
		
class MemberForm(forms.ModelForm):
	class Meta:
		model = Member
		fields = ['member_email','member_password','member_name','member_department', 'member_phone', 'gender']

class OrganizerForm(forms.ModelForm):
	class Meta:
		model = Organizer
		fields = ['organizer_email', 'organizer_password', 'organizer_department', 'organizer_phone']

class PositioningForm(forms.ModelForm):
	class Meta:
		model = Positioning
		fields = ['member_email','meetingroom_id', 'current_ssid', 'mac_address', 'wifi_level']

class SeatingForm(forms.ModelForm):
	class Meta:
		model = Seating
		fields = ['seat_xid', 'seat_yid', 'seat_ssid', 'mac_address', 'wifi_level','room_id']


