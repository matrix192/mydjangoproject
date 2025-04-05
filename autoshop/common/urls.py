from django.contrib.auth import views
from django.urls import path
from buycars.views import signup
from .views import edit_profile, profile, logout_view
from django.conf import settings
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import never_cache

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout_view"),
    path("signup/", signup, name="signup"),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('profile/', profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))