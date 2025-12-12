from django.shortcuts import render, get_object_or_404
from .models import GamePost

# Create your views here.
def home(request):
    posts = GamePost.objects.select_related('created_by').all()
    return render(request, 'home/index.html', {"posts": posts})

def game_detail(request, slug):
    """
    Display details for a single game using its slug with reviews.
    """
    game = get_object_or_404(GamePost, slug=slug)
    reviews = game.reviews.all()  # Get all reviews for this game
    
    context = {
        'game': game,
        'reviews': reviews,
    }
    return render(request, 'gamepost/game_detail.html', context)