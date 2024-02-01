from django.contrib import admin
from django.urls import path

from .views import FileAPIView

urlpatterns = [
    path('upload/', FileAPIView.as_view())
]
