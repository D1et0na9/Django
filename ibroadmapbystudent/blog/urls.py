from django.urls import path, register_converter
from . import views, converters

register_converter(converters.DigitYearConverter, 'year4')

urlpatterns = [
    path('', views.publications),
    path('blog/', views.index),
    path('contact/<int:contact_employee_id>/', views.card),
    path('contact/<slug:contact_employee_slug>/', views.card_reprezentation),
    path('archive/<year4: year>/', views.archive),
]