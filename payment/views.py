from decimal import Decimal
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseForbidden

import sys
import urllib.parse
import requests

from orders.models import Order

# Create your views here.

def nvp_handler(nvp):
	# This is passed a PayPalNVP object when payment succeeds.
    # This should do something useful!
    print(nvp)

# def payment_process(request):
# 	order_id = request.session.get('order_id')
# 	order = get_object_or_404(Order, id=order_id)
# 	host = request.get_host()
# 	item = {"paymentrequest_0_amt": '1.00',#'%.2f' % order.product.price.quantize(Decimal('.01')),
# 			"amt": '2.00',
# 			"inv": str(order.id),
# 			"custom": str(order.id),
# 			"cancelurl": 'http://{}{}'.format(host,	reverse('payment:canceled')),
# 			"returnurl": 'http://{}{}'.format(host, reverse('payment:done'))}
# 	ppp = PayPalPro(item=item,
# 			payment_template="payment/process.html",
# 			confirm_template="payment/confirmation.html",
# 			success_url="/success/",
# 			nvp_handler=nvp_handler)

# 	return ppp(request)

def payment_process(request):
	order_id = request.session.get('order_id')
	order = get_object_or_404(Order, id=order_id)
	host = request.get_host()

	return render(request, 'payment/process.html',
		   		  {'order': order, 'product': order.product})


@csrf_exempt
def payment_done(request):
	return render(request, 'payment/done.html')


@csrf_exempt
def payment_canceled(request):
	return render(request, 'payment/canceled.html')

@csrf_exempt
def payment_notification(request):
	# print('-----------------ATTENTION: PAYMENT NOTIFICATON--------------------------')

	# VERIFY_URL_PROD = 'https://www.paypal.com/cgi-bin/webscr'
	# VERIFY_URL_TEST = 'https://www.sandbox.paypal.com/cgi-bin/webscr'

	# # Switch as appropriate
	# VERIFY_URL = VERIFY_URL_TEST

	# # CGI preamble
	# print("content-type: text/plain")
	# print()

	# # Read and parse query string
	# query = 'cmd=_notify-validate'
	# for key, value in request.POST.items():
	# 	query += '&%s=%s' % (key, urllib.parse.quote(value))

	# # Post back to PayPal for validation
	# headers = {'content-type': 'application/x-www-form-urlencoded', 'host': 'www.paypal.com'}
	# r = requests.post(VERIFY_URL, params=query, headers=headers, verify=True)
	# r.raise_for_status()

	# # Check return message and take action as needed
	# if r.text == 'VERIFIED':
	#     print('verified')
	#     return HttpResponse('')
	# elif r.text == 'INVALID':
	#     print('invalid')
	#     return HttpResponseForbidden()
	# else:
	#     print('nor verified nor invalid')
	#     return HttpResponseForbidden()

	# paypal_url = 'https://www.sandbox.paypal.com/cgi-bin/webscr'
	# query = 'cmd=_notify-validate'
	# for key, value in request.POST.items():
	# 	query += '&%s=%s' % (key, urllib.parse.quote(value))
	# 	print('&%s=%s' % (key, urllib.parse.quote(value)))
	# res = requests.post(paypal_url, data=query, timeout=10)

	# print(res.text)
	# if res.text == 'VERIFIED':
	# 	print('verified')
	# 	# Extract POST variables here
	# 	payment_status = request.POST.get('payment_status')
	# 	if payment_status == 'Completed':
	# 		# Successful payment
	# 		print('completed')
	# 		# Order as completed.
	# 		order_id = request.POST.get('custom')
	# 		order = Order.objects.filter(pk=order_id)[0]
	# 		order.paid = True
	# 		order.save()
	# 		#Enrolling user.


	# 	elif payment_status == 'Reversed' or payment_status == 'Refunded':
	# 		# Payment reversed
	# 		print('reversed or refunded')
	# else:
	# Adding command for the response.
	data = b'cmd=_notify-validate&'
	data += request.body
	# Posting verification.
	verification = requests.post('https://ipnpb.sandbox.paypal.com/cgi-bin/webscr', data=data)
	print(verification.text)

	#Chacking verification
	if verification.text == 'VERIFIED':
		# process IPN
		print(request.POST)

		payment_status = request.POST.get('payment_status')
		if payment_status == 'Completed':
			# Successful payment
			print('completed')
			# Order as completed.
			# order_id = request.POST.get('custom')
			# order = Order.objects.filter(pk=order_id)[0]
			# order.paid = True
			# order.save()
			#Enrolling user.


		elif payment_status == 'Reversed' or payment_status == 'Refunded':
			# Payment reversed
			print('reversed or refunded')

		return HttpResponse('')
	else:
		return HttpResponseForbidden()


	