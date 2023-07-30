from django import forms

from .models import Send


class Sending(forms.ModelForm):
    class Meta:
        model = Send()
        fields = '__all__'
