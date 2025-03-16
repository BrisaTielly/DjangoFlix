from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from genres.models import Genre
import json
# Create your views here.

@csrf_exempt
def genre_view(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        data = []
        for genre in genres:
            data.append({"id" : genre.id, "name" : genre.name})
        return JsonResponse(data, safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        new_genre = Genre(name = data['name'])
        new_genre.save()
        return JsonResponse(
            {'id' : new_genre.id, 'name': new_genre.name}, 
            status = 201
        )

@csrf_exempt
def genre_detail_view(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    return JsonResponse(
        {'id' : genre.id, 'name' : genre.name},
        safe=False,
    )