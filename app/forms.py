from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate


class SigninForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(
            label="Password",
            max_length=32,
            widget=forms.PasswordInput
            )

    def clean(self):
        cleaned_data = super().clean()
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(username=email, password=password)
            if user is None:
                raise ValidationError('Invalid email or password')
            self.cleaned_data['user'] = user
        return cleaned_data


class SignupForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(
            label="Password",
            max_length=32,
            widget=forms.PasswordInput
            )
    password_2 = forms.CharField(
            label="Confirm Password",
            max_length=32,
            widget=forms.PasswordInput
            )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password_2 = self.cleaned_data.get('password_2')

        if password and password_2 and password != password_2:
            raise ValidationError('Passwords do not match.')
        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise ValidationError('A user with this email already exists.')
        return email

    def save(self, commit=True):
        user = User(
                username=self.cleaned_data['email'],
                email=self.cleaned_data['email']
                )
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
