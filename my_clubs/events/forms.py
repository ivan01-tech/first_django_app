from django import forms
from django.forms import ModelForm
from .models import Venue


class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = (
            "name",
            "address",
            "zip_code",
            "web",
            "email_address",
            "phone",
        )
        # labels = {"name": ""}
        widgets = {
            "name": forms.TextInput(
                attrs={"class": " my-1   border border-gray-600 bg-slate-100"}
            ),
            "address": forms.TextInput(
                attrs={"class": "border border-gray-600 bg-slate-100 my-1"}
            ),
            "zip_code": forms.TextInput(
                attrs={"class": "border border-gray-600 bg-slate-100 my-1"}
            ),
            "web": forms.URLInput(
                attrs={"class": "border border-gray-600 bg-slate-100 my-1"}
            ),
            "email_address": forms.EmailInput(
                attrs={"class": "border border-gray-600 bg-slate-100 my-1"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "border border-gray-600 bg-slate-100 my-1"}
            ),
        }
