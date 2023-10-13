from django.urls import path
from .views import pageone, Check

urlpatterns = [
    path('local/', pageone.as_view(), name='langing'),
    path('global/', Check.as_view(), name='ck'),
 ]
