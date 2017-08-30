#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.
#
#

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







