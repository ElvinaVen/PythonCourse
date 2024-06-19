from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse

from main.models import Student
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class StudentListView(ListView):
    model = Student


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        print(f'{name} : {message}')
    context = {
        'title': "Контакты"
    }
    return render(request, 'main/contact.html', context)


def view_student(request):
    student = Student.objects.get(pk=pk)
    context = {"student": student}
    return render(request, "student_detail.html", context)


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    fields = ['first_name', 'last_name', 'avatar']
    success_url = reverse_lazy('main:index')

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['first_name', 'last_name', 'avatar']
    success_url = reverse_lazy('main:index')

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('main:index')

def toggle_active(request, pk):
    student_item = get_object_or_404(Student, pk=pk)
    if student_item.is_active:
        student_item.is_active = False
    else:
        student_item.is_active = True

    student_item.save()
    return redirect(reverse('main:index'))

