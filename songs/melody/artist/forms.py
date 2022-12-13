from django import forms
from . models import Songs

class SongForm(forms.ModelForm):
    class Meta:
        model=Songs
        fields=('year','image')
