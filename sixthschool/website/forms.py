from django import forms
from .models import Questions, RequestsForAdmission

class QuestionsForm(forms.ModelForm):
    CATEGORY_CHOICES = (
    ('1','Общие вопросы'),
    ('2','Платные услуги'),
    ('3','Поступление'),
    ('4','Питание'),
    )

    class Meta:
        model = Questions
        fields = ['category', 'text', 'email']

class RequestsForAdmissionForm(forms.ModelForm):
    class Meta:
        model = RequestsForAdmission
        fields = ['student_name', 'birth_certificate', 'parents_name', 'passport_details', 'file', 'phone',
                  'school_class']

