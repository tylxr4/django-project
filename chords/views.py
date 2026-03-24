from django.shortcuts import render
from .models import Chord
from django.http import JsonResponse
from aiproject.mongo import db
# Create your views here.
def get_chords(request):
    
    chords = list(db['chords_chord'].find({}))
    for chord in chords:
        chord['_id'] = str(chord['_id'])
    return JsonResponse(chords, safe=False)