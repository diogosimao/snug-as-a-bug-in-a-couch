import html

import tmdbsimple
from django.http import HttpResponseRedirect

from django.shortcuts import render
from django.conf import settings
from django.urls import reverse_lazy

from .forms import QueryForm, ChoicesForm

tmdbsimple.API_KEY = settings.TMDB_API_KEY


def manager_view(request):
    movies_choices_list = []
    choices_form = ChoicesForm()
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            search = tmdbsimple.Search()
            search_string = html.escape(form.data.get('search', ''))
            if form.data.get('filters_choices', None):
                response = search.movie(query=search_string, year='2018')
            else:
                response = search.movie(query=search_string)

            for result in search.results:
                movies_choices_list.append((result.get('id'), result.get('title')))

            choices_form = ChoicesForm(movies_choices_list=movies_choices_list)
    else:
        form = QueryForm()

    context = {'form': form, 'choices_form': choices_form}
    
    return render(request, 'tmdb/movie_manager.html', context)


def check_view(request):
    if request.method == 'POST':
        form = ChoicesForm(request.POST)
        print('POSTED')
        if form.is_valid():
            if 'seen' in request.POST:
                return HttpResponseRedirect(reverse_lazy('tmdb:manager'))
            elif 'wannasee' in request.POST:
                return HttpResponseRedirect(reverse_lazy('tmdb:manager'))

    return HttpResponseRedirect(reverse_lazy('tmdb:manager'))

