from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('university', views.university_list),
    path('university/<int:id>', views.get_university),
    path('university/create', views.create_university),
    path('university/change/<int:id>', views.update_university),
    path('university/delete/<int:id>', views.delete_university),
    path('student', views.student_list),
    path('student/<int:id>', views.get_student),
    path('student/create', views.create_student),
    path('student/change/<int:id>', views.update_student),
    path('student/delete/<int:id>', views.delete_student),
]