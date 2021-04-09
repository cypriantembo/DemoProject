from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Driver


class DriverForms(forms.ModelForm):
    company = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', }))
    city = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', }))
    area = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', }))
    road = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', }))
    contact = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', }))
    location_coords = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', }))

    class Meta:
        model = Driver
        fields = ('company', 'city', 'area', 'road', 'contact', 'location_coords')


class CreateUserForms(UserCreationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', }))
    email = forms.EmailField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', }))
    password1 = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', }))
    password2 = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', }))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', }))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', }))

    class Meta:
        model = User
        # fields = ['username', 'email', 'password1', 'password2']
        fields = UserCreationForm.Meta.fields + ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')


class ProfileUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', }))
    email = forms.EmailField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', }))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', }))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', }))

    class Meta:
        model = User
        # fields = ['username', 'email', 'password1', 'password2']
        fields = UserCreationForm.Meta.fields + ('username', 'email', 'first_name', 'last_name')


class UserUpdateForm(forms.ModelForm):
    company = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', }))
    city = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', }))
    area = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', }))
    road = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', }))
    contact = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', }))
    location_coords = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', }))

    class Meta:
        model = Driver
        fields = ('company', 'city', 'area', 'road', 'contact', 'location_coords')






















