from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog_Post(models.Model):
    image = models.ImageField(upload_to='image', null=True, blank=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(unique=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_on', )

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog_Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    body = models.TextField()
    created = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created', )

    def __str__(self):
        return f"Comment by {self.name} on {self.blog}"