from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class BlogPost(models.Model):
    author = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    content = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/blog/{self.slug}"