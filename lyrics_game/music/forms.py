# music/forms.py
from django import forms


class LyricsForm(forms.Form):
    lyrics_input = forms.CharField(label='Complete the lyrics', max_length=100)
