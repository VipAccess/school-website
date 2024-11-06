from django.urls import path
from .views import create_page, edit_page, news

urlpatterns = [
    path('news', news, name='news'),
    # path('teacher/<int:teacher_id>', teacher, name='teacher'),
    path('create', create_page, name='create_page'),
    path('edit/<int:page_id>', edit_page, name='edit_page'),
]