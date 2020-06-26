from django import forms
from .models import RegistrationData
#addning the attirubtes in widget and passing it allows to use the attributes of bootstrap
class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30,widget = forms.TextInput(attrs={
        'class':"form-control",
        "placeholder":"Username"
    }))
    password = forms.CharField(max_length=30,widget = forms.PasswordInput(attrs={
        'class':"form-control",
        "placeholder":"Password"
    }))
    email = forms.EmailField(max_length=30,widget = forms.EmailInput(attrs={
        'class':"form-control",
        "placeholder":"Email"
    }))
    phone = forms.CharField(max_length=30,widget = forms.TextInput(attrs={
        'class':"form-control",
        "placeholder":"Phone"
    })) 

class RegistrationModel(forms.ModelForm):
    class Meta:
        model = RegistrationData
        fields = [
            'username',
            'password',
            'email',
            'phone'
        ]