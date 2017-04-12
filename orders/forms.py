from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ['first_name', 'last_name', 'city', 'country']

	def __init__(self, *args, **kwargs):
		super(OrderCreateForm, self).__init__(*args, **kwargs)
		self.fields['country'].required = True