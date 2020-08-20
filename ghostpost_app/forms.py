from django import forms

from ghostpost_app.models import Posting

class Post_form(forms.Form):
    boast_or_roast = forms.ModelChoiceField(queryset=Posting.objects.all())
    body = forms.CharField(max_length=280)
    upvote = forms.IntegerField()
    downvote = forms.IntegerField()

