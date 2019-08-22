from django import forms
from .models import Discount, Door, Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        # fields = ['w', 'h', 'd', 'door']
        exclude = ('user',)

class DoorForm(forms.Form):
    doors_type = forms.ModelChoiceField(queryset=Door.objects.values_list('code', flat=True).order_by('id').distinct(), initial=0, widget=forms.RadioSelect)
    width = forms.CharField(widget=forms.TextInput(attrs={'size': '10'}))
    height = forms.CharField(widget=forms.TextInput(attrs={'size': '10'}))
    depth = forms.CharField(widget=forms.TextInput(attrs={'size': '10'}))
    