from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    gender_list=(
        ('','-------Select Gender-------'),
        ('Male','Male'),
        ('Female','Female')
    )

    gender = forms.ChoiceField(choices=gender_list)
    age = forms.IntegerField(min_value=1, max_value=100)
    marital_status = forms.CharField(widget=forms.CheckboxInput(attrs={'value':"True"}), required=False)
    mobile = forms.CharField(required=False, min_length=10)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'gender', 'age', 'marital_status', 'email', 'mobile', 'password1', 'password2']
    

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    age = forms.IntegerField(min_value=1, max_value=100)
    class Meta:
        model = Profile
        fields = ['gender', 'age', 'marital_status', 'mobile', 'image']
        