from django import forms

from ghostpost_app.models import Posting

class Post_form(forms.Form):
    boast = forms.BooleanField(widget=forms.NullBooleanSelect())
    roast = forms.BooleanField(widget=forms.NullBooleanSelect())
    body = forms.CharField(max_length=280)


class Upvoting_form(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ["upvote"]


class Downvoting_form(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ["upvote"]

