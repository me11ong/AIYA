from django.urls import path
from . import views

app_name='inside'

urlpatterns = [
    path('',views.inside,name="main"),
    path('forecast',views.inside_forecast,name="forecast"),
]