

from django import forms
from .models import Order
from .models import Product


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['shipping_address']
        widgets = {
            'shipping_address' : forms.Textarea(attrs={'rows':3}),
        }



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name' , 'description' , 'price' , 'category' , 'image_url']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'image_url': forms.TextInput(attrs={'placeholder': 'https://example.com/image.jpg'}),
        }        