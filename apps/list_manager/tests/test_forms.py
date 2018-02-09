from django.test import TestCase

from apps.list_manager.forms import SearchForm, ChoicesForm


class SearchFormTest(TestCase):

    def test_init_form(self):
        self.assertTrue(SearchForm())


class ChoicesFormTest(TestCase):

    def test_form_data_input(self):
        form_data = {'movies-choices': [('1', 'choice1')]}
        form = ChoicesForm(data=form_data)
        self.assertTrue(form.is_valid())
