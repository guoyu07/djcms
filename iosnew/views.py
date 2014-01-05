# coding:utf-8
from django.shortcuts import render_to_response, redirect
from django.template import Template, Context
from django.template import RequestContext
import os, datetime
from .models import *

def mainpage(request):  # mainpage
    alltext = TextInfo.objects.all()
    d = {}
    for text in alltext:
	d[text.tagname]        = text.text
	d[text.tagname+'_url'] = text.url
    return render_to_response('mainpage.html',d,context_instance=RequestContext(request))

def mainpageenglish(request):  # mainpageenglish
    return render_to_response('mainpageenglish.html', context_instance=RequestContext(request))

def simple(request):  # simple中文页面
    return render_to_response('simple.html', context_instance=RequestContext(request))

def simpleenglish(request):  # simple
    return render_to_response('simpleenglish.html', context_instance=RequestContext(request))
