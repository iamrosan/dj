from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room #creation of form model for which model. here for the Room model
        fields = '__all__' #all the attributes set in the the modelling of table
