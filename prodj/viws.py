from django.http import HttpResponse
from django.shortcuts import render



# def about (request):
#     return HttpResponse('Thes is test')



def home (request):
    return render(request, 'home.html')



def reverse (request):
    user_text = request.GET['usertext']
    reverced_text = user_text[::-1]
    return render(request, 'reverse.html', {'user_text':user_text, 'reverced_text':reverced_text})