from django.urls import path
from .views import CreateUserView , HomePage      # APP URL

urlpatterns = [
    path("home/", HomePage.as_view(), name="home"),
    path("register/", CreateUserView.as_view(), name="register"),
]