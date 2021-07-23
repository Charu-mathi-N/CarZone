from django.urls import path
from . import views

# app_name = "cars"

urlpatterns = [
    path('inquiry', views.inquiry, name="inquiry"),
]