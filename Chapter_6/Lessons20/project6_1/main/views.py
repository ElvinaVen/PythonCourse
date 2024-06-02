from django.shortcuts import render

from main.models import Student


def index(request):
    students_list = Student.objects.all()
    context = {
        'object_list': students_list,
        'title': 'Главная',
    }
    return render(request, 'main/index.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        print(f'{name} : {message}')
    context = {
        'title': "Контакты"
    }
    return render(request, 'main/contact.html', context)
