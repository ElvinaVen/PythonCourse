from django import forms

from main.models import Student

from main.models import Subject


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'avatar')


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
