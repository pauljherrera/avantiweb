from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name',)
		index_together = (('id', 'slug'),)

	def __str__(self):
		return self.name


class Order(models.Model):
	owner = models.ForeignKey(User, related_name='orders', null=True, blank=True)
	first_name = models.CharField(_('first name'), max_length=50)
	last_name = models.CharField(_('last name'), max_length=50)
	city = models.CharField(_('city'), max_length=100)
	country = CountryField(null=True, blank=True)
	product = models.ForeignKey(Product, related_name='orders', null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	paid = models.BooleanField(default=False)
	
	class Meta:
		ordering = ('-created',)
	
	def __str__(self):
		return 'Order {}'.format(self.id)
		
