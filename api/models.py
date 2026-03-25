from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,blank=True, null=True,related_name='courses')

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='enrollments')
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} enrolled in {self.course.name}"
