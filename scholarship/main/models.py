from django.db import models


class Student(models.Model):
    studentid = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=255)
    phoneno = models.CharField(max_length=20, blank=True, null=True)
    dateofbirth = models.DateField()
    address = models.CharField(max_length=255)
    createdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False            # bo tabele tworzysz SQL-em
        db_table = 'student'

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Application(models.Model):
    applicationid = models.AutoField(primary_key=True)
    studentid = models.ForeignKey(Student, models.DO_NOTHING, db_column='studentid')
    status = models.CharField(max_length=50)
    academicyear = models.IntegerField()
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    essaytext = models.TextField()
    applicationdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'application'


class Supportingdocument(models.Model):
    documentid = models.AutoField(primary_key=True)
    applicationid = models.ForeignKey(Application, models.DO_NOTHING, db_column='applicationid')
    filename = models.CharField(max_length=255)
    filepath = models.CharField(max_length=512)
    filetype = models.CharField(max_length=50)
    filesizekb = models.IntegerField()
    uploaddate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supportingdocument'


class Auditlog(models.Model):
    logid = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    eventtype = models.CharField(max_length=50)
    details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auditlog'
