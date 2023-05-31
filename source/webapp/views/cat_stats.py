from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render

from source.webapp.cat import Cat


def add_view(request: WSGIRequest):
    if request.method == "GET":
        context = {
            'name': Cat.name,
            'age': Cat.age,
            'health': Cat.health,
            'happiness': Cat.happiness,
            'satiety': Cat.satiety,
            'sleep': Cat.sleep
        }
        return render(request, 'cat_stats.html', context=context)

    Cat.update_name(request)
    Cat.apply_action(request)
    return HttpResponseRedirect(request.path_info)
