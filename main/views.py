from django.shortcuts import render, redirect
from .models import Client, Driver, Transactions
from .forms import PickupForm, CreateUserForm, ClientForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User


from django.contrib import messages


def home(request):
    context = {}
    return render(request, 'main/home.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('pickup')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('pickup')
            else:
                messages.info(request, 'Username or Password is incorrect')
        context = {}
        return render(request, 'main/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('pickup')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')

                messages.success(request, 'Account Created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'main/register.html', context)


@login_required(login_url='login')
def payment(request):
    context = {}
    return render(request, 'main/payment.html', context)


@login_required(login_url='login')
def maps(request):
    context = {}
    return render(request, 'main/map.html', context)


@login_required(login_url='login')
@require_POST
def addpickup(request):

    form = PickupForm(request.POST)
    if form.is_valid():
        city = (request.POST['city'])
        waste_type = (request.POST['waste_type'])
        transaction_type = (request.POST['transaction_type'])
        amount = (request.POST['amount'])
        user = request.user

        f = Transactions(city=city, waste_type=waste_type, transaction_type=transaction_type, amount=amount, user=user)
        f.save()

    return redirect('payment')

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


@login_required(login_url='login')
def pickup(request):
    form = PickupForm()

    context = {'form': form}
    return render(request, 'main/pickup.html', context)

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
    # return render(request, 'main/pickup.html', context)

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
    # return render(request, 'main/pickup.html', context)


@login_required(login_url='login')
def tracking(request):
    context = {}
    return render(request, 'main/tracking.html', context)


@login_required(login_url='login')
def transactions(request):
    transaction_list = Transactions.objects.order_by('transacted_at')
    context = {'transaction_list': transaction_list}
    return render(request, 'main/transactions.html', context)


@login_required(login_url='login')
def profile(request):
    current_user = request.user
    print (current_user.id)
    clients = Client.objects.get(user_id=current_user.id)
    context = {'clients': clients}
    return render(request, 'main/profile.html', context)