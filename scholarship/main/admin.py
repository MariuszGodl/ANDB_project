from django.contrib import admin
from .models import Student, Application, Supportingdocument, Auditlog


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("studentid", "firstname", "lastname", "email")


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("applicationid", "studentid", "status", "academicyear", "gpa")


@admin.register(Supportingdocument)
class SupportingDocumentAdmin(admin.ModelAdmin):
    list_display = ("documentid", "applicationid", "filename", "filetype", "filesizekb")


@admin.register(Auditlog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ("logid", "timestamp", "eventtype")
