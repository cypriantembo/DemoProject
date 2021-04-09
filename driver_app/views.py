from django.shortcuts import render, redirect

from .models import Driver
from client_app.models import Transactions
from .forms import CreateUserForms, DriverForms, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages


def driver_login_page(request):
    if request.user.is_authenticated:
        return redirect('driver_pickup')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('driver_pickup')
            else:
                messages.info(request, 'Username or Password is incorrect')
        context = {}
        return render(request, 'driver_app/driver_login.html', context)


def driver_logout(request):
    logout(request)
    return redirect('driver_login')


def register_driver_page(request):
    if request.user.is_authenticated:
        return redirect('driver_pickup')
    else:
        form = CreateUserForms()
        driver_form = DriverForms()

        if request.method == 'POST':
            form = CreateUserForms(request.POST)

            driver_form = DriverForms(request.POST)

            if form.is_valid() and driver_form.is_valid():
                user = form.save()

                driver = driver_form.save(commit=False)
                driver.user = user
                driver.save()

                user = form.cleaned_data.get('username')

                messages.success(request, 'Driver Account Created for ' + user)

                return redirect('driver_login')

        context = {'form': form, 'driver_form': driver_form}
        return render(request, 'driver_app/driver_register.html', context)


@login_required(login_url='login')
def driver_profile(request):
    current_user = request.user
    print(current_user.id)
    drivers = Driver.objects.get(user_id=current_user.id)
    context = {'drivers': drivers}
    return render(request, 'driver_app/driver_profile.html', context)


@login_required(login_url='login')
def driver_pickup(request):
    pickup_list = Transactions.objects.filter(transaction_state=False)
    context = {'pickup_list': pickup_list}

    return render(request, 'driver_app/driver_pickup.html', context)


@login_required(login_url='login')
def driver_transaction_log(request):
    transaction_list = Transactions.objects.filter(transaction_state=True)
    context = {'transaction_list': transaction_list}

    return render(request, 'driver_app/driver_transaction_log.html', context)


@login_required()
def driver_home_page(request):

    return render(request, 'driver_app/driver_home.html')


@login_required()
def driver_profile_edit(request):
    current_user = request.user.driver.company

    print(current_user)
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        u_form = UserUpdateForm(request.POST, instance=request.user.driver)
        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your Profile has been updated!')
            return redirect('driver_profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user)
        u_form = UserUpdateForm(instance=request.user.driver)

    context = {'p_form': p_form, 'u_form': u_form}
    return render(request, 'driver_app/driver_profile_edit.html', context)



