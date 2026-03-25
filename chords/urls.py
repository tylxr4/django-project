from . import views
from django.urls import path

urlpatterns = [
    path('api/chords/', views.get_song_suggestions, name='song_suggestions'),
    path('', views.index, name='index'),
    
]
