from django.urls import path

from . import views

urlpatterns = [
    path('teamnames/404', views.getNotFound),
    path('teamnames/',views.getSport),
    path('teamnames/<name>', views.getTeamname),

]