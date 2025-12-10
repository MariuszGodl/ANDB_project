from django import forms

class ScholarshipApplicationForm(forms.Form):
    first_name = forms.CharField(label="Imię", max_length=100)
    last_name = forms.CharField(label="Nazwisko", max_length=100)
    email = forms.EmailField(label="Email", max_length=255)
    phone_no = forms.CharField(label="Telefon", max_length=20, required=False)
    date_of_birth = forms.DateField(label="Data urodzenia", widget=forms.DateInput(attrs={"type": "date"}))
    address = forms.CharField(label="Adres", max_length=255)
    academic_year = forms.IntegerField(label="Rok akademicki")
    gpa = forms.DecimalField(label="GPA", max_digits=3, decimal_places=2, min_value=0, max_value=5)
    essay_text = forms.CharField(label="Esej", widget=forms.Textarea)
