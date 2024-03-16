from django.urls import path
from.import views

urlpatterns = [
    path('',views.home),
     path('login/',views.login),
     path('reg/',views.reg),
     path('about/',views.about),
     path('CONTACT/',views.contact),
    
]