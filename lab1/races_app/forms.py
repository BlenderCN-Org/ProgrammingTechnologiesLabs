from django import forms


class LogInForm(forms.Form):
    email = forms.EmailField(label='email', max_length=127, widget=forms.EmailInput())
    password = forms.CharField(label='password', max_length=127, widget=forms.PasswordInput())
