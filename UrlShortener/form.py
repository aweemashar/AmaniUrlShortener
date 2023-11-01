from django import forms


class CreateShortURLForm(forms.Form):
    url = forms.CharField
