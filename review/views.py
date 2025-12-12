from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from gamepost.models import GamePost
from .models import Review
from .forms import ReviewForm


@login_required(login_url='login')
@require_http_methods(["GET", "POST"])
def create_review(request, slug):
    """Create or update a review for a specific game"""
    game = get_object_or_404(GamePost, slug=slug)
    
    # Check if user already has a review for this game
    try:
        review = Review.objects.get(game=game, created_by=request.user)
        is_update = True
    except Review.DoesNotExist:
        review = None
        is_update = False
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.game = game
            review.created_by = request.user
            review.save()
            if is_update:
                messages.success(request, 'Your review has been updated.')
            else:
                messages.success(request, 'Your review has been submitted.')
            return redirect('game-detail', slug=slug)
    else:
        form = ReviewForm(instance=review)
    
    context = {
        'form': form,
        'game': game,
        'is_update': is_update,
    }
    return render(request, 'review/review_form.html', context)


@require_http_methods(["GET"])
def review_list(request, slug):
    """Get reviews for a game (for AJAX or template inclusion)"""
    game = get_object_or_404(GamePost, slug=slug)
    reviews = game.reviews.all()  # Uses related_name from Review model
    
    context = {
        'reviews': reviews,
        'game': game,
    }
    return render(request, 'review/review_list.html', context)


@login_required(login_url='login')
@require_http_methods(["POST"])
def delete_review(request, slug, review_id):
    """Delete a review (only the creator can delete it)"""
    game = get_object_or_404(GamePost, slug=slug)
    review = get_object_or_404(Review, id=review_id, game=game)
    
    # Only allow the creator to delete
    if review.created_by != request.user:
        return redirect('game-detail', slug=slug)
    
    review.delete()
    return redirect('game-detail', slug=slug)
