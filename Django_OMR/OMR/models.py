from django.db import models

# Create your models here.
class Department(models.Model):
    department= models.CharField(max_length=2000)
    
    def __str__(self) -> str:
        return self.department
    
    class Meta:
        ordering= ['department']

class StudentID(models.Model):
    student_id= models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.student_id
    
class Subject(models.Model):
    subject_name = models.CharField(max_length=2000)

    def __str__(self) -> str:
        return self.subject_name


class Student(models.Model):
    department= models.ForeignKey(Department, related_name="depart", on_delete=models.CASCADE)
    student_id= models.OneToOneField(StudentID, related_name="stud_id", on_delete=models.CASCADE)
    student_name= models.CharField(max_length=200)
    student_age = models.IntegerField()
    student_contact= models.IntegerField()
    student_email= models.EmailField(unique=True)
    student_address= models.IntegerField()

    def __str__(self) -> str:
        return self.student_name
    
    class Meta:
        ordering= ['student_name']
        verbose_name="student"

class SubjectMarks(models.Model):
    student = models.ForeignKey(Student, related_name="studentmarks", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.student.student_name} {self.subject.subject_name }"
    class Meta:
        unique_together=['student', 'subject']

class ReportCards(models.Model):
    student = models.ForeignKey(Student, related_name="reportcards", on_delete=models.CASCADE)
    student_rank= models.IntegerField()
    date_of_report_card_generation= models.DateField(auto_now_add=True)

    class Meta:
        unique_together=['student_rank', 'date_of_report_card_generation']


