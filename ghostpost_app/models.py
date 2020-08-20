from django.db import models

from django.utils import timezone
# Create your models here.

class Posting(models.Model):
    boast_or_roast = models.BooleanField(default=True)
    body = models.CharField(max_length=280)
    upvote = models.IntegerField()
    downvote = models.IntegerField()
    post_date = models.DateTimeField(default=timezone.now)


