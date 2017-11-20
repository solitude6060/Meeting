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


#from datetime import datetime
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

class OrganizerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer
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

@api_view(['GET', 'POST'])
def SeatingList(request):
    #List all code snippets, or create a new snippet.
    if request.method == 'GET':
        queryset = Seating.objects.all()
        serializer = SeatingSerializer()
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SeatingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'PUT'])
def SeatingDetail(request,id,mac,x,y):
    #List all code snippets, or create a new snippet.
    try:
        seating = Seating.objects.filter(room_id=id, mac_address=mac, seat_xid=x, seat_yid=y)
        seat = Seating.objects.filter(room_id=id, mac_address=mac, seat_xid=x, seat_yid=y)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
        #m = Member.objects.filter(member_email=pk)

    if request.method == 'GET':
        #queryset = Member.objects.all()
        serializer = SeatingSerializer(seating, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SeatingSerializer(data=data)
        if serializer.is_valid():
            seat.delete()
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
            #return JsonResponse(serializer.data, status=201)
        #return JsonResponse(serializer.errors, status=400)


#################################################################
#   web app's view
#################################################################
def index(request):
    curtime = datetime.datetime.strptime((datetime.datetime.now()-datetime.timedelta(days=1)).isoformat(), '%Y-%m-%dT%H:%M:%S.%f').strftime('%Y-%m-%d')
    meetingObj = Meeting.objects.filter(meeting_date__gt = curtime)
    meeting = sorted(meetingObj, key=lambda x: datetime.datetime.strptime(str(x.meeting_date), '%Y-%m-%d'))
    me = meeting[0:4]
    #return render_to_response('project/index.html', locals())
    return render(request, 'project/index.html', locals())

def admin_loging(request):
    #error = False
    if request.user.is_authenticated(): 
        curtime = datetime.datetime.strptime((datetime.datetime.now()-datetime.timedelta(days=1)).isoformat(), '%Y-%m-%dT%H:%M:%S.%f').strftime('%Y-%m-%d')
        meetingObj = Meeting.objects.filter(meeting_date__gt = curtime)
        meeting = sorted(meetingObj, key=lambda x: datetime.datetime.strptime(str(x.meeting_date), '%Y-%m-%d'))
        me = meeting[0:4]
        return render(request, 'project/index.html', locals())
        #return render_to_response('project/index.html', locals())

    #error = False
    uname = request.POST.get('user')
    pword = request.POST.get('pword')

    user = authenticate(username=uname, password=pword)
    
    if user is not None:
        auth.login(request, user)
        curtime = datetime.datetime.strptime((datetime.datetime.now()-datetime.timedelta(days=1)).isoformat(), '%Y-%m-%dT%H:%M:%S.%f').strftime('%Y-%m-%d')
        meetingObj = Meeting.objects.filter(meeting_date__gt = curtime)
        meeting = sorted(meetingObj, key=lambda x: datetime.datetime.strptime(str(x.meeting_date), '%Y-%m-%d'))
        me = meeting[0:4]
        # username = request.user.username
        # oger = Organizer.objects.get(organizer_email=username)
        # name = oger.organizer_department
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
    if request.user.is_authenticated() and not request.user.is_staff:
        # username = request.user.username
        # member = Member.objects.get(member_email=username)
        # name = member.member_name 
        curtime = datetime.datetime.strptime((datetime.datetime.now()-datetime.timedelta(days=1)).isoformat(), '%Y-%m-%dT%H:%M:%S.%f').strftime('%Y-%m-%d')
        meetingObj = Meeting.objects.filter(meeting_date__gt = curtime)
        meeting = sorted(meetingObj, key=lambda x: datetime.datetime.strptime(str(x.meeting_date), '%Y-%m-%d'))
        me = meeting[0:4]
        return render_to_response('project/index.html', locals())

    if 'login' in request.POST :
        uname = request.POST.get('username')
        pword = request.POST.get('password')    

        user = authenticate(username=uname, password=pword) 

        if user is not None and not user.is_staff:
            # if not request.user.is_staff:
            #     member = Member.objects.get(member_email=uname)
            #     name = member.member_name
            # else:
            #     oger = Organizer.objects.get(organizer_email=uname)
            #     name = oger.organizer_department
            auth.login(request, user)
            curtime = datetime.datetime.strptime((datetime.datetime.now()-datetime.timedelta(days=1)).isoformat(), '%Y-%m-%dT%H:%M:%S.%f').strftime('%Y-%m-%d')
            meetingObj = Meeting.objects.filter(meeting_date__gt = curtime)
            meeting = sorted(meetingObj, key=lambda x: datetime.datetime.strptime(str(x.meeting_date), '%Y-%m-%d'))
            me = meeting[0:4]
            return render_to_response('project/index.html', locals())
            #return render(request, 'project/index.html', locals())
        else:
            error = "user None"
            register_checked = ""
            if user.is_staff:
                error3 = True
            #return render(request, 'project/login.html', locals())
            return render_to_response('project/login.html', locals())
    if 'register' in request.POST:
        
        username = request.POST.get('signUp-userName')
        password = request.POST.get('signUp-password')
        phone = request.POST.get('phone')
        realName = request.POST.get('realName')
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
            member = Member.objects.create(member_email=username, member_password=password, member_phone=phone, member_name=realName, member_department="尚未設定")
            member.save()
            user = authenticate(username=username, password=password)

            if user is not None:
                # if not request.user.is_staff:
                #     username = request.user.username
                #     member = Member.objects.get(member_email=username)
                #     name = member.member_name
                # else:
                #     username = request.user.username
                #     oger = Organizer.objects.get(organizer_email=username)
                #     name = oger.organizer_department
                auth.login(request, user)
                curtime = datetime.datetime.strptime((datetime.datetime.now()-datetime.timedelta(days=1)).isoformat(), '%Y-%m-%dT%H:%M:%S.%f').strftime('%Y-%m-%d')
                meetingObj = Meeting.objects.filter(meeting_date__gt = curtime)
                meeting = sorted(meetingObj, key=lambda x: datetime.datetime.strptime(str(x.meeting_date), '%Y-%m-%d'))
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
            curtime = datetime.datetime.strptime((datetime.datetime.now()-datetime.timedelta(days=1)).isoformat(), '%Y-%m-%dT%H:%M:%S.%f').strftime('%Y-%m-%d')
            meetingObj = Meeting.objects.filter(meeting_date__gt = curtime)
            meeting = sorted(meetingObj, key=lambda x: datetime.datetime.strptime(str(x.meeting_date), '%Y-%m-%d'))
            me = meeting[0:4]
            #return render(request, 'project/index.html', locals())
            return render_to_response('project/index.html', locals())
        else:
            meCreate = Meeting.objects.create(meeting_name=meeting_name, meetingroom_id=meetingroom_id, administrator=administrator
                , meeting_date=meeting_Date, address=address, meeting_starttime=meeting_Stime, meeting_endtime=meeting_Etime
                , fare=fare, content=content, participants=participants, attendance=attendance
                , meeting_id=meeting_id, speaker=speaker, organizer=organizer, pictures="", savefilm=0)
            meCreate.save()
            curtime = datetime.datetime.strptime((datetime.datetime.now()-datetime.timedelta(days=1)).isoformat(), '%Y-%m-%dT%H:%M:%S.%f').strftime('%Y-%m-%d')
            meetingObj = Meeting.objects.filter(meeting_date__gt = curtime)
            meeting = sorted(meetingObj, key=lambda x: datetime.datetime.strptime(str(x.meeting_date), '%Y-%m-%d'))
            me = meeting[0:4]
            #return render(request, 'project/index.html', {})
            return render_to_response('project/index.html', locals())

    return render(request, 'project/index.html', {})

def logout(request):
    auth.logout(request)
    curtime = datetime.datetime.strptime((datetime.datetime.now()-datetime.timedelta(days=1)).isoformat(), '%Y-%m-%dT%H:%M:%S.%f').strftime('%Y-%m-%d')
    meetingObj = Meeting.objects.filter(meeting_date__gt = curtime)
    meeting = sorted(meetingObj, key=lambda x: datetime.datetime.strptime(str(x.meeting_date), '%Y-%m-%d'))
    me = meeting[0:4]
    #return render(request, 'project/index.html', locals())
    return render_to_response('project/login.html', locals())

def join(request,meetingId):
    if request.user.is_authenticated() and not request.user.is_staff:
        username = request.user.username
        check = CheckIn.objects.filter(meeting_id=meetingId, member_email=username)
        meetingObj = Meeting.objects.get(meeting_id=meetingId)
        roomId = meetingObj.meetingroom_id
        #memId = Member.objects.get(member_email=username).member_email
        if check:
            curtime = datetime.datetime.strptime((datetime.datetime.now()-datetime.timedelta(days=1)).isoformat(), '%Y-%m-%dT%H:%M:%S.%f').strftime('%Y-%m-%d')
            meetingObj = Meeting.objects.filter(meeting_date__gt = curtime)
            meeting = sorted(meetingObj, key=lambda x: datetime.datetime.strptime(str(x.meeting_date), '%Y-%m-%d'))
            me = meeting[0:4]
            return render_to_response('project/personalpage.html',locals())
        else:
            checkObj = CheckIn.objects.create(meeting_id=meetingId, member_email_id=username, login_time=None, logout_time=None, meetingroom_id=roomId, seat_xid=0, seat_yid=0)
            checkObj.save()
    
    curtime = datetime.datetime.strptime((datetime.datetime.now()-datetime.timedelta(days=1)).isoformat(), '%Y-%m-%dT%H:%M:%S.%f').strftime('%Y-%m-%d')
    meetingObj = Meeting.objects.filter(meeting_date__gt = curtime)
    meeting = sorted(meetingObj, key=lambda x: datetime.datetime.strptime(str(x.meeting_date), '%Y-%m-%d'))
    me = meeting[0:4]
    # if not request.user.is_staff:
    #     username = request.user.username
    #     member = Member.objects.get(member_email=username)
    #     name = member.member_name
    # else:
    #     username = request.user.username
    #     oger = Organizer.objects.get(organizer_email=username)
    #     name = oger.organizer_department
    curtime = datetime.datetime.strptime((datetime.datetime.now()-datetime.timedelta(days=1)).isoformat(), '%Y-%m-%dT%H:%M:%S.%f').strftime('%Y-%m-%d')
    meetingObj = Meeting.objects.filter(meeting_date__gt = curtime)
    meeting_after = meetingObj.values('meeting_id')
    checkObj = CheckIn.objects.filter(member_email=username, meeting_id__in=meeting_after)
    chMeeting = checkObj.values('meeting_id')
    meObjAF = Meeting.objects.filter(meeting_id__in=chMeeting)

    ctime = datetime.datetime.strptime(datetime.datetime.now().isoformat(), '%Y-%m-%dT%H:%M:%S.%f').strftime('%Y-%m-%d')
    me = Meeting.objects.filter(meeting_date__lt = ctime)
    meeting_before = me.values('meeting_id')
    ch = CheckIn.objects.filter(member_email=username, meeting_id__in=meeting_before)
    chMe = ch.values('meeting_id')
    meObjBF = Meeting.objects.filter(meeting_id__in=chMe)

    name = member.member_name
    email = member.member_email
    department = member.member_department
    phone = member.member_phone
    return render_to_response('project/personalpage.html',locals())


def personalpage(request):
    if request.user.is_authenticated():
        username = request.user.username
        mem = Member.objects.get(member_email=username)
        member = Member.objects.get(member_email=username)

        if mem:
            curtime = datetime.datetime.strptime((datetime.datetime.now()-datetime.timedelta(days=1)).isoformat(), '%Y-%m-%dT%H:%M:%S.%f').strftime('%Y-%m-%d')
            meetingObj = Meeting.objects.filter(meeting_date__gt = curtime)
            meeting_after = meetingObj.values('meeting_id')
            checkObj = CheckIn.objects.filter(member_email=username, meeting_id__in=meeting_after)
            chMeeting = checkObj.values('meeting_id')
            meObjAF = Meeting.objects.filter(meeting_id__in=chMeeting)

            ctime = datetime.datetime.strptime(datetime.datetime.now().isoformat(), '%Y-%m-%dT%H:%M:%S.%f').strftime('%Y-%m-%d')
            me = Meeting.objects.filter(meeting_date__lt = ctime)
            meeting_before = me.values('meeting_id')
            ch = CheckIn.objects.filter(member_email=username, meeting_id__in=meeting_before)
            chMe = ch.values('meeting_id')
            meObjBF = Meeting.objects.filter(meeting_id__in=chMe)

            name = member.member_name
            email = member.member_email
            department = member.member_department
            phone = member.member_phone
            return render_to_response('project/personalpage.html', locals())
        else:
            name = email = department = phone = "資料錯誤！"

    return render_to_response('project/personalpage.html', locals())		
	
def admin_page(request):
    if request.user.is_authenticated() and request.user.is_staff:
        username = request.user.username
        orger = Organizer.objects.filter(organizer_email=username)
        org = Organizer.objects.get(organizer_email=username)

        if orger:
            curtime = datetime.datetime.strptime((datetime.datetime.now()-datetime.timedelta(days=1)).isoformat(), '%Y-%m-%dT%H:%M:%S.%f').strftime('%Y-%m-%d')
            meAf = Meeting.objects.filter(meeting_date__gt = curtime, administrator=username)

            ctime = datetime.datetime.strptime(datetime.datetime.now().isoformat(), '%Y-%m-%dT%H:%M:%S.%f').strftime('%Y-%m-%d')
            meBf = Meeting.objects.filter(meeting_date__lt = ctime, administrator=username)

            name = org.organizer_department
            email = org.organizer_email
            phone = org.organizer_phone
            return render_to_response('project/admin_homepage.html', locals())
        else:
            name = email = phone = "資料錯誤！"
    return render_to_response('project/admin_homepage.html', locals())	
	
def choose(request):
    return render_to_response('project/choose.html', locals())

def meeting(request):
    if request.user.is_authenticated():
        x_r = range(2)
        y_r = range(5)
        Matrix = [[0 for y in range(5)] for x in range(2)]
        for xx in x_r:
            for yy in y_r:
                Matrix[xx][yy] = CheckIn.objects.filter(meeting_id=11, seat_xid=xx+1, seat_yid=yy+1)
        return render_to_response('project/meeting.html', locals())
    return render_to_response('project/meeting.html', locals())	
	
def meeting_room(request):
    return render_to_response('project/meeting_room.html', locals())

def meeting_manage(request):
    return render_to_response('project/meeting_manage.html', locals())	
