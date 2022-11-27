from django.urls import path
from . import views


urlpatterns = [
    path('random-uuid', views.random_uuid)
]
