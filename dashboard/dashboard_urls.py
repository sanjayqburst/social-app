from django.urls import path
from . import views

urlpatterns = [
    path('',views.DashboardView.as_view(),name='dashboard'),
    path('post/',views.AddPost.as_view(),name='addpost'),
]
