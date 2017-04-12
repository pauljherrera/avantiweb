from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^plans/$', views.plans, name='plans'),
	url(r'^strategies/$', views.CourseListView.as_view(), name='strategies'),
	url(r'^ajax/content', views.get_ajax_content, name='get_content'),
	url(r'^ajax/promotion', views.get_ajax_promotion, name='get_promotion'),
	url(r'^ajax/question', views.post_question, name='post_question'),
	url(r'^enroll/(?P<course_id>\d+)/$', views.enroll, name='enroll'),
]
