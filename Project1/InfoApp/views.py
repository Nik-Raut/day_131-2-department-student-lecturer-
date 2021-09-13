from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *



def homeview(request):
    template_name='InfoApp/base.html'
    context={}
    return render(request,template_name,context)



@login_required(login_url='login')
def studentview(request):
    form=StudntForm()
    if request.method=='POST':
        form=StudntForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lecturer')
    template_name='InfoApp/student.html'
    context={'form':form}
    return render(request,template_name,context)

@login_required(login_url='login')
def lecturerview(request):
    form = LecturerForm()
    if request.method == 'POST':
        form = LecturerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    template_name = 'InfoApp/lecturer.html'
    context = {'form': form}
    return render(request, template_name, context)
'''
@login_required(login_url='login')
def departmentview(request):
    form = DepartmentForm()
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student')
    template_name = 'InfoApp/department.html'
    context = {'form': form}
    return render(request, template_name, context)
'''

def stdentlistview(request):
    template_name = 'InfoApp/studentsINFO.html'
    all_stu= Student.objects.all()
    context = {'all_stu': all_stu}
    return render(request, template_name, context)

#show all view

def showallstudentsview(request):
    all_students=Student.objects.all()
    context = {'all_students': all_students}
    template_name = 'InfoApp/showallstudents.html'
    return render(request, template_name, context)

def showalllecturersview(request):
    all_lecturers=Lecturer.objects.all()
    context = {'all_lecturers': all_lecturers}
    template_name = 'InfoApp/showalllecturers.html'
    return render(request, template_name, context)


def showallldepartmentview(request):
    all_departments=Department.objects.all()
    context = {'all_departments': all_departments}
    template_name = 'InfoApp/showalldepartments.html'
    return render(request, template_name, context)
#------------------------------------------------------------------------------------------------

#delete views

@login_required(login_url='login')
def studentdeleteview(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('showallstudents')


@login_required(login_url='login')
def lecturerdeleteview(request,id):
    lecturer=Lecturer.objects.get(id=id)
    lecturer.delete()
    return redirect('showalllecturers')
#------------------------------------------------------------------------------------------------

#update views
@login_required(login_url='login')
def studentupdateview(request,id):
    student = Student.objects.get(id=id)
    form=StudntForm(instance=student)

    if request.method=='POST':
        form=StudntForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('showallstudents')
    template_name = 'InfoApp/student.html'
    context={'form':form}
    return render(request, template_name, context)

@login_required(login_url='login')
def lecturerupdateview(request,id):
    lecturer = Lecturer.objects.get(id=id)
    form=LecturerForm(instance=lecturer)

    if request.method=='POST':
        form=LecturerForm(request.POST,instance=lecturer)
        if form.is_valid():
            form.save()
            redirect('showalllecturers')
    template_name = 'InfoApp/lecturer.html'
    context={'form':form}
    return render(request, template_name, context)
#------------------------------------------------------------------------------------------------


def infoview(request):

    if request.method=='GET':
        context = {}
        template_name = 'InfoApp/getINFO.html'
        return render(request, template_name, context)

    elif request.method=='POST':
        DN=request.POST.get('dn')
        data=Student.objects.filter(department__dept_name=DN)
        context = {'data': data}
        template_name = 'InfoApp/a.html'
        return render(request, template_name, context)

def searchstudentview(request):
    context={}
    if request.method=='POST':
        '''
        SN=request.POST.get('sn')
        SRN = request.POST.get('srn')
        SMK = request.POST.get('smk')
        SDPT = request.POST.get('sdpt')
        '''

        stu_obj = Student.objects.filter(Stu_name=request.POST.get('sn'))|Student.objects.filter(Marks=request.POST.get('smk'))|Student.objects.filter(Roll_No=request.POST.get('srn'))|Student.objects.filter(department__dept_name=request.POST.get('sdpt'))
        #print('stduent type:',type(stu_obj),'student name:',stu_obj)
        context={'stu_obj':stu_obj}
        template_name = 'InfoApp/searchedstudents.html'
        return render(request, template_name, context)

    template_name='InfoApp/searchstudent.html'
    return render(request,template_name,context)

def searchlecturerview(request):
    context={}
    if request.method=='POST':
        '''
        LN=request.POST.get('ln')
        LS = request.POST.get('ls')
        LD = request.POST.get('ld')
        '''

        lect_obj = Lecturer.objects.filter(Lecturer_name=request.POST.get('ln'))|Lecturer.objects.filter(Lecturer_subject=request.POST.get('ls'))|Lecturer.objects.filter(department__dept_name=request.POST.get('ld'))
        print('lecturer type:',type(lect_obj),'lecturer name:',lect_obj)
        context={'lect_obj':lect_obj}
        template_name = 'InfoApp/searchedlecturers.html'
        return render(request, template_name, context)

    template_name='InfoApp/searchlecturer.html'
    return render(request,template_name,context)



