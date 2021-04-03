from django.db import models
from django.conf import settings
from django.utils import timezone


# We're creating a Post class that inherits from Model
class Post(models.Model):
    """Creating a Django model, post."""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """publishes an article/post"""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """renders the class in string format"""
        return self.title

