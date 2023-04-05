from dataclasses import field
from django import forms
from betterforms.multiform import MultiModelForm

from .models import Booking, Event, EventImage, EventAgenda

class BookForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['eventname','numtickets','username']


class EventForm(forms.ModelForm):


    class Meta:
        model = Event
        # fields = ['category', 'name', 'uid', 'description', 'job_category', 'scheduled_status', 'venue', 'start_date', 'end_date', 'location', 'points', 'maximum_attende', 'status']
        fields = ['category', 'name', 'ufid', 'description', 'scheduled_status', 'venue', 'start_date', 'end_date', 'location', 'maximum_attende','num_tickets_available', 'status']
        widgets = {
            'start_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class EventImageForm(forms.ModelForm):


    class Meta:
        model = EventImage
        fields = ['image']



class EventAgendaForm(forms.ModelForm):


    class Meta:
        model = EventAgenda
        fields = ['session_name', 'speaker_name', 'start_time', 'end_time']
        # fields = ['session_name', 'speaker_name', 'start_time', 'end_time', 'venue_name']

        widgets = {
            'start_time': forms.TextInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TextInput(attrs={'class': 'form-control', 'type': 'time'}),
        }


class EventCreateMultiForm(MultiModelForm):
    form_classes = {
        'event': EventForm,
        'event_image': EventImageForm,
        'event_agenda': EventAgendaForm,
        'book': BookForm,
    }