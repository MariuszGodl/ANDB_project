from django.shortcuts import render
from django.db import transaction
from .forms import ScholarshipApplicationForm
from .models import Student, Application
from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')

def scholarships(request):
    return render(request, 'scholarships.html')

def contact(request):
    return render(request, 'contact.html')

def apply(request):
    # Check if the form was submitted (POST request)
    if request.method == 'POST':
        
        # 1. Collect the data using the 'name' attributes from your HTML inputs
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        gpa = request.POST.get('gpa')
        statement = request.POST.get('statement')

        # 2. Print the values to your TERMINAL (Console)
        print(f"Name:      {full_name}")
        print(f"Email:     {email}")
        print(f"GPA:       {gpa}")
        print(f"Statement: {statement}")

        # 3. Return the page with a success message
        return render(request, 'apply.html', {'success': True})

    # If it's a GET request (just viewing the page), render the form normally
    return render(request, 'apply.html')



@transaction.atomic
def scholarship_application_view(request):
    if request.method == "POST":
        form = ScholarshipApplicationForm(request.POST)
        if form.is_valid():
            student, created = Student.objects.get_or_create(
                email=form.cleaned_data["email"],
                defaults={
                    "firstname": form.cleaned_data["first_name"],
                    "lastname": form.cleaned_data["last_name"],
                    "phoneno": form.cleaned_data.get("phone_no"),
                    "dateofbirth": form.cleaned_data["date_of_birth"],
                    "address": form.cleaned_data["address"],
                },
            )

            if not created:
                student.firstname = form.cleaned_data["first_name"]
                student.lastname = form.cleaned_data["last_name"]
                student.phoneno = form.cleaned_data.get("phone_no")
                student.dateofbirth = form.cleaned_data["date_of_birth"]
                student.address = form.cleaned_data["address"]
                student.save()

            application = Application.objects.create(
                studentid=student,
                status='Submitted',
                academicyear=form.cleaned_data["academic_year"],
                gpa=form.cleaned_data["gpa"],
                essaytext=form.cleaned_data["essay_text"],
            )

            return render(request, "scholarship/success.html", {"application_id": application.applicationid})
    else:
        form = ScholarshipApplicationForm()

    return render(request, "scholarship/application_form.html", {"form": form})
