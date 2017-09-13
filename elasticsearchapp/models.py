from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .search import BlogPostIndex

# Create your models here.

# Blogpost to be indexed into ElasticSearch


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogpost')
    posted_date = models.DateField(default=timezone.now)
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=1000)

    # Method for indexing the model
    def indexing(self):
        obj = BlogPostIndex(
            meta={'id': self.id},
            author=self.author.username,
            posted_date=self.posted_date,
            title=self.title,
            text=self.text
        )
        obj.save()
        return obj.to_dict(include_meta=True)
