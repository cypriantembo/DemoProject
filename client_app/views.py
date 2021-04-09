from django.shortcuts import render, redirect
from .models import Client, Transactions
from .forms import PickupForm, CreateUserForm, ClientForm, UserProfileUpdateForm, ClientUpdateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User


from django.contrib import messages


@login_required()
def home(request):
    context = {}
    return render(request, 'client_app/home.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')
        context = {}
        return render(request, 'client_app/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


def register_page(request):
    if request.user.is_authenticated:
        return redirect('login')
    else:
        form = CreateUserForm()
        client_form = ClientForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)

            client_form = ClientForm(request.POST)

            if form.is_valid() and client_form.is_valid():
                user = form.save()

                client = client_form.save(commit=False)
                client.user = user
                client.save()

                user = form.cleaned_data.get('username')

                messages.success(request, 'Account Created for ' + user)

                return redirect('login')

        context = {'form': form, 'client_form': client_form}
        return render(request, 'client_app/register.html', context)


@login_required()
def payment(request):
    context = {}
    return render(request, 'client_app/payment.html', context)


@login_required()
def maps(request):
    context = {}
    return render(request, 'client_app/map.html', context)


@login_required()
@require_POST
def add_pickup(request):

    form = PickupForm(request.POST)
    if form.is_valid():
        city = (request.POST['city'])
        waste_type = (request.POST['waste_type'])
        transaction_type = (request.POST['transaction_type'])
        amount = (request.POST['amount'])
        user = request.user

        f = Transactions(city=city, waste_type=waste_type, transaction_type=transaction_type, amount=amount, user=user)
        f.save()

    return redirect('maps')

    # form = ClientForm(request.POST)
    #
    # if form.is_valid():
    #     first_name = (request.POST['first_name'])
    #     last_name = (request.POST['last_name'])
    #     cell = (request.POST['cell'])
    #     location = (request.POST['location'])
    #     user = request.user
    #
    #     f = Client(first_name=first_name, last_name=last_name, cell=cell, location=location, user=user)
    #     f.save()
    #
    # return redirect('pickup')


@login_required()
def pickup(request):
    form = PickupForm()

    context = {'form': form}
    return render(request, 'client_app/pickup.html', context)

    # form = PickupForm(request.POST)
    #
    # if form.is_valid():
    #     city_select = Transactions(city=request.POST['city'])
    #     waste_type_select = Transactions(waste_type=request.POST['waste_type'])
    #     transaction_type_select = Transactions(transaction_type=request.POST['transaction_type'])
    #     amount_select = Transactions(amount=request.POST['amount'])
    #     print(request.POST['city'])
    #
    #     city_select.save()
    #     waste_type_select.save()
    #     transaction_type_select.save()
    #     amount_select.save()
    #     return redirect('payment')
    # context = {'form': form}
    # return render(request, 'driver/pickup.html', context)

    # form = PickupForm()
    #
    # if request.method == 'POST':
    #     form = PickupForm(request.POST)
    #
    #     if form.is_valid():
    #         city = Transactions(city=request.POST['city'])
    #         waste_type = Transactions(waste_type=request.POST['waste_type'])
    #         transaction_type = Transactions(transaction_type=request.POST['transaction_type'])
    #         amount = Transactions(amount=request.POST['amount'])
    #         city.save()
    #         waste_type.save()
    #         transaction_type.save()
    #         amount.save()
    #
    # context = {'form': form}
    # return render(request, 'driver/pickup.html', context)


@login_required()
def tracking(request):
    context = {}
    return render(request, 'client_app/tracking.html', context)


@login_required()
def maps(request):
    context = {}
    return render(request, 'client_app/maps.html', context)


@login_required()
def drivers(request):
    context = {}
    return render(request, 'client_app/drivers.html', context)


@login_required()
def transactions(request):
    current_user = request.user
    # queryset
    transaction_list = Transactions.objects.filter(user_id=current_user.id)
    context = {'transaction_list': transaction_list}
    return render(request, 'client_app/transactions.html', context)


@login_required()
def profile(request):
    current_user = request.user
    print(current_user.id)
    clients = Client.objects.get(user_id=current_user.id)
    context = {'clients': clients}
    return render(request, 'client_app/profile.html', context)


@login_required()
def profile_edit(request):
    current_user = request.user.client.area

    print(current_user)
    if request.method == 'POST':
        user_form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        client_form = ClientUpdateForm(request.POST, instance=request.user.client)
        if user_form.is_valid() and client_form.is_valid():
            client_form.save()
            user_form.save()
            messages.success(request, 'Your Profile has been updated!')
            return redirect('profile')
    else:
        user_form = UserProfileUpdateForm(instance=request.user)
        client_form = ClientUpdateForm(instance=request.user.client)

    context = {'user_form': user_form, 'client_form': client_form}
    return render(request, 'client_app/profile_edit.html', context)


# from django.shortcuts import render

# def profile(request):
#     if request.user.is_authenticated():
#         template= "Blog/logged_in_template.html"
#     else:
#         template= "Blog/public_template.html"

#     context= {}
#     return render (request, template, context)
