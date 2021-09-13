from django.contrib.auth.models import User
from django.db import models

dept_choices=(('mech','MECH'),
              ('civil','CIVIL'),
              ('it','IT'),
              ('computer','COMPUTER'))


class Department(models.Model):
    dept_name = models.CharField(max_length=50, choices=dept_choices)

    def __str__(self):
        return self.dept_name


class Student(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

    Roll_No=models.IntegerField()
    Stu_name=models.CharField(max_length=50)
    Marks=models.IntegerField()

    def __str__(self):
        return self.Stu_name




class Lecturer(models.Model):
    department = models.ManyToManyField(Department)

    Lecturer_name = models.CharField(max_length=30)
    Lecturer_subject=models.CharField(max_length=30)


    def multiple_dept_of_lectuer(self):
        return ",".join([str(x) for x in self.department.all()])

    def __str__(self):
        return self.Lecturer_name





