from django import forms


class SignInForm(forms.Form):
    email = forms.EmailField(label='email', max_length=127, widget=forms.EmailInput())
    password = forms.CharField(label='password', max_length=127, widget=forms.PasswordInput())


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=127)
    last_name = forms.CharField(max_length=127)
    email = forms.EmailField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput(), max_length=127)
    password_confirm = forms.CharField(widget=forms.PasswordInput(), max_length=127)
    roles = (('client', 'Common'), ('bookmaker', 'Bookmaker'), ('admin', 'Administrator'))
    role = forms.ChoiceField(choices=roles)

    def is_valid(self):
        if super(forms.Form, self).is_valid():
            password_data = self.cleaned_data.get('password')
            password_confirm_data = self.cleaned_data.get('password_confirm')
            print(password_data + ' ' + password_confirm_data)
            if password_data == password_confirm_data:
                return True
        return False
