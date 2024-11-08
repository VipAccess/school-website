from django.urls import path
from .views import create_page, edit_page, news, page

urlpatterns = [
    path('news', news, name='news'),
    path('news/<slug:slug>', page, name='page'),
    path('create', create_page, name='create_page'),
    path('edit/<int:page_id>', edit_page, name='edit_page'),
]