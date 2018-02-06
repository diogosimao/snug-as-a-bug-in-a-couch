import html
import json

import tmdbsimple
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest

from django.shortcuts import render
from django.conf import settings
from django.urls import reverse_lazy

from .forms import SearchForm, ChoicesForm, ThumbnailImagesChoicesForm

tmdbsimple.API_KEY = settings.TMDB_API_KEY


def tmdb_search_view(request):
    if request.method == 'POST':
        post_text = request.POST.get('post_query', None)
        filters_choices = request.POST.get('filters_choices', None)
        tmdb_search = tmdbsimple.Search()
        response = None
        if post_text:
            search_string = html.escape(post_text)
            if filters_choices:
                response = tmdb_search.movie(query=search_string, year='2018')
            else:
                response = tmdb_search.movie(query=search_string)
            tmdb_config = tmdbsimple.Configuration()
            tmdb_config_info = tmdb_config.info()
            movies_choices_list = []
            for item in tmdb_search.results:
                result = {}
                base_url = tmdb_config_info.get('images').get('secure_base_url')
                size = tmdb_config_info.get('images').get('profile_sizes')[1]
                poster_path = item.get('poster_path')
                poster_url = ""
                if poster_path:
                    poster_url = "{}{}{}".format(base_url, size, poster_path)

                result['id'] = item.get('id')
                result['title'] = item.get('title')
                result['poster_url'] = poster_url
                movies_choices_list.append(result)

        if response:
            return HttpResponse(json.dumps(movies_choices_list), content_type="application/json")

        return HttpResponseBadRequest(json.dumps({'err': 'Fill search field!'}), content_type="application/json")

    elif request.method == 'GET':
        form = SearchForm()
        choices_form = ChoicesForm()
        thumbnail_img_choices_form = ThumbnailImagesChoicesForm()
        context = {'form': form, 'choices_form': choices_form, 'thumbnail_img_choices_form': thumbnail_img_choices_form}
        return render(request, 'list_manager/movie_search.html', context)
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def marker_view(request):
    if request.method == 'POST':
        form = ChoicesForm(request.POST)
        if form.is_valid():
            if 'seen' in request.POST:
                return HttpResponseRedirect(reverse_lazy('list_manager:search'))
            elif 'wannasee' in request.POST:
                return HttpResponseRedirect(reverse_lazy('list_manager:search'))

    return HttpResponseRedirect(reverse_lazy('list_manager:search'))

