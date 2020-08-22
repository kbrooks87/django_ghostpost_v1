from django.db import models

from django.utils import timezone
# Create your models here.

class Posting(models.Model):
    boast = models.BooleanField()
    roast = models.BooleanField()
    body = models.CharField(max_length=280)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.body

