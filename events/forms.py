from django import forms
from django.forms import ModelForm
from .models import Venue,Event

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields =('name','address','zip_code','phone','web','email_address')
        labels={
            'name':'',
            'address':'',
            'zip_code':'',
            'phone':'',
            'web':'',
            'email_address':''
        }

        widgets ={
            'name': forms.TextInput(attrs={'class':'form-control',"placeholder":"venue Name"}),
            'address':forms.TextInput(attrs={'class':'form-control',"placeholder":"address"}),
            'zip_code':forms.TextInput(attrs={'class':'form-control',"placeholder":"zip code"}),
            'phone':forms.TextInput(attrs={'class':'form-control',"placeholder":"phone"}),
            'web':forms.TextInput(attrs={'class':'form-control',"placeholder":"web adress"}),
            'email_address':forms.EmailInput(attrs={'class':'form-control',"placeholder":"Email"})
              }
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields =('name','event_date','venue','manager','attendees','description')
        labels={
            'name':'',
            'event_date':'yyyy-MM-DD HH:MM:SS',
            'venue':'Venue ',
            'manager':'manager ',
            'description':'',
            'attendees':'atendeees'
        }

        widgets ={
            'name': forms.TextInput(attrs={'class':'form-control',"placeholder":"Event Name"}),
            'event_date':forms.TextInput(attrs={'class':'form-control',"placeholder":"Event date"}),
            'venue':forms.Select(attrs={'class':'form-select',"placeholder":"venue"}),
            'manager':forms.Select(attrs={'class':'form-select',"placeholder":"manager"}),
            'description':forms.Textarea(attrs={'class':'form-control',"placeholder":"description"}),
            'attendees':forms.SelectMultiple(attrs={'class':'form-control',"placeholder":"Atendees"})
              }
        

