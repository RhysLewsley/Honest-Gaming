from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import GamePost

# Create your views here.
def home(request):
    posts = GamePost.objects.select_related('created_by').all()
    query = request.GET.get('q', '')
    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(synopsis__icontains=query))
    return render(request, 'home/index.html', {"posts": posts})

def game_detail(request, slug):
    """
    Display details for a single game using its slug with reviews.
    """
    game = get_object_or_404(GamePost, slug=slug)
    reviews = game.reviews.all()  # Get all reviews for this game
    # Determine if the logged-in user has already reviewed this game
    has_review = False
    if request.user.is_authenticated:
        has_review = reviews.filter(created_by=request.user).exists()

    context = {
        'game': game,
        'reviews': reviews,
        'has_review': has_review,
    }
    return render(request, 'gamepost/game_detail.html', context)