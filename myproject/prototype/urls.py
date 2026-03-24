from django.urls import path
from . import views

urlpatterns = [
    path('', views.iss_tracker, name='iss_tracker'),
    path('iss-position/', views.iss_position, name='iss_position'),
]