from django.urls import path
from home import views
from home.dash_apps.finished_apps import simpleexample


urlpatterns = [
    path('', views.index, name="home")
]
