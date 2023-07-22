from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request):
    return HttpResponse('1st app First response')
def second(request):
    return HttpResponse('1st app First response')