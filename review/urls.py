from django.urls import path
from . import views

urlpatterns = [
    path('game/<slug:slug>/review/', views.create_review, name='create-review'),
    path('game/<slug:slug>/reviews/', views.review_list, name='review-list'),
    path('game/<slug:slug>/review/<int:review_id>/delete/', views.delete_review, name='delete-review'),
]
