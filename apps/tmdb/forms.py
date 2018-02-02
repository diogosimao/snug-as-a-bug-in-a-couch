from django import forms


class QueryForm(forms.Form):

    FILTER_CHOICES = [(True, 'Release at 2018')]

    filters_choices = forms.ChoiceField(required=False, choices=FILTER_CHOICES, widget=forms.RadioSelect())
    search = forms.CharField(required=True, max_length=255)


class ChoicesForm(forms.Form):

    def __init__(self, movies_choices_list=[], *args, **kwargs):
        super(ChoicesForm, self).__init__(*args, **kwargs)
        self.fields['movies_choices'].choices = movies_choices_list

    movies_choices = forms.MultipleChoiceField(
        required=False,
        choices=(),
        help_text='Check as many as you like.',
    )

