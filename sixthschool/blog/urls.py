from django.urls import path
from .views import news, page

urlpatterns = [
    path('news', news, name='news'),
    path('news/<slug:slug>', page, name='page'),
]