from django import forms
from .models import FeedBack, ContactUs

class ContactForm (forms.ModelForm):
    class Meta:
        model = ContactUs
        fields='__all__'

class Feedback (forms.ModelForm):
    class Meta:
        model = FeedBack

        fields={
            'name', 'email',
            'subject', 'message'
        }