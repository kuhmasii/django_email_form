from django import forms
from django.core.exceptions import ValidationError



class EmailingForm(forms.Form):
	name = forms.CharField(max_length=50, required=True)
	Subject = forms.CharField(max_length=50, required=True)
	email = forms.EmailField()
	message = forms.CharField(widget=forms.Textarea, required=True)


	def clean(self):
		all_cleaned = super().clean()

		name = all_cleaned["name"]
		email = all_cleaned.get("email")

		numbers = [str(x) for x in range(11)]

		for nam in name:
			if nam in numbers:
				raise ValidationError("Instance of number cannot be in name")