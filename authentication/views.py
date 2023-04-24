from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, reverse
from django.utils.crypto import get_random_string
from django.views import View

from utils.email_service import send_email
from .forms import LoginForm, RegisterForm, ForgotPasswordForm, ResetPasswordForm
from .models import User


class RegisterView(View):

    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'authentication/sign_up.html', {'register_form': register_form})

    def post(self, request):

        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            email = register_form.cleaned_data.get('email')
            password = register_form.cleaned_data.get('password')
            confirm_password = register_form.cleaned_data.get('confirm_password')
            checkemail: bool = User.objects.filter(email__iexact=email).exists()
            user: bool = User.objects.filter(username__iexact=username).exists()

            if checkemail:
                messages.error(request, 'Email address already registered!', extra_tags='danger')
            else:
                if user:
                    messages.error(request, 'Username already taken!', extra_tags='danger')
                else:
                    if confirm_password:
                        new_user = User(
                            email=email,
                            active_code=get_random_string(47),
                            is_active=False,
                            is_staff=False,
                            password=password,
                            username=username,
                        )
                        new_user.set_password(password)
                        new_user.save()

                        send_email('activation', new_user.email, {'user': new_user}, 'emails/activate_account.html')
                        messages.success(request, 'Your email has been sent successfully!')


                    else:
                        messages.error(request, 'Please ensure your passwords match!', extra_tags='danger')

        return render(request, 'authentication/sign_up.html', {'register_form': register_form})


class LoginView(View):
    def get(self, request):
        Login_form = LoginForm(request.GET)
        return render(request, 'authentication/sign_in.html', {'Login_form': Login_form})

    def post(self, request):
        Login_form = LoginForm(request.POST)
        if Login_form.is_valid():
            email = Login_form.cleaned_data.get('email')
            password = Login_form.cleaned_data.get('password')
            mail = User.objects.filter(email__iexact=email).first()
            if mail is not None:
                if not mail.is_active:
                    messages.error(request, 'Account not activated')
                else:
                    is_password_correct = mail.check_password(password)
                    if is_password_correct:
                        login(request, mail)
                        return redirect(reverse('home'))
                    else:
                        messages.error(request, 'Incorrect password!', extra_tags='danger')
            else:

                messages.error(request, 'No account found with this email address!', extra_tags='danger')
        return render(request, 'authentication/sign_in.html', {'Login_form': Login_form})


class ActivationView(View):
    def get(self, request, active_code):
        user: User = User.objects.filter(active_code__iexact=active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.is_staff = True
                user.active_code = get_random_string(47)
                user.save()
                return redirect(reverse('login'))

        else:
            return redirect(reverse('Notfound'))

        return redirect(reverse('login'))


class ForgotPassword(View):
    def get(self, request):

        ForgetpassForm = ForgotPasswordForm(request.GET)
        return render(request, 'authentication/forgot_password.html', {'forgetpassword': ForgetpassForm})

    def post(self, request):
        ForgetpassForm = ForgotPasswordForm(request.POST)
        if ForgetpassForm.is_valid():
            email = ForgetpassForm.cleaned_data.get('email')
            user: bool = User.objects.filter(email__iexact=email).first()
            if user is not None:
                send_email('forget password', user.email, {'user': user}, 'emails/forget_password.html')
                messages.success(request, 'Your email has been sent successfully!')
        return render(request, 'authentication/forgot_password.html', {'forgetpassword': ForgetpassForm})


class ResetPassword(View):
    def get(self, request, active_code):
        ResetpassForm = ResetPasswordForm()
        user: User = User.objects.filter(active_code__iexact=active_code).first()
        if user is None:
            messages.error(request, 'No account found with this email address!', extra_tags='danger')

        return render(request, 'authentication/reset_password.html', {'resetpassword': ResetpassForm})

    def post(self, request, active_code):
        ResetpassForm = ResetPasswordForm(request.POST)
        if ResetpassForm.is_valid():
            user: User = User.objects.filter(active_code__iexact=active_code).first()
            confirm_password = ResetpassForm.cleaned_data.get('confirm_password')
            if ResetpassForm.is_valid():
                if user is None:
                    return redirect(reverse('Notfound'))
                else:
                    if confirm_password:
                        NewPassword = ResetpassForm.cleaned_data.get('password')
                        user.set_password(NewPassword)
                        user.active_code = get_random_string(47)
                        user.is_active = True
                        user.is_staff = True
                        user.save()
                    else:
                        messages.error(request, 'Please ensure your passwords match!', extra_tags='danger')

        return render(request, 'authentication/reset_password.html', {'resetpassword': ResetpassForm})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('home'))
