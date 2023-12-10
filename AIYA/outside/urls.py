from django.urls import path
from . import views

app_name='outside'

urlpatterns = [
    path('',views.outside,name="main"),
]