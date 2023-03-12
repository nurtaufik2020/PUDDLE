from django import forms

from .models import Item
#tambahkan ini  untuk mengatur layout
INPUT_ClASSES = 'w-full py-4 px-rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields=('Category','name','description','price','image',)
    widget ={
        'category': forms.Select(attrs={
            'class':INPUT_ClASSES
        }),
        'name': forms.TextInput(attrs={
            'class':INPUT_ClASSES
        }),
        'description': forms.Textarea(attrs={
            'class':INPUT_ClASSES
        }),
        'price': forms.TextInput(attrs={
            'class':INPUT_ClASSES
        }),
        'image': forms.FileInput(attrs={
            'class':INPUT_ClASSES
        }),
    }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields=('name','description','price','image','is_sold')
    widget ={
        'name': forms.TextInput(attrs={
            'class':INPUT_ClASSES
        }),
        'description': forms.Textarea(attrs={
            'class':INPUT_ClASSES
        }),
        'price': forms.TextInput(attrs={
            'class':INPUT_ClASSES
        }),
        'image': forms.FileInput(attrs={
            'class':INPUT_ClASSES
        }),
    }