import html

import tmdbsimple as tmdb

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.conf import settings

from .forms import QueryForm

tmdb.API_KEY = settings.TMDB_API_KEY


def query_view(request):
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            search = tmdb.Search()
            search_string = html.escape(form.data.get('search', ''))
            if form.data.get('choices', None):
                response = search.movie(query=search_string, year='2018')
            else:
                response = search.movie(query=search_string)
            for s in search.results:
                print(s['title'], s['id'], s['release_date'], s['popularity'])
            return HttpResponseRedirect(reverse_lazy('tmdb:query'))

    else:
        form = QueryForm()
        context = {'form': form}
        return render(request, 'tmdb/query_list.html', context)
