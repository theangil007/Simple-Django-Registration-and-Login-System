from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexpageview, name="index"),
    path("register/", views.registerpageview, name="register"),
    path("dashboard/", views.dashboardpageview, name="dashboard"),
]
