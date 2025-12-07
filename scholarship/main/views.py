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