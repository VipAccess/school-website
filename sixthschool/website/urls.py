from django.urls import path
from .views import teacher, teachers, documents, requests_for_admission, questions, awards, licenses, contacts
from .views import download_questions, download_requests

urlpatterns = [
    path('teachers', teachers, name='teachers'),
    path('teacher/<int:teacher_id>', teacher, name='teacher'),
    path('documents', documents, name='documents'),
    path('awards', awards, name='awards'),
    path('licenses', licenses, name='licenses'),
    path('ask_a_question', questions, name='ask_a_question'),
    path('request_for_admission', requests_for_admission, name='request_for_admission'),
    path('contacts', contacts, name='contacts'),
    path('download_questions', download_questions, name='download_questions'),
    path('download_requests', download_requests, name='download_requests'),
]