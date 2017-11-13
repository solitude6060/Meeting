#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse

from rest_framework import viewsets, generics
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import mixins
from rest_framework import generics

from .serializers import CheckInSerializer, FeedbackSheetSerializer, MeetingSerializer, MeetingroomSerializer, MemberSerializer, OrganizerSerializer, PositioningSerializer, SeatingSerializer
from .models import CheckIn, FeedbackSheet, Meeting, Meetingroom, Member, Organizer, Positioning, Seating
from .forms import CheckInForm, FeedbackSheetForm, MeetingForm, MeetingroomForm, MemberForm, OrganizerForm, PositioningForm, SeatingForm

from .serializers import AuthUserSerializer
from .models import AuthUser
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.models import User


from datetime import datetime
import datetime
#################################################################
#restful api's view
#################################################################
class UserViewSet(viewsets.ModelViewSet):
    """
    List all snippets, or create a new snippet.
    """
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserSerializer
    pagination_class = None

class MeetingViewSet(viewsets.ModelViewSet):
    """
    List all snippets, or create a new snippet.
    """
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    pagination_class = None


class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    pagination_class = None

class MeetingRoomViewSet(viewsets.ModelViewSet):

    queryset = Meetingroom.objects.all()
    serializer_class = MeetingroomSerializer
    pagination_class = None
 

