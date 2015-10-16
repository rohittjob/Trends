from django.db import models


class TopTrends(models.Model):
    topic = models.CharField(max_length=200)
    rank=models.IntegerField(default=0)
    # ...
    def __str__(self):              # __unicode__ on Python 2
        return self.topic