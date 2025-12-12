from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from gamepost.models import GamePost


class Review(models.Model):
    """Model for game reviews"""
    game = models.ForeignKey(GamePost, on_delete=models.CASCADE, related_name='reviews')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(5.00)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['game', 'created_by']  # One review per user per game
    
    def __str__(self):
        return f"{self.created_by.username}'s review of {self.game.title} - {self.rating}★"
