from django.shortcuts import render

from main.models import Student
from django.views.generic import ListView, DetailView

class StudentListView(ListView):
    model = Student
    template_name = 'main/index.html'


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        print(f'{name} : {message}')
    context = {
        'title': "Контакты"
    }
    return render(request, 'main/contact.html', context)

class StudentDetailView(DetailView):
    model = Student
    template_name = 'main/student_detail.html'

