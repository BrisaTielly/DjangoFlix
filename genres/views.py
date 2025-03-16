from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from genres.models import Genre
import json
# Create your views here.

@csrf_exempt
def genreView(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        list = []
        for genre in genres:
            list.append({"id" : genre.id, "name" : genre.name})
        return JsonResponse(list, safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        new_genre = Genre(name = data['name'])
        new_genre.save()
        return JsonResponse(
            {'id' : new_genre.id, 'name': new_genre.name}, 
            status = 201
        )