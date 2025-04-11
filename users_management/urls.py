from django.urls import path
from django.contrib.auth import views as auth_views
from users_management import views



urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users_management/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
]