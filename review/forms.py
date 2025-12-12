from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    # Generate rating choices: 0.00, 0.25, 0.50, ..., 5.00
    RATING_CHOICES = [(round(i * 0.25, 2), f"{round(i * 0.25, 2):.2f} ★") for i in range(21)]
    
    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Rating',
        help_text='Select a rating from 0.00 to 5.00'
    )
    
    class Meta:
        model = Review
        fields = ['review_text', 'rating']
        widgets = {
            'review_text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Share your thoughts about this game...'
            }),
        }
        labels = {
            'review_text': 'Your Review',
        }
