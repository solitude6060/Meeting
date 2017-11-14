"""Meeting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
admin.autodiscover()
from project import views
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns


#apis
router = routers.DefaultRouter()
router.register(r'meeting', views.MeetingViewSet, 'meeting-view')
router.register(r'member', views.MemberViewSet, 'member-view')
router.register(r'meetingroom', views.MeetingRoomViewSet, 'meetingroom-view')
router.register(r'user', views.UserViewSet, 'user-view')

#apps
urlpatterns = [
    url(r'^$', views.index),
    url(r'^', include(router.urls)),
    url(r'^index', views.index),
    url(r'^admin_backend/', admin.site.urls),
    url(r'^information', views.information),
    url(r'^admin_logging', views.admin_loging),
    url(r'^login', views.login),
    url(r'^login/', TemplateView.as_view(template_name="login.html"),
                   name='login'),
    url(r'^upload', views.upload),
    url(r'^about', views.about),
    url(r'^logout', views.logout),
    url(r'^join&(?P<meetingId>[0-9]+)$', views.join),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^admin_homepage', views.admin_page),
	url(r'^personalpage', views.personalpage),
	
    #   restful-api     #
    url(r'^memberUpdate/(?P<pk>.+)$', views.MemberDetail),
    url(r'^memberApi', views.MemberList),
    url(r'^meetingApi', views.MeetingList),
    url(r'^positionApi', views.PositionList),
    url(r'^positionUpdate/(?P<pk>.+)/(?P<mac>.+)$', views.PositionDetail),
    url(r'^checkinApi', views.CheckinList),
    url(r'^checkinUpdate/(?P<member>.+)/(?P<meeting>.+)$', views.CheckinDetail),
    url(r'^feedbackApi', views.FeedbackList),
    url(r'^feedbackUpdate/(?P<member>.+)/(?P<meeting>.+)$', views.FeedbackDetail),
    #url(r'^member_api/(?P<member_name>[0-9]+)$', views.MemberDetail.as_view()),

    #   OAuth-login     #
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    
]

#urlpatterns = format_suffix_patterns(urlpatterns)

