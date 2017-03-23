from django.conf.urls import url, include
from django.contrib.auth import views as v

from . import views


urlpatterns = [
	# post views
	#url(r'^login/$', views.user_login, name='login'),
	url(r'^login/$', v.login, name='login'),
	url(r'^logout/$', v.logout, name='logged_out'),
	url(r'^logout-then-login/$', v.logout_then_login, name='logout_then_login'),
	url(r'^$', views.dashboard, name='dashboard'),
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
	url(r'^edit/$', views.edit, name='edit'),
	url(r'^users/$', views.user_list, name='user_list'),
	url(r'^users/follow/$', views.user_follow, name='user_follow'),
	url(r'^users/(?P<username>[-\w]+)/$', views.user_detail,
		name='user_detail'),
	url(r'^enroll-course/$', views.StudentEnrollCourseView.as_view(),
		name='student_enroll_course'),
	url(r'^courses/$', views.StudentCourseListView.as_view(),
		name='student_course_list'),
	url(r'^course/(?P<pk>\d+)/$', views.StudentCourseDetailView.as_view(),
		name='student_course_detail'),
	url(r'^course/(?P<pk>\d+)/(?P<module_id>\d+)/$',
		views.StudentCourseDetailView.as_view(),
		name='student_course_detail_module'),
]