@api_view(['GET', 'PUT'])
def MemberDetail(request,pk):
    #List all code snippets, or create a new snippet.
    try:
        member = Member.objects.filter(member_email=pk)
        mem = Member.objects.get(member_email=pk)
    except Member.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        #m = Member.objects.filter(member_email=pk)

    if request.method == 'GET':
        #queryset = Member.objects.all()
        serializer = MemberSerializer(member, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MemberSerializer(data=data)
        if serializer.is_valid():
            serializer.update(mem, data)
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
            #return JsonResponse(serializer.data, status=201)
        #return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'POST'])
def MemberList(request):
    #List all code snippets, or create a new snippet.
    
    if request.method == 'GET':
        queryset = Member.objects.all()
        serializer = MemberSerializer()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def MeetingList(request):
    #List all code snippets, or create a new snippet.
    if request.method == 'GET':
        queryset = Meeting.objects.all()
        #serializer_class = MemberSerializer
        serializer = MeetingSerializer()
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MeetingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def PositionList(request):
    #List all code snippets, or create a new snippet.
    if request.method == 'GET':
        queryset = Positioning.objects.all()
        serializer = PositioningSerializer()
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PositioningSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'PUT'])
def PositionDetail(request,pk,mac):
    #List all code snippets, or create a new snippet.
    try:
        position_obj = Positioning.objects.filter(member_email=pk)
        #member = Member.objects.only('member_email').get(member_email=pk)
        #mem = Member.objects.get(member_email=pk)
        mac_ad = Positioning.objects.filter(mac_address=mac,member_email=pk) 
    
    except Positioning.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PositioningSerializer(position_obj, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PositioningSerializer(data=data)
        if serializer.is_valid():

            mac_ad.delete()
            serializer.save()
            #serializer.update(pos_id, data)

            ser_filter = PositioningSerializer(mac_ad, many=True)
            #return Response(ser_filter.data, status=200)
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def CheckinList(request):
    #List all code snippets, or create a new snippet.
    if request.method == 'GET':
        queryset = CheckIn.objects.all()
        serializer = CheckInSerializer()
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CheckInSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'PUT'])
def CheckinDetail(request,member,meeting):
    #List all code snippets, or create a new snippet.
    try:
        checkin_obj = CheckIn.objects.filter(member_email=member)
        check = CheckIn.objects.filter(meeting_id=meeting,member_email=member) 
    
    except CheckIn.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CheckInSerializer(checkin_obj, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CheckInSerializer(data=data)
        if serializer.is_valid():

            check.delete()
            serializer.save()

            ser_filter = CheckInSerializer(check, many=True)
            #return Response(ser_filter.data, status=201)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def FeedbackList(request):
    #List all code snippets, or create a new snippet.
    if request.method == 'GET':
        queryset = FeedbackSheet.objects.all()
        serializer = FeedbackSheetSerializer()
        #return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FeedbackSheetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT'])
def FeedbackDetail(request,member,meeting):
    #List all code snippets, or create a new snippet.
    try:
        feedback_obj = FeedbackSheet.objects.filter(member_email=member)
        feedback = FeedbackSheet.objects.filter(meeting_id=meeting,member_email=member) 
    
    except FeedbackSheet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FeedbackSheetSerializer(feedback_obj, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FeedbackSheetSerializer(data=data)
        if serializer.is_valid():

            feedback.delete()
            serializer.save()

            ser_filter = FeedbackSheetSerializer(feedback, many=True)
            #return Response(ser_filter.data)
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)


#################################################################
#   web app's view
#################################################################
def index(request):
    meeting = Meeting.objects.all()
    meeting = sorted(meeting ,key=lambda x: datetime.datetime.strptime(str(x.meeting_date), '%Y-%m-%d'), reverse=True)
    me = meeting[0:4]
    return render_to_response('project/index.html', locals())

def admin_loging(request):
    #error = False
    if request.user.is_authenticated(): 
        meeting = Meeting.objects.all()
        meeting = sorted(meeting ,key=lambda x: datetime.datetime.strptime(str(x.meeting_date), '%Y-%m-%d'), reverse=True)
        me = meeting[0:4]
        return render(request, 'project/index.html', locals())

    #error = False
    uname = request.POST.get('user')
    pword = request.POST.get('pword')

    user = authenticate(username=uname, password=pword)
    
    if user is not None:
        auth.login(request, user)
        meeting = Meeting.objects.all()
        meeting = sorted(meeting ,key=lambda x: datetime.datetime.strptime(str(x.meeting_date), '%Y-%m-%d'), reverse=True)
        me = meeting[0:4]
        #return render_to_response('project/index.html', locals())
        return render(request, 'project/index.html', locals())
    else:
        #error = True
        return render(request, 'project/admin_loging.html', locals())
    #error = False
    return render(request, 'project/admin_loging.html', locals())

def about(request):
    return render_to_response('project/about.html', locals())

def login(request):
    if request.user.is_authenticated(): 
        meeting = Meeting.objects.all()
        meeting = sorted(meeting ,key=lambda x: datetime.datetime.strptime(str(x.meeting_date), '%Y-%m-%d'), reverse=True)
        me = meeting[0:4]
        return render_to_response('project/index.html', locals())

    if 'login' in request.POST:
        uname = request.POST.get('username')
        pword = request.POST.get('password')    

        user = authenticate(username=uname, password=pword) 

        if user is not None:
            auth.login(request, user)
            meeting = Meeting.objects.all()
            meeting = sorted(meeting ,key=lambda x: datetime.datetime.strptime(str(x.meeting_date), '%Y-%m-%d'), reverse=True)
            me = meeting[0:4]
            return render_to_response('project/index.html', locals())
            #return render(request, 'project/index.html', locals())
        else:
            error = "user None"
            register_checked = ""
            return render(request, 'project/login.html', locals())
            #return render(request, 'project/login.html', locals())
    if 'register' in request.POST:
        
        username = request.POST.get('signUp-userName')
        password = request.POST.get('signUp-password')

        #already have account
        error1 = False
        #none username or password
        error2 = False

        #already have account
        if AuthUser.objects.filter(username=username):
            error1 = True

        #none username or password
        if not username or not password :
            error2 = True

        if not error1 and not error2 :
            u = User(username=username,password=password)
            u.set_password(password)
            u.save()
            user = authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                meeting = Meeting.objects.all()
                meeting = sorted(meeting ,key=lambda x: datetime.datetime.strptime(str(x.meeting_date), '%Y-%m-%d'), reverse=True)
                me = meeting[0:4]
                return render_to_response('project/index.html', locals())

        else:
            register_checked = "checked='false'"
            return render_to_response('project/login.html', locals())

    register_checked = ""
    return render(request, 'project/login.html', {})


def information(request):
    return render_to_response('project/information.html', locals())

def upload(request):
    if request.method == "GET":
        return render(request, 'project/upload.html', {})
    if request.method == "POST":
        mform = MeetingForm(request.POST)
        
        meeting = Meeting.objects.all()
        meeting = sorted(meeting, key=lambda x:x.meeting_id, reverse=True)
        meeting_id = meeting[0].meeting_id
        meeting_id += 1

        administrator = request.user.username
        meeting_name = mform.data.get('meetingName')
        address = mform.data.get('meetingPlace')
        meetingroom_id = mform.data.get('meetingroom')
        organizer = mform.data.get('Organizer')
        speaker = mform.data.get('Speaker')
        participants = mform.data.get('participants')
        attendance = mform.data.get('attendance')
        fare = mform.data.get('fare')
        content = mform.data.get('content')

        meeting_Date = mform.data.get('Date')
        # meeting_edDate = mform.data.get('EDate')
        meeting_Stime = mform.data.get('STime')
        meeting_Etime = mform.data.get('ETime')

        meetingfiliter = Meeting.objects.filter(meeting_name=meeting_name, meetingroom_id=meetingroom_id, administrator=administrator, meeting_date=meeting_Date, meeting_id=meeting_id)

        if meetingfiliter : 
            meeting = Meeting.objects.all()
            meeting = sorted(meeting ,key=lambda x: datetime.datetime.strptime(str(x.meeting_date), '%Y-%m-%d'), reverse=True)
            me = meeting[0:4]
            #return render(request, 'project/index.html', locals())
            return render_to_response('project/index.html', locals())
        else:
            meCreate = Meeting.objects.create(meeting_name=meeting_name, meetingroom_id=meetingroom_id, administrator=administrator
                , meeting_date=meeting_Date, address=address, meeting_starttime=meeting_Stime, meeting_endtime=meeting_Etime
                , fare=fare, content=content, participants=participants, attendance=attendance
                , meeting_id=meeting_id, speaker=speaker, organizer=organizer, pictures="", savefilm=0)
            meCreate.save()
            meeting = Meeting.objects.all()
            meeting = sorted(meeting ,key=lambda x: datetime.datetime.strptime(str(x.meeting_date), '%Y-%m-%d'), reverse=True)
            me = meeting[0:4]
            #return render(request, 'project/index.html', {})
            return render_to_response('project/index.html', locals())

    return render(request, 'project/index.html', {})

def logout(request):
    auth.logout(request)
    meeting = Meeting.objects.all()
    meeting = sorted(meeting ,key=lambda x: datetime.datetime.strptime(str(x.meeting_date), '%Y-%m-%d'), reverse=True)
    me = meeting[0:4]
    return render(request, 'project/index.html', locals())
    #return render_to_response('project/login.html', locals())

def join(request,meetingId):
    if request.user.is_authenticated():
        username = request.user.username
        check = CheckIn.objects.filter(meeting_id=meetingId, member_email=username)
        meetingObj = Meeting.objects.get(meeting_id=meetingId)
        roomId = meetingObj.meetingroom_id
        #memId = Member.objects.get(member_email=username).member_email
        if check:
            meeting = Meeting.objects.all()
            meeting = sorted(meeting ,key=lambda x: datetime.datetime.strptime(str(x.meeting_date), '%Y-%m-%d'), reverse=True)
            me = meeting[0:4]
            return render(request, 'project/index.html', locals())
        else:
            checkObj = CheckIn.objects.create(meeting_id=meetingId, member_email_id=username, login_time=None, logout_time=None, meetingroom_id=roomId, seat_id=777)
            checkObj.save()
    
    return render_to_response('myapp/challenge.html',locals())



	



