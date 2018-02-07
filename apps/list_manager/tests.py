from django.test import TestCase

from .forms import SearchForm


class SearchFormTest(TestCase):

    def setUp(self):
        TestCase.setUp(self)

    def test_init(self):
        SearchForm()

