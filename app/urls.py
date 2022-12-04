from django.urls import path
from .views import Index, About, feed_back,contact_view, Members

urlpatterns =[
    path('', Index, name="index"),
    path('about/', About, name="about"),
    path('members/', Members, name="member"),
    path('contact/', contact_view, name="contact"),
    path('feedback/', feed_back, name="feedback"),
]