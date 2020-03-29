from django.forms import ModelForm
from django.forms import SelectMultiple


from .models import Perms



class PermsForm(ModelForm):
    class Meta:
        model = Perms
        fields = '__all__'