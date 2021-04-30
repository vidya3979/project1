from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from mobileapp.models import Mobile, Buyer


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class MobileCreateForm(ModelForm):
    class Meta:
        model = Mobile
        fields = "__all__"


class MobileEditForm(ModelForm):
    class Meta:
        model = Mobile
        fields = "__all__"


class BuyerForm(ModelForm):
    class Meta:
        model = Buyer
        fields = "__all__"
        widgets={
            "user":forms.TextInput(attrs={'readonly':'readonly'}),
            "product":forms.TextInput(attrs={'readonly':'readonly'})
        }



class BuyerEditForm(ModelForm):
    class Meta:
        model = Buyer
        fields = "__all__"
