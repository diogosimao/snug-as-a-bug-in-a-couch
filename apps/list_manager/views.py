import html
import json
from ast import literal_eval

import tmdbsimple
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.conf import settings
from django.urls import reverse_lazy

from .forms import SearchForm, ChoicesForm, ThumbnailImagesChoicesForm
from .models import WatchList

tmdbsimple.API_KEY = settings.TMDB_API_KEY


def tmdb_search_view(request):
    if request.method == 'POST':
        post_text = request.POST.get('post_query', None)
        filters_choices = request.POST.get('filters_choices', None)
        tmdb_search = tmdbsimple.Search()
        if post_text:
            search_string = html.escape(post_text)
            if filters_choices:
                tmdb_search.movie(query=search_string, year='2018')
            else:
                tmdb_search.movie(query=search_string)
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

            if movies_choices_list:
                return HttpResponse(json.dumps(movies_choices_list), content_type="application/json")

        return HttpResponseBadRequest(json.dumps({'err': 'Fill search field!'}), content_type="application/json")

    elif request.method == 'GET':
        context = {'form': SearchForm(),
                   'choices_form': ChoicesForm(),
                   'thumbnail_img_choices_form': ThumbnailImagesChoicesForm()}
        return render(request, 'list_manager/movie_search.html', context)
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def marker_view(request):
    if request.method == 'POST':
        movies_choices_list = dict(request.POST).get('movies_choices')
        if movies_choices_list:
            choices = list(map(lambda item: (item, 'str'), movies_choices_list)) \
                if isinstance(movies_choices_list, list) else list()
            form = ChoicesForm(movies_choices_list=choices, data=request.POST)
        else:
            form = ChoicesForm(request.POST)
        if form.is_valid():
            post_dict = dict(request.POST)
            action = post_dict.get('action', list())
            for tmdb_id in post_dict.get("movies_choices"):
                item = WatchList(tmdb_id=literal_eval(tmdb_id))
                if 'seen' in action:
                    item.seen = True
                elif 'wannasee' in action:
                    item.seen = False
                else:
                    return HttpResponseBadRequest(json.dumps({'err': 'Invalid action'}), content_type="application/json")
                item.save()
            return HttpResponse(json.dumps({'marked': True}), content_type="application/json")
        else:
            return HttpResponseBadRequest(json.dumps({'err': 'Invalid form post'}), content_type="application/json")

    return HttpResponseRedirect(reverse_lazy('list_manager:search'))

