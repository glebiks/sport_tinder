from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('matches', views.matches, name="matches"),
    path('settings', views.settings, name="settings"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('logout', views.logout, name="logout"),
]