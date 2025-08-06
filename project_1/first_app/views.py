from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def courses(request):
    return HttpResponse("This is courses Page. ")
def about(request):
    return HttpResponse("This is About Page. ")
def house(request):
    return HttpResponse("This is house Page. ")