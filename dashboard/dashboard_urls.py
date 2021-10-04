from django.urls import path
from . import views
import dashboard

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    # path('dashboard_create', dashboard.views.createComment,name='dashboard_create'),
    path('post/', views.AddPost.as_view(), name='addpost'),
]
