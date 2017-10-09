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

#apps
urlpatterns = [
    url(r'^$', views.index),
    url(r'^', include(router.urls)),
    url(r'^index', views.index),
    url(r'^admin_backend/', admin.site.urls),
    url(r'^contact', views.contact),
    url(r'^portfolio_1_col', views.portfolio_1_col),
    url(r'^portfolio_2_col', views.portfolio_2_col),
    url(r'^portfolio_3_col', views.portfolio_3_col),
    url(r'^portfolio_4_col', views.portfolio_3_col),
    #url(r'^admin', views.admin),
    url(r'^admin_loging', views.admin_loging),
    url(r'^about', views.about),
    url(r'^login', views.login),
    url(r'^full_width', views.full_width),
    url(r'^information', views.information),
    url(r'^choose', views.choose),
    url(r'^room', views.room),
    url(r'^blog_home_1', views.blog_home_1),
    url(r'^blog_home_2', views.blog_home_2),
    url(r'^blog_post', views.blog_post),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    #   restful-api     #
    url(r'^memberApi', views.MemberList),
    url(r'^meetingApi', views.MeetingList),
    url(r'^positionApi', views.PositionList),
    url(r'^checkinApi', views.CheckinList),
    #url(r'^positionApi/(?P<who>[\w\-]+)', views.PositionList),
    #url(r'^member_api/(?P<member_name>[0-9]+)$', views.MemberDetail.as_view()),
    
]

#urlpatterns = format_suffix_patterns(urlpatterns)

