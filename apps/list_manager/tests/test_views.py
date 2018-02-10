import json

from django.http import HttpResponseBadRequest
from django.test import TestCase
from unittest.mock import patch
from django.urls import reverse_lazy


movies_choices_list_sample = [{'id': 445842,
                              'title': 'Saber Google',
                              'poster_url': 'https://image.tmdb.org/t/p/w45/ujkOTrAHLIYE3vTuIIiNZYtyhlV.jpg'}]


class MarkerViewTest(TestCase):

    """

    Test the ChoicesForm create view
    (It's a POST over marker_view with a rendered ChoicesForm)

    """

    def test_post_valid_form_without_action(self):
        response = self.client.post(reverse_lazy('list_manager:mark'), {'movies_choices': ['1', '2']})
        self.assertJSONEqual(json.dumps({"err": "Invalid action"}), json.loads(response.content))

    def test_post_valid_form_with_action(self):
        response = self.client.post(reverse_lazy('list_manager:mark'), {'movies_choices': ['2', '1'],
                                                                        'action': 'seen'},)
        self.assertJSONEqual(json.dumps({"marked": True}), json.loads(response.content))

    def test_post_invalid_form(self):
        response = self.client.post(reverse_lazy('list_manager:mark'), {'invalid': 'form'})
        self.assertJSONEqual(json.dumps({"err": "Invalid form post"}), json.loads(response.content))

    def test_post_bad_request(self):
        response = self.client.post(reverse_lazy('list_manager:mark'), {'invalid': 'form'})
        self.assertEqual(HttpResponseBadRequest.status_code, response.status_code)

    def test_not_post(self):
        response = self.client.get(reverse_lazy('list_manager:mark'))
        self.assertEqual(response.url, reverse_lazy('list_manager:search'))


class SearchViewTest(TestCase):
    
    def test_query_movie_empty_search_field(self):
        response = self.client.post(reverse_lazy('list_manager:search'))
        self.assertJSONEqual(json.dumps({'err': 'Fill search field!'}), json.loads(response.content))

    def test_default_response(self):
        response = self.client.get(reverse_lazy('list_manager:search'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list_manager/movie_search.html')
        self.assertContains(response, 'Choose and mark')

    def test_unexpected_method_request(self):
        response = self.client.options(reverse_lazy('list_manager:search'))
        self.assertJSONEqual(json.dumps({"nothing to see": "this isn't happening"}), json.loads(response.content))

    @patch('apps.list_manager.views.retrieve_movies_choices_list_from_tmdb_api_results')
    def test_query_movie_with_valid_search_no_results(self, mock_retrieve_movies_choices_list):
        mock_retrieve_movies_choices_list.return_value = []
        response = self.client.post(reverse_lazy('list_manager:search'), {'post_query': 'Movie Name'})
        self.assertJSONEqual(json.dumps({'err': 'tmdb returned no results'}), json.loads(response.content))

    @patch('apps.list_manager.views.retrieve_movies_choices_list_from_tmdb_api_results')
    def test_query_movie_with_valid_search_and_results(self, mock_retrieve_movies_choices_list):
        mock_retrieve_movies_choices_list.return_value = movies_choices_list_sample
        response = self.client.post(reverse_lazy('list_manager:search'), {'post_query': 'Movie Name'})
        self.assertJSONEqual(json.dumps(movies_choices_list_sample), json.loads(response.content))
