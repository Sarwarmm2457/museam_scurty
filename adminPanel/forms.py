from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm

# the AccountAuthenticationForm that we use in our login page.
class AccountAuthenticationForm(forms.ModelForm):
    # creating two fields for username and password
    passwordlogin = forms.CharField(
        label="Password", widget=forms.PasswordInput)
    usernamelogin = forms.CharField(label='username')

    class Meta:
        # setting the Model to the User model with the fields
        model = User
        fields = ("usernamelogin", 'passwordlogin')

    def clean(self):
        if self.is_valid():  # check if it's valid
            usernamelogin = self.cleaned_data['usernamelogin']
            passwordlogin = self.cleaned_data['passwordlogin']
            # if the user is not authenticated after the authentication that means something went wrong and the given crendenial is invalid so we raise a validationError.
            if not authenticate(username=usernamelogin, password=passwordlogin):
                raise forms.ValidationError('Invalid Login') # return when login is invalid 