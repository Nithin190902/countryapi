# myapp/urls.py
from django.urls import path
from .views import CountryList

urlpatterns = [
    path('items/', CountryList.as_view(), name='item-list'),
]
