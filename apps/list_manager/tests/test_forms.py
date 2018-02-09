from django.test import TestCase

from apps.list_manager.forms import SearchForm, ChoicesForm


class SearchFormTest(TestCase):

    def test_init_form(self):
        self.assertTrue(SearchForm())


class ChoicesFormTest(TestCase):

    def test_form_data_input(self):
        form_data = {'name': 'movies_choices', 'value': ['1', '2']}
        form = ChoicesForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_choices_input(self):
        choices = [('1', 'choice1'), ('2', 'str')]
        form_data = {'name': 'movies_choices', 'value': ['1', '2']}
        form = ChoicesForm(movies_choices_list=choices, data=form_data)
        self.assertTrue(form.is_valid())
