from django.urls import path

from homeapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('booking/',views.booking,name='booking'),
    path('contact/',views.contact,name='contact'),
    path('doctor/',views.doctor,name='doctor'),
    path('department/',views.department,name='department'),
]
