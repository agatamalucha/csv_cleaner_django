from django.urls import path, include
from home.views import home, dashboard, my_page

app_name = "home"

urlpatterns = [
    path("", home, name="home"),
    path("dashboard",dashboard, name="dashboard"),
    path ("my_page", my_page, name="my_page"),
]