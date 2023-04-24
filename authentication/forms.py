from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.EmailInput(
        attrs={'placeholder': "Username", 'type': "text", 'class': "form-control input-lg", 'id': "name",
               'aria-describedby': "nameHelp"}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': "Email", 'type': "email", 'class': "form-control input-lg", 'id': "email",
               'aria-describedby': "emailHelp"}))
    password = forms.CharField(widget=forms.EmailInput(
        attrs={'placeholder': "Password", 'type': "password", 'class': "form-control input-lg", 'id': "password"}))
    confirm_password = forms.CharField(widget=forms.EmailInput(
        attrs={'placeholder': "Password", 'type': "password", 'class': "form-control input-lg", 'id': "password"}))

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password'),
        confirm_password = self.cleaned_data.get('confirm_password'),
        if password == confirm_password:
            return confirm_password


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'placeholder': "email", 'type': "email", 'class': "form-control input-lg", 'id': "email",
               'aria-describedby': "emailHelp"}))
    password = forms.CharField(widget=forms.EmailInput(
        attrs={'placeholder': "password", 'type': "password", 'class': "form-control input-lg", 'id': "password"}))


class ForgotPasswordForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'placeholder': "email", 'type': "email", 'class': "form-control input-lg", 'id': "email",
               'aria-describedby': "emailHelp"}))

class ResetPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.EmailInput(
        attrs={'placeholder': "password", 'type': "password", 'class': "form-control input-lg", 'id': "password"}))
    confirm_password = forms.CharField(widget=forms.EmailInput(
        attrs={'placeholder': "confirm password", 'type': "password", 'class': "form-control input-lg", 'id': "password"}))
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password'),
        confirm_password = self.cleaned_data.get('confirm_password'),
        if password == confirm_password:
            return confirm_password
