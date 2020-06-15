from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, request
from datetime import date
from forms.models import student_info, subjects
from forms.forms import SubjectsForm

def exam(request):
    batch_year = reversed(range(date.today().year-10+58, date.today().year+58)) #range = 10 years before from today ad to bs = add 58 years
    exam_year= reversed(range(date.today().year+57, date.today().year + 1+58))

    #sub collects all the subjects attributes to pass it in javascript of template file
    subject = subjects.objects.all()


    return render(request, '../templates/index.html', {"range_year": exam_year, "cur_year" : batch_year, "subject": subject })



def addDetail(request):
    new_student_info = student_info(
        year = request.POST['Year'],
        faculty = request.POST['Faculty'],
        batch = request.POST['Batch'],
        college = request.POST['College'],
        firstName = request.POST['First_name'],
        lastName = request.POST['Last_name'],
        gender = request.POST['Gender'],
        phone = request.POST['Phone'],
        tu_registraion_number = request.POST['Tu_registration_number'],
        semester = request.POST['Semester'],
    )

    new_student_info.save()

    return HttpResponseRedirect('//')

def subjectForm(request):
#    form = Subject_Form()

    subject = subjects.objects.all()
    form = SubjectsForm()
    return render(request, '../templates/subjects.html',{"subject": subject, "form":form })

def addSubject(request):
    if request.method == 'POST':
        form_data = SubjectsForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponseRedirect('/subjectForm/')
    else:
        form = SubjectsForm()
    return HttpResponseRedirect('/subjectForm/')
