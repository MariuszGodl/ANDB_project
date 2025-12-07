from django.shortcuts import render

def index(request):
    return render(request, 'homepage.html')

def apply(request):
    if request.method == 'POST':
        pass 
    return render(request, 'apply.html')