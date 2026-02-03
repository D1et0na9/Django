from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('Страница блога')

def publications(request):
    return HttpResponse('Очень много научных публикаций')

def card(request, contact_employee_id):
    return HttpResponse(f'<h1>На данной странице можно оставить свои пожелания и предложения для улучшения блога</h1><p>id: {contact_employee_id}</p>')

def card_reprezentation(request, contact_employee_slug):
    return HttpResponse(f'<h1>На данной странице можно оставить свои пожелания и предложения для улучшения блога</h1><p>slug: {contact_employee_slug}</p>')

def archive(request, year):
    return HttpResponse(f'<h1>Архив записей</h1><p>{year}</p>')
