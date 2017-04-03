from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^strategies/$', views.CourseListView.as_view(), name='strategies'),
	url(r'^ajax/content', views.get_ajax_content, name='get_content'),
	url(r'^ajax/question', views.post_question, name='post_question'),
]
