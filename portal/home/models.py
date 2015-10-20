from django.db import models


class TopTrends(models.Model):
    topic = models.CharField(max_length=200)
    rank=models.IntegerField(default=0)
    # ...
    def __unicode__(self):              # __str__ on Python 3
        return self.topic