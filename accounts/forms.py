from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django import forms
from .models import UserProfile

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2','first_name','last_name',)
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter Username'}),
            'email': forms.TextInput(
                attrs={'placeholder': 'Enter Email'}),
            'password1': forms.PasswordInput(
                attrs={'placeholder': 'Enter Password'}),
            'password2': forms.PasswordInput(
                attrs={'placeholder': 'Confirm Password Again'}),
        }

    def clean_password1(self):
        print('Password validation')
        password1 = self.cleaned_data.get('password1')
        try:
            password_validation.validate_password(password1, self.instance)
        except forms.ValidationError as error:
            self.add_error('password1', error)
        return password1

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone_number','tag_line')

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email','first_name','last_name')
