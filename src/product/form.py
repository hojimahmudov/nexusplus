from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'category', 'city', 'price', 'discaunt', 'candition', 'address']
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control input-md", "placeholder": "Title"}),
            "category": forms.Select(attrs={"class": "tg-select form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control input-md", "placeholder": "Add your price"}),
            "city": forms.Select(attrs={"class": "tg-select form-control"}),
            "candition": forms.Select(attrs={"class": "tg-select form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control input-md"})
        }


class ProductImageForm(forms.Form):
    image = forms.ImageField(label="image")


ProductImageFormSet = forms.formset_factory(ProductImageForm, extra=2)
