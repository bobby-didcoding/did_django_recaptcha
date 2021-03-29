from django.forms import ModelForm
from django import forms
from .models import Contact

# DOCS - https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/


'''
Basic model-form for our contact model
'''
class ContactForm(forms.ModelForm):
	
	name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Full name..'}))
	telephone = forms.CharField(max_length=15, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Telephone..'}))
	email = forms.EmailField(max_length=254, required=True, 
		widget=forms.TextInput(attrs={'placeholder': '*Email..'}))
	message = forms.CharField(max_length=1000, required=True, 
		widget=forms.TextInput(attrs={'placeholder': '*Message..'}))
	#reCAPTCHA token
	token = forms.CharField(
		widget=forms.HiddenInput())

	class Meta:
		model = Contact
		fields = ('name', 'telephone', 'email', 'message',)

