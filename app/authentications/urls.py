from django.urls import path

from .views import SigninView, SignupView, LogoutView

urlpatterns = [
    path("login/", SigninView.as_view(), name="login"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
