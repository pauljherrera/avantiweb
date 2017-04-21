from decimal import Decimal
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseForbidden
from paypal.standard.forms import PayPalPaymentsForm
from paypal.pro.views import PayPalPro

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

	paypal_dict = {
		'business': settings.PAYPAL_RECEIVER_EMAIL,
		'amount': '%.2f' % order.product.price.quantize(Decimal('.01')),
		'item_name': 'Order {}'.format(order.id),
		'invoice': str(order.id),
		'currency_code': 'USD',
		'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
		'return_url': 'http://{}{}'.format(host, reverse('payment:done')),
		'cancel_return': 'http://{}{}'.format(host,	reverse('payment:canceled')),
	}
	form = PayPalPaymentsForm(initial=paypal_dict)
	
	return render(request, 'payment/process.html',
		   		  {'order': order, 'form':form})


@csrf_exempt
def payment_done(request):
	return render(request, 'payment/done.html')


@csrf_exempt
def payment_canceled(request):
	return render(request, 'payment/canceled.html')

@csrf_exempt
def payment_notification(request):
	# print('-----------------ATTENTION: PAYMENT NOTIFICATON--------------------------')
	# print(request.POST)

	# VERIFY_URL_PROD = 'https://www.paypal.com/cgi-bin/webscr'
	# VERIFY_URL_TEST = 'https://www.sandbox.paypal.com/cgi-bin/webscr'

	# # Switch as appropriate
	# VERIFY_URL = VERIFY_URL_TEST

	# # CGI preamble
	# print("content-type: text/plain")
	# print()

	# # Read and parse query string
	# param_str = sys.stdin.readline().strip()
	# params = urllib.parse.parse_qsl(param_str)

	# # Add '_notify-validate' parameter
	# params.append(('cmd', '_notify-validate'))

	# # Post back to PayPal for validation
	# headers = {'content-type': 'application/x-www-form-urlencoded', 'host': 'www.paypal.com'}
	# print('here')
	# r = requests.post(VERIFY_URL, params=params, headers=headers, verify=True)
	# r.raise_for_status()

	# # Check return message and take action as needed
	# if r.text == 'VERIFIED':
	#     print('verified')
	#     return HttpResponse('')
	# elif r.text == 'INVALID':
	#     print('invalid')
	# else:
	#     print('nor verified nor invalid')

	paypal_url = 'https://www.sandbox.paypal.com/cgi-bin/webscr'
	query = 'cmd=_notify-validate'
	for key, value in request.POST.items():
		query += '&%s=%s' % (key, urllib.parse.quote(value))
	res = requests.post(paypal_url, data=query, timeout=10)

	print(res.text)
	if res.text == 'VERIFIED':
		print('verified')
		# Extract POST variables here
		payment_status = request.POST.get('payment_status')
		if payment_status == 'Completed':
			# Successful payment
			print('completed')
			print(request.POST)
			return HttpResponse('')
		elif payment_status == 'Reversed' or payment_status == 'Refunded':
			# Payment reversed
			print('reversed or refunded')
			return HttpResponseForbidden()
	else:
		return HttpResponseForbidden()