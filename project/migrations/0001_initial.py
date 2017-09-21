# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=80)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(null=True, blank=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(unique=True, max_length=150)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CheckIn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meeting_id', models.IntegerField(null=True, db_column='Meeting_id', blank=True)),
                ('login_time', models.TimeField(null=True, db_column='Login_time', blank=True)),
                ('logout_time', models.TimeField(null=True, db_column='Logout_time', blank=True)),
                ('seat_id', models.IntegerField(null=True, db_column='Seat_id', blank=True)),
            ],
            options={
                'db_table': 'Check_in',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(null=True, blank=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FeedbackSheet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meeting_id', models.IntegerField(null=True, db_column='Meeting_id', blank=True)),
                ('member_email', models.CharField(max_length=50, null=True, db_column='Member_email', blank=True)),
                ('time_feedback', models.IntegerField(null=True, db_column='Time_feedback', blank=True)),
                ('location_feedback', models.IntegerField(null=True, db_column='Location_feedback', blank=True)),
                ('itinerary_feedback', models.IntegerField(null=True, db_column='Itinerary_feedback', blank=True)),
                ('suggestions', models.TextField(null=True, db_column='Suggestions', blank=True)),
            ],
            options={
                'db_table': 'Feedback_sheet',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meeting_id', models.IntegerField(null=True, db_column='Meeting_id', blank=True)),
                ('meeting_name', models.CharField(max_length=24, null=True, db_column='Meeting_name', blank=True)),
                ('meetingroom_id', models.IntegerField(null=True, db_column='MeetingRoom_id', blank=True)),
                ('meeting_date', models.DateField(null=True, db_column='Meeting_date', blank=True)),
                ('meeting_starttime', models.TimeField(null=True, db_column='Meeting_startTime', blank=True)),
                ('meeting_endtime', models.TimeField(null=True, db_column='Meeting_endTime', blank=True)),
                ('administrator', models.CharField(max_length=50, null=True, db_column='Administrator', blank=True)),
                ('organizer', models.CharField(max_length=24, null=True, db_column='Organizer', blank=True)),
                ('speaker', models.CharField(max_length=11, null=True, db_column='Speaker', blank=True)),
                ('participants', models.CharField(max_length=11, null=True, db_column='Participants', blank=True)),
                ('content', models.TextField(null=True, db_column='Content', blank=True)),
                ('fare', models.IntegerField(null=True, db_column='Fare', blank=True)),
                ('pictures', models.CharField(max_length=100, null=True, db_column='Pictures', blank=True)),
                ('address', models.CharField(max_length=100, null=True, db_column='Address', blank=True)),
                ('attendance', models.IntegerField(null=True, db_column='Attendance', blank=True)),
                ('savefilm', models.IntegerField(null=True, db_column='saveFilm', blank=True)),
            ],
            options={
                'db_table': 'Meeting',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Meetingroom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room_id', models.CharField(max_length=11, null=True, db_column='Room_id', blank=True)),
                ('meetingroom_ssid', models.CharField(max_length=24, null=True, db_column='MeetingRoom_ssid', blank=True)),
            ],
            options={
                'db_table': 'MeetingRoom',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('member_email', models.CharField(unique=True, max_length=50, db_column='Member_email', blank=True)),
                ('member_password', models.CharField(max_length=50, null=True, db_column='Member_password', blank=True)),
                ('member_name', models.CharField(max_length=24, null=True, db_column='Member_name', blank=True)),
                ('member_department', models.CharField(max_length=24, null=True, db_column='Member_department', blank=True)),
                ('member_phone', models.CharField(max_length=20, null=True, db_column='Member_phone', blank=True)),
                ('gender', models.IntegerField(null=True, db_column='Gender', blank=True)),
            ],
            options={
                'db_table': 'Member',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organizer_email', models.CharField(max_length=50, null=True, db_column='Organizer_email', blank=True)),
                ('organizer_password', models.IntegerField(null=True, db_column='Organizer_password', blank=True)),
                ('organizer_department', models.CharField(max_length=24, null=True, db_column='Organizer_department', blank=True)),
                ('organizer_phone', models.CharField(max_length=20, null=True, db_column='Organizer_phone', blank=True)),
            ],
            options={
                'db_table': 'Organizer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Positioning',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meetingroom_id', models.IntegerField(null=True, db_column='MeetingRoom_id', blank=True)),
                ('current_ssid', models.CharField(max_length=24, null=True, db_column='Current_ssid', blank=True)),
                ('wifi_level', models.IntegerField(null=True, db_column='Wifi_level', blank=True)),
            ],
            options={
                'db_table': 'Positioning',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Seating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meeingroom_id', models.CharField(max_length=11, null=True, db_column='MeeingRoom_id', blank=True)),
                ('seat_id', models.IntegerField(null=True, db_column='Seat_id', blank=True)),
                ('seat_ssid', models.IntegerField(null=True, db_column='Seat_ssid', blank=True)),
                ('wifi_level', models.IntegerField(null=True, db_column='Wifi_level', blank=True)),
            ],
            options={
                'db_table': 'Seating',
                'managed': False,
            },
        ),
    ]
