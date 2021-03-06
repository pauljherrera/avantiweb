from django.conf.urls import url
from django.utils.translation import gettext_lazy as _

from . import views

urlpatterns = [
	url(_(r'^process/$'), views.payment_process, name='process'),
	url(_(r'^done/$'), views.payment_done, name='done'),
	url(r'^canceled/$', views.payment_canceled, name='canceled'),
	url(r'^notification/$', views.payment_notification, name='notification'),
	url(r'^ajax_check/$', views.payment_check, name='ajax_check'),
]