from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('Страница блога')

def publications(request):
    return HttpResponse('Очень много научных публикаций')

def card(request):
    return HttpResponse('На данной странице можно оставить свои пожелания и предложения для улучшения блога')