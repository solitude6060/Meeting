
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
        fields = ('meeingroom_id', 'seat_id', 'seat_ssid', 'mac_address', 'wifi_level')


################################################################
#	Organizer, feedback and meetingroom in meeting serializer
################################################################

class MeetingroomSerializer(serializers.ModelSerializer):
    Meetingroom_seat = SeatingSerializer(many=True, read_only=True)
    class Meta:
        model = Meetingroom
        fields = ('room_id', 'meetingroom_ssid','mac_address', 'Meetingroom_seat')

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

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        meeting = Meeting.objects.create(**validated_data)
        return Meeting.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.meeting_id = validated_data.get('meeting_id', instance.meeting_id)
        instance.meeting_name = validated_data.get('meeting_name', instance.meeting_name)
        instance.meetingroom_id = validated_data.get('meetingroom_id', instance.meetingroom_id)
        instance.meeting_date = validated_data.get('meeting_date', instance.meeting_date)
        instance.meeting_starttime = validated_data.get('meeting_starttime', instance.meeting_starttime)
        instance.meeting_endtime = validated_data.get('meeting_endtime', instance.meeting_endtime)
        instance.administrator = validated_data.get('administrator', instance.administrator)
        instance.address = validated_data.get('address', instance.address)
        instance.organizer = validated_data.get('organizer', instance.organizer)
        instance.speaker = validated_data.get('speaker', instance.speaker)
        instance.participants = validated_data.get('participants', instance.participants)
        instance.content = validated_data.get('content', instance.content)
        instance.fare = validated_data.get('fare', instance.fare)
        instance.attendance = validated_data.get('attendance', instance.attendance)
        instance.savefilm = validated_data.get('savefilm', instance.savefilm)
        instance.save()
        return instance

#########################################################
#	Checkin and position in member's serializer
#########################################################

class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = ('member_email','meeting_id', 'login_time', 'logout_time', 'seat_id')
	
	def create(self, validated_data):
		checkin_object = CheckIn.objects.create(**validated_data)
		return checkin_object

class PositioningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positioning
        fields = ('member_email','meetingroom_id', 'current_ssid', 'mac_address', 'wifi_level')
	
	def create(self, validated_data):
		position_object = Positioning.objects.create(**validated_data)
		return position_object

class MemberSerializer(serializers.ModelSerializer):
    position = PositioningSerializer(many = True)
    checkin = CheckInSerializer(many = True)

    class Meta:
        model = Member
    	fields = ('member_email','member_password','member_name','position','checkin','member_department', 'member_phone', 'gender')

    def create(self, validated_data):
        position_data = validated_data.pop('position')
        checkin_data = validated_data.pop("checkin")
        member = Member.objects.create(**validated_data)
        #member = Member.objects.create(position=position_data,checkin=checkin_data,**validated_data)

        # for position_data in position_data:
        #     Positioning.objects.create(**position_data)
        # for checkin_data in checkin_data:
        #     CheckIn.objects.create(**checkin_data)
        return member
        #return Member.objects.create(**validated_data)
	
	def update(self, instance, validated_data):
	        
	        #Update and return an existing `Snippet` instance, given the validated data.
	        
	        instance.member_email = validated_data.get('member_email', instance.member_email)
	        instance.member_password = validated_data.get('member_password', instance.member_password)
	        instance.member_name = validated_data.get('member_name', instance.member_name)
	        instance.member_department = validated_data.get('member_department', instance.member_department)
	        instance.member_phone = validated_data.get('member_phone', instance.member_phone)
	        instance.gender = validated_data.get('gender', instance.gender)
	        instance.save()
	        return instance

    



