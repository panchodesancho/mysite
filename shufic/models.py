from django.db import models
from datetime import datetime


class Video(models.Model):
    class Metha():
        db_table = "Vidoe"

    Video_url = models.URLField()
    Video_title = models.CharField(max_length = 200)
    Video_text = models.TextField()
    Video_likes = models.IntegerField(default=0)
    Video_date = models.DateTimeField(default= datetime.now, blank=True)

    def __str__(self):
        return self.Video_title


class Comment(models.Model):
    class Metha():
        db_table = "Comments"

    Comment_text = models.TextField()
    Comment_Video = models.ForeignKey(Video, on_delete=models.CASCADE)
# Create your models here.
