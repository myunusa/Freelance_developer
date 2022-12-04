from django import forms
from .models import FeedBack,Book_Project

class Feedback (forms.ModelForm):
    class Meta:
        model = FeedBack

        fields={
            'name', 'email',
            'subject', 'message'
        }

class Bookform (forms.ModelForm):
    class Meta:
        model = Book_Project

        fields={
            'name', 'email','phone',
            'topic', 'description'
        }
