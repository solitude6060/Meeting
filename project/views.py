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

#################################################################
#restful api's view
#################################################################
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
        #m = Member.objects.filter(member_email=pk)

    if request.method == 'GET':
        #queryset = Member.objects.all()
        serializer = PositioningSerializer(position_obj, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        #serializer = PositioningSerializer(mem, data=data)
        serializer = PositioningSerializer(data=data)
        if serializer.is_valid():

            # Positioning.objects.update_or_create(
            #     current_ssid=data["current_ssid"][0], wifi_level=data["wifi_level"],
            #     defaults={"mac_address": mac},
            # )
            mac_ad.delete()
            serializer.save()
            #serializer.update(pos_id, data)

            ser_filter = PositioningSerializer(mac_ad, many=True)
            return Response(ser_filter.data)
        
        return JsonResponse(serializer.errors, status=400)

class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Positioning.objects.get(member_email=pk)
        except Positioning.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        position = self.get_object(pk)
        serializer = PositioningSerializer(position)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        position = self.get_object(pk)
        serializer = PositioningSerializer(position, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        position = self.get_object(id=pk)
        position.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Positioning.objects.all()
#     serializer_class = PositioningSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


@api_view(['GET', 'POST'])
def CheckinList(request):
    #List all code snippets, or create a new snippet.
    if request.method == 'GET':
        queryset = Meeting.objects.all()
        serializer = CheckInSerializer()
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CheckInSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
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


#################################################################
#   web app's view
#################################################################
def index(request):
     return render_to_response('project/index.html', locals())

def contact(request):
    return render_to_response('project/contact.html', locals())

def portfolio_1_col(request):
    return render_to_response('project/portfolio_1_col.html', locals())

def portfolio_2_col(request):
    return render_to_response('project/portfolio_2_col.html', locals())

def portfolio_3_col(request):
    return render_to_response('project/portfolio_3_col.html', locals())

def portfolio_4_col(request):
    return render_to_response('project/portfolio_4_col.html', locals())

def admin(request):
    return render_to_response('project/admin.html', locals())

def about(request):
    return render_to_response('project/about.html', locals())

def login(request):
    return render_to_response('project/login.html', locals())

def information(request):
    return render_to_response('project/information.html', locals())

def full_width(request):
    return render_to_response('project/full_width.html', locals())

def choose(request):
    return render_to_response('project/choose.html', locals())

def room(request):
    return render_to_response('project/room.html', locals())

def blog_home_1(request):
    return render_to_response('project/blog_home_1.html', locals())

def blog_home_2(request):
    return render_to_response('project/blog_home_2.html', locals())

def blog_post(request):
    return render_to_response('project/blog_post.html', locals())



