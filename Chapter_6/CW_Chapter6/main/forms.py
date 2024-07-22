# from django import forms
#
# from main.models import Newsletter
#
#
# class StyleFormMixin:
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'
#
#
# class StudentForm(StyleFormMixin, forms.ModelForm):
#
#     class Meta:
#         model = Newsletter
#         fields = '__all__'
