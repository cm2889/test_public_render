from django.urls import path

from . import views

urlpatterns = [
   path('students/', views.StudentListView.as_view(), name='student-list'),
   path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),
   path ('subjects/', views.SubjectListView.as_view(), name='subject-list'),
   path('subjects/<int:pk>/', views.SubjectDetailView.as_view(), name='subject-detail'),
   path('teachers/', views.TeacherListView.as_view(), name='teacher-list'),
    path('teachers/<int:pk>/', views.TeacherDetailView.as_view(), name='teacher-detail'),
    path('courses/', views.CourseListView.as_view(), name='course-list'),
    path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('enrollments/', views.EnrollmentListView.as_view(), name='enrollment-list'),
    path('enrollments/<int:pk>/', views.EnrollmentDetailView.as_view(), name='enrollment-detail'),

]