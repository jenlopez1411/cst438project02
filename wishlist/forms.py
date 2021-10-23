from django.forms import ModelForm 
from .models import Users, models


class UserForm(ModelForm):
    class Meta: 
        model = Users
        fields = '__all__'