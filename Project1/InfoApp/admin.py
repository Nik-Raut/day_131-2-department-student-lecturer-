

from django.contrib import admin
from .models import *

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id','dept_name']

admin.site.register(Department,DepartmentAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','user','Stu_name','Roll_No','Marks','department']


admin.site.register(Student, StudentAdmin)


class LecturerAdmin(admin.ModelAdmin):
    list_display = ['id','Lecturer_name','Lecturer_subject','multiple_dept_of_lectuer']


admin.site.register(Lecturer, LecturerAdmin)



