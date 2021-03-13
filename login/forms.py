from django import forms
from django.contrib.auth import get_user_model


non_allowed_usernames = ['abc']

User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField()
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user_password"
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user_confirm_password"
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username_iexact=username)  # iexact équivaut thisIsMyUsername==thisIsMyUsername

        if username in non_allowed_usernames:
            raise forms.ValidationError("Username invalide")
        if qs.exists():
            raise forms.ValidationError("Email invalide, essayer un autre ")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email_iexact=email)  # iexact équivaut thisIsMyUsername==thisIsMyUsername
        if not qs.exists():
            raise forms.ValidationError("Email invalide ")
        return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user_password"
            }
        )
    )
        # def clean(self):
        #    username = self.cleaned_data.get("username")
        #   password = self.cleaned_data.get("password")


    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username_iexact=username) # iexact équivaut thisIsMyUsername==thisIsMyUsername
        if not qs.exists():
            raise forms.ValidationError("Username invalide ")
        if qs.count() !=1:
            raise forms.ValidationError("Username invaloid")
        return username