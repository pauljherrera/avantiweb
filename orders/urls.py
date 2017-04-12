from django.conf.urls import url
from django.utils.translation import gettext_lazy as _

from . import views

urlpatterns = [
	url(_(r'^create/(?P<pk>[0-9]+)$'), views.order_create, name='order_create'),
	url(r'^admin/order/(?P<order_id>\d+)/$', views.admin_order_detail,
		name='admin_order_detail'),
]