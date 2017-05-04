from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.admin.views.decorators import staff_member_required

from .models import Order, Product
from .forms import OrderCreateForm
from .tasks import order_created

# Create your views here.
def order_create(request, pk):
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order = form.save(commit=False)
			order.owner = request.user
			order.product = Product.objects.filter(pk=request.session['product_id'])[0]
			order.save()
			request.session['order_id'] = order.id
			request.session['product_id'] = pk

			return redirect(reverse('payment:process'))
	else:
		request.session['product_id'] = pk
		form = OrderCreateForm()

	return render(request, 'orders/order/create.html',
				  {'form': form, 'product_id': pk})


@staff_member_required
def admin_order_detail(request, order_id):
	order = get_object_or_404(Order, id=order_id)

	return render(request, 'admin/orders/order/detail.html',
				  {'order': order})
