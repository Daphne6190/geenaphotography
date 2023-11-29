from django import forms
from photographyapp.models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname', 'lastname', 'address', 'phonenumber', 'email', 'service']
