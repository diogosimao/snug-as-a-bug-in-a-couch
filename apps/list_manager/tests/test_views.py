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
        response = self.client.post(reverse_lazy('list_manager:mark'), {'movies_choices': ['choice1', 'choice2']})
        self.assertJSONEqual(json.dumps({"err": "Invalid action"}), json.loads(response.content))

    def test_post_valid_form_with_action(self):
        response = self.client.post(reverse_lazy('list_manager:mark'), {'movies_choices': ['choice1', 'choice2'],
                                                                        'action': 'seen'},)
        self.assertJSONEqual(json.dumps({"seen": True}), json.loads(response.content))

    def test_post_invalid_form(self):
        response = self.client.post(reverse_lazy('list_manager:mark'), {'invalid': 'form'})
        self.assertJSONEqual(json.dumps({"err": "Invalid form post"}), json.loads(response.content))

    def test_post_bad_request(self):
        response = self.client.post(reverse_lazy('list_manager:mark'), {'invalid': 'form'})
        self.assertEqual(HttpResponseBadRequest.status_code, response.status_code)

    def test_not_post(self):
        response = self.client.get(reverse_lazy('list_manager:mark'))
        self.assertEqual(response.url, reverse_lazy('list_manager:search'))
