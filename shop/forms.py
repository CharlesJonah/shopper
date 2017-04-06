import string
from django import forms
from django.contrib.auth.models import User


class UserForm(forms.Form): 
    first_name = forms.CharField(required=True, max_length=30, \
                                widget=forms.TextInput(attrs={'placeholder': 'First name ...','class':'txt'}))
    last_name = forms.CharField(required=True,  max_length=30, \
                                widget=forms.TextInput(attrs={'placeholder': 'Last name ...','class':'txt'}))
    email = forms.EmailField( required=True, max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'Email ...','class':'txt'}))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder': 'New password ...','class':'pwd'}))

    def clean_mail(self, email):
       if User.objects.filter(username=email).exists():
           self.add_error("email", "Email already exists!")
           return False
       return self.cleaned_data
    def clean_pwd(self,password):
        if not any(x.isupper() for x in password) or not any(x.islower() for x in password) or len(password) < 8 or len(password) < 8 \
           or not any(x.isdigit() for x in password):
             self.add_error("password", "Password must contain a capital letter, a small letter, a digit and should be 8 to 16 characters long")
             return False
        return self.cleaned_data


class SignInForm(forms.Form):
    email = forms.EmailField( required=True, max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'Email ...','class':'txt'}))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Password ...','class':'pwd'}))
    
class SearchForm(forms.Form): 
    search = forms.CharField(required=True, max_length=30, \
                                widget=forms.TextInput(attrs={'placeholder': 'Search Products ...','class':'search'}))

        