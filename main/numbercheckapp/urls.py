from django.urls import path
from . import views

urlpatterns= [
    path("number", views.form,name="displayform"),
    path("check", views.findTheNumber, name="displayform")
]