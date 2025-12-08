from django.contrib import admin
from .models import Student, Application, Supportingdocument, Auditlog

# Register your models here.
admin.site.register(Student)
admin.site.register(Application)
admin.site.register(Supportingdocument)
admin.site.register(Auditlog)