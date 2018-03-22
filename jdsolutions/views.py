from django.shortcuts import render

from django.http import HttpResponse

# FORMS
from jdsolutions.forms import ContactForm

# Create your views here.


def home(request):
	if request.method == 'POST':
		form = ContactForm(request.POST or None)
		if form.is_valid():
			contact = form.save(commit=False)
			contact.save()
			return render(request, 'jdsolutions/home.html')
	else:
		form = ContactForm()
	context = {'form':form}

	return render(request, 'jdsolutions/home.html', context)






