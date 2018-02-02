import html

import tmdbsimple

from django.shortcuts import render
from django.conf import settings

from .forms import QueryForm

tmdbsimple.API_KEY = settings.TMDB_API_KEY


def query_view(request):
    movies_choices_list = []
    if request.method == 'POST':
        form = QueryForm([], request.POST)
        if form.is_valid():
            search = tmdbsimple.Search()
            search_string = html.escape(form.data.get('search', ''))
            if form.data.get('filters_choices', None):
                response = search.movie(query=search_string, year='2018')
            else:
                response = search.movie(query=search_string)

            for result in search.results:
                movies_choices_list.append((result.get('id'), result.get('title')))

            form = QueryForm(movies_choices_list=movies_choices_list)
    else:
        form = QueryForm()

    context = {'form': form}
    
    return render(request, 'tmdb/query_list.html', context)
