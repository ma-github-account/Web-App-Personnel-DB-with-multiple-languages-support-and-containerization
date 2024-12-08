from django import forms
from .models import Contact
from django.forms import ModelForm

#class NameForm(forms.Form):
#    
#	name = forms.CharField(label='Name', max_length=100)
#	second_name = forms.CharField(label='Second_name', max_length=100)


#class ContactForm(forms.ModelForm):
#
#	class Meta:
#
#		model = Contact
#		fields = ('name', 'second_name')

class ContactForm(ModelForm):

	class Meta:
		model = Contact
		fields = '__all__'


















