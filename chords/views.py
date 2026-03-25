from django.shortcuts import render
from django.http import JsonResponse
from aiproject.mongo import db
from openai import OpenAI
from django.views.decorators.csrf import csrf_exempt
import json
import os

@csrf_exempt
def get_song_suggestions(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        skill_level = data.get('skill_level')
        known_chords = data.get('known_chords')
        prompt = f"I am a {skill_level} guitarist and I only know these chords: {known_chords}. Suggest 3 songs that use ONLY these exact chords and absolutely no others. Do not suggest any song that requires chords outside of this list. For each song include the title, artist, and chord progression."

    
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        suggestion = response.choices[0].message.content
        return JsonResponse({'suggestions': suggestion})

def index(request):
    return render(request, 'chords/index.html')