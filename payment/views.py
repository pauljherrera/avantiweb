from decimal import Decimal
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.contrib.auth.models import User

import sys
import urllib.parse
import requests
import json

from common.decorators import ajax_required
from orders.models import Order
from courses.models import Course

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
	
	print(request.user.username)
	print(request.session)
	return render(request, 'payment/done.html')

@ajax_required
def payment_check(request):
	# Checking if the last order was already paid.
	if request.user.is_authenticated():
		if request.user.orders.all()[0].paid:
			print('ok')
			return JsonResponse({'status': 'ok'})
		else:
			print('ko')
			return JsonResponse({'status': 'ko'})
	else:
		return JsonResponse({'status': 'no_session'})




@csrf_exempt
def payment_canceled(request):
	return redirect('courses:strategies')

@csrf_exempt
def payment_notification(request):
	# Adding command for the response.
	data = b'cmd=_notify-validate&'
	data += request.body

	# Posting verification.
	verification = requests.post('https://ipnpb.sandbox.paypal.com/cgi-bin/webscr', data=data)
	print(verification.text)

	#Checking verification
	if verification.text == 'VERIFIED':
		# process IPN
		print(request.POST)

		payment_status = request.POST.get('payment_status')
		if payment_status == 'Completed':
			# Successful payment
			print('completed')
			data = request.POST.get('custom').split(',')
			user_id = int(data[0])
			order_id = int(data[1])

			#Order as completed.
			order = Order.objects.filter(pk=order_id)[0]
			order.paid = True
			order.save()

			#Enrolling user.
			user = User.objects.filter(pk=user_id)[0]
			course = order.product.course
			#In the bought course.
			course.students.add(user)
			#In the other courses.
			c = Course.objects.filter(pk=1)[0]
			c.students.add(user)
			if course.id > 2:
				c = Course.objects.filter(pk=2)[0]
				c.students.add(user)


		elif payment_status == 'Reversed' or payment_status == 'Refunded':
			# Payment reversed
			print('reversed or refunded')

		return HttpResponse('')
	else:
		return HttpResponseForbidden()


	