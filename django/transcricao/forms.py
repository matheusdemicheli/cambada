from django import forms


class TranscricaoForm(forms.Form):
    arquivo = forms.FileField()
