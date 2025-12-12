from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class GamePost(models.Model):
    """
    Model for a game post with title, slug, image, synopsis, and creation metadata.
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    gameimage = CloudinaryField('image', folder='gamepost/')
    synopsis = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='game_posts')

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title