from django.urls import path, include
from home.views import home, dashboard

app_name = "home"

urlpatterns = [
    path("", home, name="home"),
    path("dashboard",dashboard, name="dashboard")
]