import json

from django.http import HttpResponseBadRequest
from django.test import TestCase, Client
from django.urls import reverse_lazy


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
