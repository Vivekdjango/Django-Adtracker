from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponse

from django.contrib.sessions.backends.db import SessionStore

from bar import *

from .models import *

from insert import *

import os

import subprocess

from report import *

import requests
from django.contrib.gis.geoip import GeoIP
#g = GeoIP()


os.environ["VAR"]="http://10.14.125.159:8000"
ip=dict(os.environ.items())
o=ip['LANG'].split('_')

def dash(request):
	return render_to_response('index.html')

def repo(request):
	return render_to_response('report.htm')

def plat(request):
	return render(request,'platform.html')

def new(request):
	return render(request,"first.html") # For POST method necessary to put render method

def image(request):
	img=db_image()
	current = db_curr()	
	return render_to_response("overview.html",{"img":img,"cu":current})


def video(request):
	img=db_image()
        current = db_curr()
        return render_to_response("vid.html",{"img":img,"cu":current})


def carou(request):
	img=db_image()
        current = db_curr()
        return render_to_response("carou.html",{"img":img,"cu":current})


def banner(request):
	img=db_image()
        current = db_curr()
        return render_to_response("ban.html",{"img":img,"cu":current})



def map(request):
	return render_to_response('map.htm')
count=0
def text(request):
	global count
	if request.method == 'POST':
		count+=1
	ip=request.META['REMOTE_ADDR']
	pf=request.META['HTTP_USER_AGENT'].split()[2]
	proc = subprocess.Popen(["whois %s | awk -F':[ \t]+' 'tolower($1) ~ /^country$/ { print toupper($2) }'"%(ip)], stdout=subprocess.PIPE, shell=True)
	(location,err)=proc.communicate()
	insert(ip,pf,count,location)
	return HttpResponse()


def banu(request):
	global count
        if request.method == 'POST':
                count+=1
        ip=request.META['REMOTE_ADDR']
        pf=request.META['HTTP_USER_AGENT'].split()[2]
        proc = subprocess.Popen(["whois %s | awk -F':[ \t]+' 'tolower($1) ~ /^country$/ { print toupper($2) }'"%(ip)], stdout=subprocess.PIPE, shell=True)
        (location,err)=proc.communicate()
        bann(ip,pf,count,location)
        return HttpResponse()


def vid(request):
        global count
        if request.method == 'POST':
                count+=1
        ip=request.META['REMOTE_ADDR']
        pf=request.META['HTTP_USER_AGENT'].split()[2]
        proc = subprocess.Popen(["whois %s | awk -F':[ \t]+' 'tolower($1) ~ /^country$/ { print toupper($2) }'"%(ip)], stdout=subprocess.PIPE, shell=True)
        (location,err)=proc.communicate()
        vid(ip,pf,count,location)
        return HttpResponse()

def caru(request):
        global count
        if request.method == 'POST':
                count+=1
        ip=request.META['REMOTE_ADDR']
        pf=request.META['HTTP_USER_AGENT'].split()[2]
        proc = subprocess.Popen(["whois %s | awk -F':[ \t]+' 'tolower($1) ~ /^country$/ { print toupper($2) }'"%(ip)], stdout=subprocess.PIPE, shell=True)
        (location,err)=proc.communicate()
        carou(ip,pf,count,location)
        return HttpResponse()



def bar(request):
	t=db_bar()
	j,e,n,c=[],[],[],[]
        for i in t[1:]:
                j.append(int(float(i[1]))/100),e.append(int(float(i[2]))/10),n.append(int(float(i[3]))/10),c.append(int(float(i[4]))/10)
	jp=sum(j)/240
	ep=sum(e)/240
	np=sum(n)/240
	cp=sum(c)/240
        return render_to_response('test.html',{'japac':j,'emea':e,'na':n,'central':c,'jp':jp,'ep':ep,'np':np,'cp':cp})
      
