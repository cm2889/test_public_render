from rest_framework import serializers

from .models import Subject, Student, Teacher, Course, Enrollment

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        #fields = '__all__'
        fields = ['id', 'name', 'is_active']



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        #fields = '__all__'
        fields = ['id', 'name', 'is_active', 'teacher']
class TeacherSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    class Meta:
        model = Teacher
        #fields = '__all__'
        fields = ['id', 'name', 'email', 'phone', 'is_active', 'courses']

class EnrollmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Enrollment
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    enrollments = EnrollmentSerializer(many=True, read_only=True)
    class Meta:
        model = Student
        #fields = '__all__'
        fields = ['id', 'name', 'email', 'phone', 'is_active', 'enrollments']