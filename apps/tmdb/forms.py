from django import forms


class QueryForm(forms.Form):
    CHOICES = [(True, 'Release at 2018')]

    choices = forms.ChoiceField(required=False, choices=CHOICES, widget=forms.RadioSelect())
    search = forms.CharField(required=False, max_length=255)

