from django.utils.translation import ugettext_lazy as _
from django import forms
from django.conf import settings


class SearchForm(forms.Form):

    FILTER_CHOICES = [('2018', _('Release at 2018'))]

    filters_choices = forms.MultipleChoiceField(required=False, label='', choices=FILTER_CHOICES,
                                                widget=forms.CheckboxSelectMultiple(attrs={
                                                    'id': 'filters-choices'
                                                }))

    search = forms.CharField(required=True, max_length=255, label='', widget=forms.TextInput(
        attrs={
            'required': 'True',
            'id': 'query-search',
            'placeholder': _('Search for movies you wanna add to your lists')
        }))


class ChoicesForm(forms.Form):

    def __init__(self, movies_choices_list=None, *args, **kwargs):
        if movies_choices_list is None:
            movies_choices_list = list()
        super(ChoicesForm, self).__init__(*args, **kwargs)
        movies_choices = forms.MultipleChoiceField(choices=movies_choices_list,
                                                   required=False,
                                                   help_text=_('Check as many as you like.'),
                                                   label='',
                                                   widget=forms.SelectMultiple(attrs={
                                                       'id': 'movies-choices',
                                                   }))
        self.fields['movies_choices'] = movies_choices

    movies_choices = forms.MultipleChoiceField(
        required=False,
        choices=(),
        label='',
        help_text=_('Check as many as you like.'),
        widget=forms.SelectMultiple(attrs={
            'id': 'movies-choices',
        }))


class ThumbnailImagesChoicesForm(forms.Form):

    thumbnail_img_movies_choices = forms.MultipleChoiceField(
        required=False,
        choices=(),
        label='',
        widget=forms.CheckboxSelectMultiple(attrs={
            'id': 'thumbnail-img-movies-choices',
        }))


class LanguageForm(forms.Form):

    language = forms.ChoiceField(required=True, label='', choices=settings.LANGUAGES, widget=forms.Select(attrs={
        'value': '/',
    }))

    next = forms.CharField(label='', widget=forms.HiddenInput(attrs={'value': '/'}))

