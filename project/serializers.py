
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import CheckIn, FeedbackSheet, Meeting, Meetingroom, Member, Organizer, Positioning, Seating


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


################################################################
#	Seating in meetingroom serializer
################################################################


class SeatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seating
        fields = ('meeingroom_id', 'seat_id', 'seat_ssid', 'wifi_level')


################################################################
#	Organizer, feedback and meetingroom in meeting serializer
################################################################

class MeetingroomSerializer(serializers.ModelSerializer):
    Meetingroom_seat = SeatingSerializer(many=True, read_only=True)
    class Meta:
        model = Meetingroom
        fields = ('room_id', 'meetingroom_ssid','Meetingroom_seat')

class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        fields = ('organizer_email', 'organizer_password', 'organizer_department', 'organizer_phone')

class FeedbackSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackSheet
        fields = ('meeting_id', 'member_email','time_feedback', 'location_feedback', 'itinerary_feedback', 'suggestions')

class MeetingSerializer(serializers.ModelSerializer):
    Meeting_meetingroom = MeetingroomSerializer(many=True, read_only=True)
    Meeting_organizer = OrganizerSerializer(many=True, read_only=True)
    Meeting_feedbackSheet = FeedbackSheetSerializer(many=True, read_only=True)

    class Meta:
        model = Meeting
        fields = ('meeting_id', 'meeting_name','meetingroom_id', 'meeting_date', 'meeting_starttime', 'meeting_endtime', 'administrator', 'organizer', 'speaker', 'participants', 'content', 'fare', 'pictures', 'address', 'attendance', 'savefilm', 'Meeting_meetingroom', 'Meeting_feedbackSheet', 'Meeting_organizer')


#########################################################
#	Checkin and position in member's serializer
#########################################################

class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = ('meeting_id', 'member_email','login_time', 'logout_time', 'seat_id')


class PositioningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positioning
        fields = ('meetingroom_id', 'member_email', 'current_ssid', 'wifi_level')
		
class MemberSerializer(serializers.ModelSerializer):
    Member_positioning = PositioningSerializer(many=True, read_only=True)
    Member_checkin = CheckInSerializer(many=True, read_only=True)

    class Meta:
        model = Member
        fields = ('member_password', 'member_email','member_name', 'member_department', 'member_phone', 'gender', 'Member_positioning', 'Member_checkin')




