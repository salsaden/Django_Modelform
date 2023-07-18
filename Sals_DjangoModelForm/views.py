from django.shortcuts import render
from Sals_DjangoModelForm.forms import EmpForm


def home(request):

    stud = EmpForm()
    return render(request, 'index.html', {'form':stud})
