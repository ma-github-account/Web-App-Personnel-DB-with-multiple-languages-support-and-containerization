from django.shortcuts import render, get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext

def contact_list(request):
	
	trans = translate(language='fr')
	contact = None
	contacts = Contact.objects.all()
	return render(request, 'organizer/contact/list.html', {'trans': trans, 'contacts': contacts})

def contact_detail(request, id):

	contact = get_object_or_404(Contact, id=id)
	trans = translate(language='fr')
	return render(request, 'organizer/contact/detail.html', {'trans': trans,'contact': contact})

#def get_name(request):
#	# if this is a POST request we need to process the form data
#	if request.method == 'POST':
#		# create a form instance and populate it with data from the request:
#		form = ContactForm(request.POST)
#		# check whether it's valid:
#		if form.is_valid():
#
#			name = form.cleaned_data["name"]
#
#			second_name = form.cleaned_data["second_name"]
#
#
#			#new_testobject = form.save(commit=True)
#
#			new_testobject = Contact(name = name, second_name = second_name)
#
#			new_testobject.save()
#
#
#			# process the data in form.cleaned_data as required
#			# ...
#			# redirect to a new URL:
#			return HttpResponseRedirect('/')
#
#	# if a GET (or any other method) we'll create a blank form
#	else:
#		form = ContactForm()
#
#	return render(request, 'organizer/contact/name.html', {'form': form})







def add(request):

	form = ContactForm()

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			
	context = {'form':form}
	return render(request, 'organizer/contact/add.html', context)


def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext('hello')
    finally:
        activate(cur_language)
    return text












