from django.shortcuts import render, get_object_or_404
from .models import GamePost

# Create your views here.
def home(request):
    posts = GamePost.objects.select_related('created_by').all()
    return render(request, 'home/index.html', {"posts": posts})

def game_detail(request, slug):
    """
    Display details for a single game using its slug.
    """
    game = get_object_or_404(GamePost, slug=slug)
    return render(request, 'gamepost/game_detail.html', {"game": game})