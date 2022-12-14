from django import forms
from . models import Songs

class SongForm(forms.ModelForm):
    class Meta:
        model=Songs
        fields=('name','artist','year','image')
