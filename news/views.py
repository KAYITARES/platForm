from django.http import HttpResponse
import datetime as dte
from django.shortcuts import render
from . models import LanguageDetails

def welcome(request):
  return render(request,"welcome.html")

def today(request):
  today=dte.date.today()
  nam=LanguageDetails.disp()
  return render(request,'allnews/today.html',{'date':today, 'dash':nam})

def pastDate(request,past):
  dates=dte.datetime.strptime(past, '%Y-%m-%d').date()
  return render(request,'allnews/past.html',{'date':dates})