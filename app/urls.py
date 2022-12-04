from django.urls import path
from .views import Index, About, feed_back, Members, book_project

urlpatterns =[
    path('', Index, name="index"),
    path('about/', About, name="about"),
    path('members/', Members, name="member"),
    path('feedback/', feed_back, name="feedback"),
    path('bookproject/', book_project, name="project"),
]