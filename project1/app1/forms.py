from django import forms
from . models import registration

class registrationforms(forms.ModelForm):
        class Meta:
            model = registration
            fields = '__all__'
