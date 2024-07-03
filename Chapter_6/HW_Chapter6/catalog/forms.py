from django import forms

from catalog.models import Product, Version
from django.forms import BooleanField


class StyleFormMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        exclude = ['id', 'owner']

    def clean_name(self):
        bad_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data = self.cleaned_data['name']
        if cleaned_data in bad_words:
            raise forms.ValidationError(f'Слово {cleaned_data} не должно присутствовать в наименовании товара')
        return cleaned_data

    def clean_description(self):
        bad_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data = self.cleaned_data['description']
        if cleaned_data in bad_words:
            raise forms.ValidationError(f'Слово {cleaned_data} не должно присутствовать в описании товара')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
