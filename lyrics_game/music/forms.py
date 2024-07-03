# music/forms.py
from django import forms

class LyricsForm(forms.Form):
    user_input = forms.CharField(label='Complete the lyrics', max_length=100)
    random_word = forms.CharField(widget=forms.HiddenInput())
    words_around = forms.CharField(widget=forms.HiddenInput())


class LyricsGameForm(forms.Form):
    user_input = forms.CharField(label='Guess the word', max_length=100)
