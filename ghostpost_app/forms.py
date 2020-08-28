from django import forms
from ghostpost_app.models import Post


class PostForm(forms.Form):
  post = forms.CharField(max_length=280)
  post_choices = forms.ChoiceField(choices=(
    (True, 'Boast'),
    (False, 'Roast'),
  ))
