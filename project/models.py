# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models



class Meeting(models.Model):
    meeting_id = models.IntegerField(db_column='Meeting_id', blank=True, null=True, unique=True)  # Field name made lowercase.
    meeting_name = models.CharField(db_column='Meeting_name', max_length=24, blank=True, null=True)  # Field name made lowercase.
    meetingroom_id = models.CharField(db_column='MeetingRoom_id', max_length=50, blank=True, null=True)  # Field name made lowercase.
    meeting_date = models.DateField(db_column='Meeting_date', blank=True, null=True)  # Field name made lowercase.
    meeting_starttime = models.TimeField(db_column='Meeting_startTime', blank=True, null=True)  # Field name made lowercase.
    meeting_endtime = models.TimeField(db_column='Meeting_endTime', blank=True, null=True)  # Field name made lowercase.
    administrator = models.CharField(db_column='Administrator', max_length=50, blank=True, null=True)  # Field name made lowercase.
    organizer = models.CharField(db_column='Organizer', max_length=24, blank=True, null=True)  # Field name made lowercase.
    speaker = models.CharField(db_column='Speaker', max_length=11, blank=True, null=True)  # Field name made lowercase.
    participants = models.CharField(db_column='Participants', max_length=11, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    fare = models.IntegerField(db_column='Fare', blank=True, null=True)  # Field name made lowercase.
    pictures = models.CharField(db_column='Pictures', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    attendance = models.IntegerField(db_column='Attendance', blank=True, null=True)  # Field name made lowercase.
    savefilm = models.IntegerField(db_column='saveFilm', blank=True, null=True)  # Field name made lowercase.

    def __unicode__(self):
       return 'Meeting : ' + str(self.meeting_id)

    class Meta: 
        managed = False
        db_table = 'Meeting'

class FeedbackSheet(models.Model):
    #meeting_id = models.IntegerField(db_column='Meeting_id', blank=True, null=True)  # Field name made lowercase.
    meeting_id = models.ForeignKey(Meeting, related_name='feedback', to_field='meeting_id',db_column='Meeting_id')
    member_email = models.CharField(db_column='Member_email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    time_feedback = models.IntegerField(db_column='Time_feedback', blank=True, null=True)  # Field name made lowercase.
    location_feedback = models.IntegerField(db_column='Location_feedback', blank=True, null=True)  # Field name made lowercase.
    itinerary_feedback = models.IntegerField(db_column='Itinerary_feedback', blank=True, null=True)  # Field name made lowercase.
    suggestions = models.TextField(db_column='Suggestions', blank=True, null=True)  # Field name made lowercase.

    def __unicode__(self):
        if self.meeting_id is None:
            return 'FeedbackSheet with no meeting_id.'
        else:
            return 'Meeting : ' + str(self.meeting_id) + "'s feedback"
       #return 'Meeting : ' + self.meeting_id + "'s feedback"

    class Meta:
        managed = False
        db_table = 'Feedback_sheet'



class Meetingroom(models.Model):
    room_id = models.CharField(db_column='Room_id', max_length=11, blank=True, null=False, unique=True)  # Field name made lowercase.
    meetingroom_ssid = models.CharField(db_column='MeetingRoom_ssid', max_length=24, blank=True, null=True)  # Field name made lowercase.
    mac_address = models.CharField(db_column='Mac_address', max_length=50, blank=True, null=True)

    def __unicode__(self):
       return 'Room : ' + self.room_id

    class Meta:
        managed = False
        db_table = 'MeetingRoom'


class Member(models.Model):
    member_email = models.CharField(db_column='Member_email', max_length=50, blank=True, null=False, unique=True)  # Field name made lowercase.
    member_password = models.CharField(db_column='Member_password', max_length=50, blank=True, null=True)  # Field name made lowercase.
    member_name = models.CharField(db_column='Member_name', max_length=24, blank=True, null=True)  # Field name made lowercase.
    member_department = models.CharField(db_column='Member_department', max_length=24, blank=True, null=True)  # Field name made lowercase.
    member_phone = models.CharField(db_column='Member_phone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    gender = models.IntegerField(db_column='Gender', blank=True, null=True)  # Field name made lowercase.

    def __unicode__(self):
       if self.member_name is None:
        return 'Position with null member_name.'
       else:
        return 'Member : ' + self.member_name

    class Meta:
        managed = False
        db_table = 'Member'


class Organizer(models.Model):
    organizer_email = models.CharField(db_column='Organizer_email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    organizer_password = models.CharField(db_column='Organizer_password', max_length=50, blank=True, null=True)  # Field name made lowercase.
    organizer_department = models.CharField(db_column='Organizer_department', max_length=24, blank=True, null=True)  # Field name made lowercase.
    organizer_phone = models.CharField(db_column='Organizer_phone', max_length=20, blank=True, null=True)  # Field name made lowercase.

    def __unicode__(self):
       return 'Organizer : ' + self.organizer_email + ". department : " + self.organizer_department
    
    class Meta:
        managed = False
        db_table = 'Organizer'

class CheckIn(models.Model):
    meeting_id = models.IntegerField(db_column='Meeting_id', blank=True, null=True)  # Field name made lowercase.
    meetingroom_id = models.CharField(db_column='MeetingRoom_id', max_length=11, blank=True, null=True)
    #member_email = models.CharField(db_column='Member_email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    member_email = models.ForeignKey(Member, related_name = "checkin", to_field='member_email', db_column = 'Member_email')
    login_time = models.TimeField(db_column='Login_time', blank=True, null=True)  # Field name made lowercase.
    logout_time = models.TimeField(db_column='Logout_time', blank=True, null=True)  # Field name made lowercase.
    seat_id = models.IntegerField(db_column='Seat_id', blank=True, null=True)  # Field name made lowercase.
    meetingroom_id = models.CharField(db_column='MeetingRoom_id', max_length=11, blank=True, null=True)

    def __unicode__(self):
       return 'Meeting : ' + str(self.meeting_id) + "'s checkin"
    
    class Meta:
        managed = False
        db_table = 'Check_in'


class Positioning(models.Model):
    #id = models.IntegerField(primary_key=True)
    meetingroom_id = models.CharField(db_column='MeetingRoom_id', max_length=11, blank=True, null=True)  # Field name made lowercase.
    #member_email = models.CharField(db_column='Member_email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    member_email = models.ForeignKey(Member, related_name="position", to_field='member_email', db_column = 'Member_email')
    current_ssid = models.CharField(db_column='Current_ssid', max_length=24, blank=True, null=True)  # Field name made lowercase.
    wifi_level = models.IntegerField(db_column='Wifi_level', blank=True, null=True)  # Field name made lowercase.
    mac_address = models.CharField(db_column='Mac_address', max_length=50, blank=True, null=True)
    wifi_time = models.DateTimeField(db_column='wifi_time',blank=True, null=True)

    def __unicode__(self):
       return 'Room : ' + str(self.meetingroom_id) + "'s position"

    class Meta:
        managed = False
        db_table = 'Positioning'


class Seating(models.Model):
    #meeingroom_id = models.CharField(db_column='MeeingRoom_id', max_length=11, blank=True, null=True)  # Field name made lowercase.
    room_id = models.ForeignKey(Meetingroom, related_name="seat", to_field='room_id', db_column = 'room_id')
    seat_id = models.IntegerField(db_column='Seat_id', blank=True, null=True)  # Field name made lowercase.
    seat_ssid = models.CharField(db_column='Seat_ssid', max_length=24, blank=True, null=True)  # Field name made lowercase.
    wifi_level = models.IntegerField(db_column='Wifi_level', blank=True, null=True)  # Field name made lowercase.
    mac_address = models.CharField(db_column='Mac_address', max_length=50, blank=True, null=True)

    def __unicode__(self):
       return 'Room : ' + str(self.room_id) + ". Seat : " + str(self.seat_id)
    
    class Meta:
        managed = False
        db_table = 'Seating'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
