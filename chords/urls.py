from . import views
from django.urls import path

urlpatterns = [
    path('api/chords/', views.get_chords, name='chords'),
]
