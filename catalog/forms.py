from django import forms
from django.forms import ModelForm, BooleanField
from django.core.exceptions import ValidationError
from catalog.models import Product

forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево",
"бесплатно", "обман", "полиция", "радар"]


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = "form-check-input"
            else:
                fild.widget.attrs['class'] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ("views_counter",)

    def clean_name(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')

        for word in forbidden_words:
            if name and word.lower() in name.lower():
                raise ValidationError(f'Название не может содержать запрещенное слово {word}')
        return name

    def clean_description(self):
        cleaned_data = super().clean()
        description = cleaned_data.get('description')
        descriptions = description.split()

        for wrd in descriptions:
            for word in forbidden_words:
                if wrd and word.lower() in wrd.lower():
                    raise ValidationError(f'Описание не может содержать запрещенное слово {word}')
        return description

    def clean_price(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('price')

        if price < 0:
                raise ValidationError('Цена продукта не может быть отрицательной')
        return price