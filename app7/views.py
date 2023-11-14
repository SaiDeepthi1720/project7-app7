from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mom(request):
    return HttpResponse('<h1><marquee>hi mom how r u</h1></marquee>')
