from django import forms

from main.models import Student

from main.models import Subject


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class StudentForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'avatar', 'email',)

    def clean_email(self):
        cleaned_data = self.cleaned_data['email']
        if 'sky.pro' not in cleaned_data:
            raise forms.ValidationError('Please enter a valid email address.')
        return cleaned_data


class SubjectForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
