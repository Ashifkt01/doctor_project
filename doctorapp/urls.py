from django.urls import path
from doctorapp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/',views.about,name='about'),
    path('booking/',views.booking,name='booking'),
    path('contact/',views.contact,name='contact'),
    path('department/',views.department,name='department'),
    path('doctor/',views.doctors,name='doctor'),
    path('confirmation/',views.confirmation,name='confirmation'),
]