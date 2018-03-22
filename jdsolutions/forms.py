from jdsolutions.models import Contact
from django.forms import ModelForm



class ContactForm(ModelForm):
	class Meta:
		model = Contact
		fields = ['name', 'email', 'comment']

	# def clean(self):
	# 	cleaned_data = super(ContactForm, self).clean()
	# 	name = cleaned_data.get('name')
	# 	phone = cleaned_data.get('phone')
	# 	email = cleaned_data.get('email')
	# 	comment = cleaned_data.get('comment')

	# 	if not name and not phone and not email and not comment:
	# 		raise forms.ValidationError('You have to write something!')

	# 	if not name:
	# 		raise forms.ValidationError("You need to enter your name")
	# 	if not phone:
	# 		raise forms.ValidationError("You need to enter a valid phone number")
	# 	if not email:
	# 		raise forms.ValidationError("You need to enter your email")
	# 	if not comment:
	# 		raise forms.ValidationError("Please leave us a message")
























































