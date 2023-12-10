from django.urls import path
from . import views

app_name='tomorrow'

urlpatterns = [
    path('',views.tomorrow_A, name="main"),
    path('forecast',views.tomorrow_B, name="forecast"),
]