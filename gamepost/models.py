from django.db import models

# Create your models here.
class gamepost(models.Model):
    """
    Model to represent a game post with title, slug, image URL, synopsis, and creation date.
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    gameimage = models.URLField()
    synopsis = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + self.gameimage + self.synopsis