from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'first_name',
                  'last_name',
                  'password1',
                  'password2'
        ]
        labels = {
            'username':"Používateľské meno",
            'email':"Email",
            'first_name':"Meno",
            'last_name':"Priezvisko",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].label = "Heslo"
        self.fields['password2'].label = "Potvrdenie hesla"

        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Používateľské meno")
    password = forms.CharField(label="Heslo", widget=forms.PasswordInput)