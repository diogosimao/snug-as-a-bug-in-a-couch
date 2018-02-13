from django.test import TestCase
from unittest.mock import patch

from apps.list_manager import helpers


tmdb_movie_search_result_sample = [{'id': 445842,
                                    'title': 'Saber Google',
                                    'poster_path': '/ujkOTrAHLIYE3vTuIIiNZYtyhlV.jpg'}
                                   ]

tmdb_configuration_info_sample = {'images': {'secure_base_url': 'https://image.tmdb.org/t/p/',
                                             'profile_sizes': ['x00', 'w45']}
                                  }

tmdb_movie_info_result_sample = {'original_title': 'LEGO Marvel Super Heroes: Avengers Reassembled!',
                                 'title': 'LEGO Marvel Super Heroes: Avengers Reassembled!'}


class TMDBHelperTest(TestCase):

    @patch('apps.list_manager.helpers.retrieve_tmdb_api_results')
    @patch('apps.list_manager.helpers.retrieve_tmdb_api_config_info')
    def test_retrieve_movies_choices_list(self, mock_info, mock_results):
        mock_info.return_value = tmdb_configuration_info_sample
        mock_results.return_value = tmdb_movie_search_result_sample
        desired_output = [{'id': 445842,
                           'title': 'Saber Google',
                           'poster_url': """https://image.tmdb.org/t/p/w45/ujkOTrAHLIYE3vTuIIiNZYtyhlV.jpg"""}]

        output = helpers.retrieve_movies_choices_list_from_tmdb_api_results('string')
        self.assertEqual(output, desired_output)


    @patch('apps.list_manager.helpers.html')
    @patch('tmdbsimple.Search')
    def test_retrieve_tmdb_api_results(self, mock_search, mock_html):
        mock_search.return_value.movie.return_value = None
        mock_search.return_value.results = tmdb_movie_search_result_sample
        self.assertEqual(tmdb_movie_search_result_sample, helpers.retrieve_tmdb_api_results("string?venus/marte''"))
        self.assertTrue(mock_html.escape.called)


    @patch('tmdbsimple.Configuration')
    def test_retrieve_tmdb_api_config_info(self, mock_config_info):
        mock_config_info.return_value.info.return_value = tmdb_configuration_info_sample
        self.assertEqual(helpers.retrieve_tmdb_api_config_info(), tmdb_configuration_info_sample)


    @patch('tmdbsimple.Movies')
    def test_retrieve_movie_info_by_tmdb_id(self, mock_movies):
        mock_movies.return_value.info.return_value = tmdb_movie_info_result_sample
        self.assertEqual(helpers.retrieve_movie_info_by_tmdb_id(id=368304).get('id'),
                         tmdb_movie_info_result_sample.get('id'))
