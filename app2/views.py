from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request):
    return HttpResponse('2nd app First response')
def second(request):
    return HttpResponse('2nd app First response')