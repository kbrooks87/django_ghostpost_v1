from django.shortcuts import render, HttpResponseRedirect, reverse

from ghostpost_app.models import Posting
from ghostpost_app.forms import Post_form, Upvoting_form, Downvoting_form
# Create your views here.

def index(request):
    posts = Posting.objects.all()

    return render(request, "index.html", {"posts": posts})


def new_post_view(request):
    if request.method == "POST":
        form = Post_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Posting.objects.create(
                boast=data.get("boast"),
                roast=data.get("roast"),
                body=data.get("body")
            )
            return HttpResponseRedirect(reverse('newpost'))
        form = Post_form()
        return render(request, "new_post.html", {"form": form})


def upvoting_view(request):
    if request == "POST":
        form = Upvoting_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Posting.upvote = Posting.upvote + 1
        form = Upvoting_form()
        return render(request, "index.html", {"upvote": form})


def downvoting_view(request):
    if request == "POST":
        form = Downvoting_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Posting.downvote = Posting.downvote + 1
        form = Downvoting_form()
        return render(request, "index.html", {"downvote": form})

