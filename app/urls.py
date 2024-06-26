from django.urls import path
from . import views


app_name = "app"
urlpatterns = [
    path("", views.index, name="landing"),
    path("signin/", views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout_view, name="logout"),
]
