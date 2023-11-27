from django.contrib import admin
from .models import University, Student

class UniversityAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'name', 
        'short_name', 
        'create_date'
    )
admin.site.register(University, UniversityAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'firstname',
        'lastname',
        'patronymic',
        'birthdate',
        'university',
        'entrance_date'
    )
admin.site.register(Student, StudentAdmin)
