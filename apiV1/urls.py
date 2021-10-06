from django.urls import path
from .views import CommentView, ContentView

urlpatterns = [
    path('comment',CommentView.as_view(),name='comment'),
    path('content',ContentView.as_view()),
]
