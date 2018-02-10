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

    @patch('tmdbsimple.Search.movie')
    def test_retrieve_tmdb_api_results(self, mock_search):
        pass

    @patch('tmdbsimple.Configuration')
    def test_retrieve_tmdb_api_config_info(self, mock_config_info):
        mock_config_info.return_value.info.return_value = tmdb_configuration_info_sample
        self.assertEqual(helpers.retrieve_tmdb_api_config_info(), tmdb_configuration_info_sample)
