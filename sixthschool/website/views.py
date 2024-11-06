from django.shortcuts import render, get_object_or_404, redirect

from .forms import QuestionsForm, RequestsForAdmissionForm
from .models import Teachers, Licenses, Documents, Awards, Contacts

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


