from django.http import HttpResponse
from django.shortcuts import render



def about (request):
    return HttpResponse('Thes is test')



def home (request):
    return render(request, 'home.html')