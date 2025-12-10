from django.db import models

class Student(models.Model):
    studentid = models.AutoField(db_column='StudentID', primary_key=True)
    firstname = models.CharField(db_column='FirstName', max_length=100)
    lastname = models.CharField(db_column='LastName', max_length=100)
    email = models.EmailField(db_column='Email', max_length=255, unique=True)
    phoneno = models.CharField(db_column='PhoneNo', max_length=20, blank=True, null=True)
    dateofbirth = models.DateField(db_column='DateOfBirth')
    address = models.CharField(db_column='Address', max_length=255)
    createdat = models.DateTimeField(db_column='CreatedAt', auto_now_add=True)

    class Meta:
        db_table = 'Student'


class Application(models.Model):
    applicationid = models.AutoField(db_column='ApplicationID', primary_key=True)
    student = models.ForeignKey(Student, db_column='StudentID', on_delete=models.CASCADE)
    status = models.CharField(db_column='Status', max_length=50, default='Draft')
    academicyear = models.IntegerField(db_column='AcademicYear')
    gpa = models.DecimalField(db_column='GPA', max_digits=3, decimal_places=2)
    essaytext = models.TextField(db_column='EssayText')
    applicationdate = models.DateTimeField(db_column='ApplicationDate', auto_now_add=True)

    class Meta:
        db_table = 'Application'
