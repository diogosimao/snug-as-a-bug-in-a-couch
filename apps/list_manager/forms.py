from django import forms


class SearchForm(forms.Form):

    FILTER_CHOICES = [('2018', 'Release at 2018')]

    filters_choices = forms.MultipleChoiceField(required=False, choices=FILTER_CHOICES,
                                                widget=forms.CheckboxSelectMultiple(attrs={
                                                    'id': 'filters-choices'}
                                                ))

    search = forms.CharField(required=True, max_length=255, widget=forms.TextInput(
        attrs={
            'required': 'True',
            'id': 'query-search',
            'placeholder': 'Search for movies you wanna add to your lists'
        }))


class ChoicesForm(forms.Form):

    def __init__(self, movies_choices_list=[], *args, **kwargs):
        super(ChoicesForm, self).__init__(*args, **kwargs)
        self.fields['movies_choices'].choices = movies_choices_list

    movies_choices = forms.MultipleChoiceField(
        required=False,
        choices=(),
        help_text='Check as many as you like.',
        widget=forms.SelectMultiple(attrs={
            'id': 'movies-choices'}
        )
    )

