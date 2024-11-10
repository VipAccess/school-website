from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

import zipfile
import os

from unicodedata import category

from .forms import QuestionsForm, RequestsForAdmissionForm
from .models import Teachers, Licenses, Documents, Awards, Contacts, RequestsForAdmission, Questions


def teachers(request):
    data = Teachers.objects.all()
    return render(request, 'website/teachers.html', {"teachers": data})


def teacher(request, teacher_id):
    data = get_object_or_404(Teachers, pk=teacher_id)
    return render(request, 'website/teacher.html', {'teacher': data})


def awards(request):
    data = Awards.objects.all()
    return render(request, 'website/awards.html', {"awards": data})


def licenses(request):
    data = Licenses.objects.all()
    return render(request, 'website/licenses.html', {"licenses": data})


def documents(request):
    data = Documents.objects.all()
    return render(request, 'website/documents.html', {"documents": data})


def requests_for_admission(request):
    if request.method == 'POST':
        form = RequestsForAdmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news')
    else:
        form = RequestsForAdmissionForm()
    data = {'form': form}
    return render(request, 'website/request_for_admission.html', data)


def questions(request):
    if request.method == 'POST':
        form = QuestionsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
    else:
        form = QuestionsForm()
    data = {'form': form}
    return render(request, 'website/ask_a_question.html', data)


def contacts(request):
    data = Contacts.objects.all()
    return render(request, 'website/contacts.html', {"contacts": data})


def download_requests(request):
    # Создаем временный файл для архива
    zip_filename = 'requests.zip'
    response = HttpResponse(content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename={zip_filename}'

    with zipfile.ZipFile(response, 'w') as zip_file:
        # Получаем данные из модели
        data = RequestsForAdmission.objects.all()

        for obj in data:
            folder_name = f'{obj.student_name}'  # Имя папки для записи
            zip_file.writestr(f'{folder_name}/', b'')  # Создаем пустую папку
            # Создаем текстовый файл для каждого объекта
            file_name = f'{folder_name}/{obj.request_id}.txt'
            file_content = f"""ID: {obj.request_id};
            Ф.И.О студента: {obj.student_name};
            Ф.И.О родителя{obj.parents_name};
            Телефон: {obj.phone};
            Класс: {obj.school_class}
            Дата заявки: {obj.date_of_request}"""
            zip_file.writestr(file_name, file_content)

            if obj.birth_certificate:
                path = obj.birth_certificate.path
                zip_file.write(path, os.path.join(folder_name, os.path.basename(path)))

            if obj.passport_details:
                path = obj.passport_details.path
                zip_file.write(path, os.path.join(folder_name, os.path.basename(path)))

            if obj.file:
                path = obj.file.path
                zip_file.write(path, os.path.join(folder_name, os.path.basename(path)))

    return response

def download_questions(request):
    # Создаем временный файл для архива
    zip_filename = 'questions.zip'
    response = HttpResponse(content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename={zip_filename}'

    with zipfile.ZipFile(response, 'w') as zip_file:
        # Получаем данные из модели
        data = Questions.objects.all()

        for obj in data:
            # Создаем текстовый файл для каждого объекта
            file_name = f'{obj.question_id}.txt'
            file_content = f'ID: {obj.question_id};\nКатегория: {obj.category};\nВопрос: {obj.text};\nemail: {obj.email};\nДата: {obj.date}'
            zip_file.writestr(file_name, file_content)

    return response
