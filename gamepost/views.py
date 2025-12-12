from django.shortcuts import render
from .models import GamePost

# Create your views here.
def home(request):
    posts = GamePost.objects.select_related('created_by').all()
    return render(request, 'home/index.html', {"posts": posts})