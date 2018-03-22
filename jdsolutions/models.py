from django.db import models

# Create your models here.



class Contact(models.Model):
	name = models.CharField(max_length=250, help_text="Please provide your first and last names")
	email = models.EmailField(help_text="Please provide contact email")
	comment = models.TextField(help_text="What is the nature of your inquiry/problem")
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

































