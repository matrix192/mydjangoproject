from django.contrib.auth import views
from django.urls import path
from buycars.views import signup
from .views import edit_profile, profile, logout_view

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout_view"),
    path(
        "password_change/", views.PasswordChangeView.as_view(), name="password_change"
    ),
    path(
        "password_change/done/",
        views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("signup/", signup, name="signup"),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('profile/', profile, name='profile'),
]
