from django import forms
from . models import Student_model

class Student_signup_form(forms.ModelForm):
    class Meta:
        model = Student_model
        widgets = {'password': forms.PasswordInput(),'conform_password': forms.PasswordInput(),}
        fields = "__all__"

class Student_login_form(forms.Form):
    name = forms.CharField(max_length=64,widget=forms.TextInput())
    password = forms.CharField(max_length=10,widget=forms.PasswordInput())
