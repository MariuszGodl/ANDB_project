from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction, IntegrityError
from django.conf import settings
import os

from .models import Student, Application, Supportingdocument, Auditlog


def homepage(request):
    return render(request, 'homepage.html')


def scholarships(request):
    return render(request, 'scholarships.html')


def contact(request):
    return render(request, 'contact.html')


def apply(request):
    print(">>> apply view called, method =", request.method)

    if request.method == 'POST':
        print(">>> POST:", request.POST)
        print(">>> FILES:", request.FILES)

        try:
            with transaction.atomic():
                # 1. Student
                student = Student.objects.create(
                    firstname=request.POST.get('first_name'),
                    lastname=request.POST.get('last_name'),
                    email=request.POST.get('email'),
                    phoneno=request.POST.get('phone_no') or None,
                    dateofbirth=request.POST.get('date_of_birth'),
                    address=request.POST.get('address'),
                )
                print(">>> Student created:", student.studentid)

                # 2. Application
                application = Application.objects.create(
                    studentid=student,
                    status='Submitted',
                    academicyear=int(request.POST.get('academic_year')),
                    gpa=float(request.POST.get('gpa')),
                    essaytext=request.POST.get('essay_text'),
                )
                print(">>> Application created:", application.applicationid)

                # 3. Supportingdocument – plik (opcjonalnie)
                if 'document' in request.FILES and request.FILES['document']:
                    document_file = request.FILES['document']
                    print(">>> Document received:", document_file.name)

                    upload_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
                    os.makedirs(upload_dir, exist_ok=True)

                    disk_path = os.path.join(upload_dir, document_file.name)
                    with open(disk_path, 'wb+') as destination:
                        for chunk in document_file.chunks():
                            destination.write(chunk)

                    Supportingdocument.objects.create(
                        applicationid=application,
                        filename=document_file.name,
                        filepath=os.path.join('uploads', document_file.name),
                        filetype=document_file.content_type,
                        filesizekb=document_file.size // 1024,
                    )

                # 4. Auditlog
                Auditlog.objects.create(
                    eventtype='Application Submitted',
                    details=f'Student ID: {student.studentid}, Application ID: {application.applicationid}',
                )

                # Przekierowanie na stronę sukcesu (bez ID)
                return redirect('success')

        except IntegrityError:
            messages.error(request, 'Error: this email already exists in the database.')
        except ValueError:
            messages.error(request, 'Data error: check GPA and academic year.')
        except Exception as e:
            print(">>> ERROR in apply:", e)
            messages.error(request, f'Unexpected error: {e}')

    return render(request, 'apply.html')


def success(request):
    return render(request, 'success.html')
