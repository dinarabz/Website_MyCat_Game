from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def index_view(request: WSGIRequest):
    name = request.GET.get('name', 'Felix')
    return render(request, 'index.html', context={
        'name': name
    })
