from django import forms
from .models import *

class routeForm(forms.ModelForm):
    class Meta:
        model = Routes
        fields = ('route_short_name',)
