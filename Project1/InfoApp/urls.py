from django.urls import path
from .views import *
urlpatterns=[
    path('home/',homeview,name='home'),
    path('student/',studentview,name='student'),
    path('lecturer/',lecturerview,name='lecturer'),
    path('showallstudents/',showallstudentsview,name='showallstudents'),
    path('showalllecturers/',showalllecturersview,name='showalllecturers'),
    path('showallldepartment/', showallldepartmentview, name='showallldepartment'),

    #delete views
    path('deletestudent/<int:id>', studentdeleteview, name='deletestudent'),
    path('deletelecturer/<int:id>', lecturerdeleteview, name='deletelecturer'),

    #update views
    path('updatestudent/<int:id>', studentupdateview, name='updatestudent'),
    path('updatelecturer/<int:id>', lecturerupdateview, name='updatelecturer'),


    #search views

    path('searchstudent/', searchstudentview, name='searchstudent'),
    path('searchlecturer/', searchlecturerview, name='searchlecturer'),



]