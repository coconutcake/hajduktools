from django import forms
from .models import Discount, Door, Order

class OrderForm(forms.ModelForm):

        class Meta:
            model = Order
            CHOICES = (
            (11, 'Credit Card'),
            (12, 'Student Loans'),
            (13, 'Taxes'),
            (21, 'Books'),
            (22, 'Games'),
            (31, 'Groceries'),
            (32, 'Restaurants'),
        )
            
            fields = ['door', 'w', 'h', 'd', 'handle_site', 'inlet_site', 'customer', 'price',]
            exclude = ('user','data',)

            widgets = {
                'door': forms.RadioSelect(attrs={
                    'class': 'radioselect',
                }),
                'w': forms.TextInput(attrs={
                    'measure': 'width',
                    'class': 'shadow-sm form-control',
                    'id': 'w', 
                    'required': True, 
                    'placeholder': 'Type width here...'
                }),
                'h': forms.TextInput(attrs={
                    'measure': 'height',
                    'class': 'shadow-sm form-control',
                    'id': 'h', 
                    'required': True, 
                    'placeholder': 'Type height here...'
                }),
                'd': forms.TextInput(attrs={
                    'measure': 'depth',
                    'class': 'shadow-sm form-control',
                    'id': 'd', 
                    'required': False, 
                    'placeholder': 'Type depth here...'
                }),
                'handle_site': forms.Select(attrs={
                    'class': 'shadow-sm form-control'
                }),
                'inlet_site': forms.Select(attrs={
                    'class': 'shadow-sm form-control'
                }),
                'customer': forms.Textarea(attrs={
                    'class': 'shadow-sm form-control',
                    'rows': 2, 
                    'cols':1
                }),
                'price': forms.NumberInput(attrs={
                    'id' : 'pole_price',
                    'style': 'display:none;'
                }),
                
            }

        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.fields['price'].widget.attrs.update({'style': 'display:none;'})


            

            

class DoorForm(forms.Form):
    doors_type = forms.ModelChoiceField(queryset=Door.objects.values_list('code', flat=True).order_by('id').distinct(), initial=0, widget=forms.RadioSelect)
    width = forms.CharField(widget=forms.TextInput(attrs={'size': '10'}))
    height = forms.CharField(widget=forms.TextInput(attrs={'size': '10'}))
    depth = forms.CharField(widget=forms.TextInput(attrs={'size': '10'}))
    