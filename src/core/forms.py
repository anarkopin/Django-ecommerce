from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': "Tu nombre"
    }))
    Email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': "Tu Correo electronico"
    }))
    message = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Tu mensaje"
    }))


