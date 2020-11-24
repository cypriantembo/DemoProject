from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

CITIES = [('Lusaka', 'Lusaka'),
          ('Ndola', 'Ndola'),
          ('Kabwe', 'Kabwe')]

WASTE_TYPE = [('Plastic', 'Plastic'), ('Metal', 'Metal'), ('Glass', 'Glass'),
              ('Paper', 'Paper'), ('Organic', 'Organic')]
PAYMENT_METHOD = [('Bank', 'Bank'), ('Mtn money', 'Mtn Money'), ('Airtel money', 'Airtel Money')]


class ClientForm(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', }))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', }))
    cell = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', }))
    location = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', }))


class PickupForm(forms.Form):
    city = forms.CharField(label='Select your city?', widget=forms.Select(
        choices=CITIES, attrs={'class': 'form-control', }))
    waste_type = forms.CharField(label='Select your city?', widget=forms.Select(
        choices=WASTE_TYPE, attrs={'class': 'form-control', }))
    transaction_type = forms.CharField(label='Select your city?', widget=forms.Select(
        choices=PAYMENT_METHOD, attrs={'class': 'form-control', }))
    amount = forms.DecimalField(max_digits=4, decimal_places=0,  widget=forms.TextInput(
        attrs={'class': 'form-control', }))


class CreateUserForm(UserCreationForm):
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


#
# FRUIT_CHOICES= [
#     ('orange', 'Oranges'),
#     ('cantaloupe', 'Cantaloupes'),
#     ('mango', 'Mangoes'),
#     ('honeydew', 'Honeydews'),
#     ]
#
# class UserForm(forms.Form):
#     first_name= forms.CharField(max_length=100)
#     last_name= forms.CharField(max_length=100)
#     email= forms.EmailField()
#     age= forms.IntegerField()
#     favorite_fruit= forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=FRUIT_CHOICES))
