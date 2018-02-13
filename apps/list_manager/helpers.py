import html
import tmdbsimple
from django.conf import settings


tmdbsimple.API_KEY = settings.TMDB_API_KEY


def retrieve_movie_info_by_tmdb_id(id):
    tmdb_movie = tmdbsimple.Movies(id=id)
    return tmdb_movie.info()


def retrieve_tmdb_api_results(search_string):
    tmdb_search = tmdbsimple.Search()
    tmdb_search.movie(query=html.escape(search_string))
    return tmdb_search.results


def retrieve_tmdb_api_config_info():
    tmdb_config = tmdbsimple.Configuration()
    return tmdb_config.info()


def retrieve_movies_choices_list_from_tmdb_api_results(search_string):
    movies_choices_list = []
    tmdb_config_info = retrieve_tmdb_api_config_info()
    tmdb_results = retrieve_tmdb_api_results(search_string)
    for item in tmdb_results:
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

    return movies_choices_list
