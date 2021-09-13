from django import forms
from .models import *



class StudntForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        labels = {
            'department': 'Department Name',
            'Stu_name': 'Student Name',
            'Roll_No': 'Student Roll No.',
            'Marks': 'Student Marks'
        }

class DepartmentForm(forms.ModelForm):
    class Meta:
        model=Department
        fields='__all__'
        labels = {
            "dept_name": "Department Name"
        }


class LecturerForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = '__all__'
        '''
        widgets = {
            'department': forms.CheckboxSelectMultiple()
        }
        labels = {
            'department': 'Department Name',
            'Lecturer_name': 'Lecturer Name',
            'Lecturer_subject': 'Lecturer Subject'
        }
        '''
