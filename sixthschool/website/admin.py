from django.contrib import admin
from .models import Teachers, Disciplines, Questions, Contacts, RequestsForAdmission, Documents, Licenses, Awards

@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'photo', 'position', 'education_level', 'qualification', 'degree',
                    'academic_rank', 'advanced_training_info', 'professional_retraining_info',
                    'experience', 'contact_phone', 'email', 'educational_programs', 'get_discipline']

@admin.register(Disciplines)
class DisciplinesAdmin(admin.ModelAdmin):
    list_display = ['discipline_id', 'discipline_name']

@admin.register(Awards)
class AwardsAdmin(admin.ModelAdmin):
    list_display = ['award_name', 'photo', 'info', 'is_published']

@admin.register(Licenses)
class LicensesAdmin(admin.ModelAdmin):
    list_display = ['licenses_name', 'photo', 'info', 'is_published']

@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    list_display = ['document_name', 'category', 'file', 'info', 'is_published']

@admin.register(RequestsForAdmission)
class RequestsForAdmissionAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'parents_name', 'file', 'phone', 'passport_details', 'date_of_request',
                    'status']

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'position', 'email', 'phone']

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['question_id', 'category', 'text', 'email', 'date', 'status']

