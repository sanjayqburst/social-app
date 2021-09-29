from dashboard import dashboard_urls
from django.urls import path
from django.urls.conf import include
from . import views
import dashboard


urlpatterns=[
    path('',include(dashboard_urls)),
]