import html
import json

import tmdbsimple
from django.http import HttpResponseRedirect, HttpResponse

from django.shortcuts import render
from django.conf import settings
from django.urls import reverse_lazy

from .forms import QueryForm, ChoicesForm

tmdbsimple.API_KEY = settings.TMDB_API_KEY


def manager_view(request):
    movies_choices_list = []
    if request.method == 'POST':
        post_text = request.POST.get('post_query', None)
        filters_choices = request.POST.get('filters_choices', None)
        if post_text:
            search = tmdbsimple.Search()

            search_string = html.escape(post_text)
            if filters_choices:
                response = search.movie(query=search_string, year='2018')
            else:
                response = search.movie(query=search_string)

            for result in search.results:
                movies_choices_list.append((result.get('id'), result.get('title')))

        return HttpResponse(
                    json.dumps(search.results),
                    content_type="application/json"
                )
    elif request.method == 'GET':
        form = QueryForm()
        choices_form = ChoicesForm()
        context = {'form': form, 'choices_form': choices_form}
        return render(request, 'tmdb/movie_manager.html', context)
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def check_view(request):
    if request.method == 'POST':
        form = ChoicesForm(request.POST)
        if form.is_valid():
            if 'seen' in request.POST:
                return HttpResponseRedirect(reverse_lazy('tmdb:manager'))
            elif 'wannasee' in request.POST:
                return HttpResponseRedirect(reverse_lazy('tmdb:manager'))

    return HttpResponseRedirect(reverse_lazy('tmdb:manager'))

