from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models import Avg

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

    def get_average_rating(self):
        """Calculate average rating for this game"""
        avg = self.reviews.aggregate(Avg('rating'))['rating__avg']
        return round(avg, 1) if avg else 0

    def get_rating_count(self):
        """Get number of ratings for this game"""
        return self.reviews.count()

    def __str__(self):
        return self.title


class Rating(models.Model):
    """
    Model for user ratings on game posts.
    """
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
    
    game = models.ForeignKey(GamePost, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('game', 'user')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.game.title} ({self.rating}/5)"