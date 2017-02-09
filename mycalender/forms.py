from django import forms
#from django.contrib.auth.models import User

from .models import Event 



class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['event_name', 'location', 'starts', 'ends','all_day','description','event_date']


