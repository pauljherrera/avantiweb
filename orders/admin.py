import csv
import datetime
from django.http import HttpResponse
from django.contrib import admin
from django.core.urlresolvers import reverse

from .models import Order, Product

# Register your models here.
def export_to_csv(modeladmin, request, queryset):
	opts = modeladmin.model._meta
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; \
		filename={}.csv'.format(opts.verbose_name)
	writer = csv.writer(response)
	fields = [field for field in opts.get_fields()\
			  if not field.many_to_many and not field.one_to_many]
	# Write a first row with header information
	writer.writerow([field.verbose_name for field in fields])
	# Write data rows
	for obj in queryset:
		data_row = []
		for field in fields:
			value = getattr(obj, field.name)
			if isinstance(value, datetime.datetime):
				value = value.strftime('%d/%m/%Y')
			data_row.append(value)
		writer.writerow(data_row)
	return response

export_to_csv.short_description = 'Export to CSV'


def order_detail(obj):
	return '<a href="{}">View</a>'.format(
		reverse('orders:admin_order_detail', args=[obj.id]))	

order_detail.allow_tags = True


class OrderAdmin(admin.ModelAdmin):
	list_display = ['id', 'owner', 'first_name', 'last_name',
					'city', 'country', 'product', 'paid',
					'created', 'updated', order_detail]
	list_filter = ['paid', 'created', 'updated']
	actions = [export_to_csv]

class ProductAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'price', 'paypal_button', 'course']


admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
