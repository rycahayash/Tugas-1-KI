from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from user.forms import RegistrationForm, AccountAuthenticationForm

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def registration_view(request):
    context = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            # Save user data
            user = form.save(commit=False)
            user.save()

            # Handle the uploaded video
            if 'video_file' in request.FILES:
                user.video_file = request.FILES['video_file']
                user.save()

            # Authenticate and log in the user
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'user/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('home')
    
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('home')
            
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'user/login.html', context)

def home_view(request):
    context = {}
    return render(request, 'user/home.html', context)

def user_profil_view(request):
    context = {}
    return render(request, 'profil/profil.html', context)

def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to keep the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')  # Redirect to the same page after successful password change
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user/edit.html', {'form': form})

def show_kebijakan_privasi(request):
    context = {}
    return render(request, 'kebijakan_privasi.html', context)