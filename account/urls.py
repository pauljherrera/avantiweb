from django.conf.urls import url, include
from django.contrib.auth import views as v

from . import views


urlpatterns = [
	url(r'^login/$', v.login, name='login'),
	url(r'^logout/$', v.logout, name='logged_out'),
	url(r'^logout-then-login/$', v.logout_then_login, name='logout_then_login'),
	url(r'^password-change/$', v.password_change, name='password_change'),
	url(r'^password-change/done/$',	v.password_change_done,
		name='password_change_done'),
	# restore password urls
	url(r'^password-reset/$', v.password_reset,	name='password_reset'),
	url(r'^password-reset/done/$', v.password_reset_done, 
		name='password_reset_done'),
	url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', 
		v.password_reset_confirm, name='password_reset_confirm'),
	url(r'^password-reset/complete/$', v.password_reset_complete, 
		name='password_reset_complete'),
	url(r'^register/$', views.register, name='register'),
]