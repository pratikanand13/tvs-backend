from django.urls import path
from .views import pageone, pagetwo

urlpatterns = [
    path('local/', pageone.as_view(), name='local'),
    path('global/', pagetwo.as_view(), name='global'),
 ]
