from django.conf.urls import url
from django.utils.translation import gettext_lazy as _

from . import views

urlpatterns = [
	url(_(r'^plans/$'), views.plans, name='plans'),
	url(_(r'^strategies/$'), views.CourseListView.as_view(), name='strategies'),
	url(r'^ajax/content', views.get_ajax_content, name='get_content'),
	url(r'^ajax/promotion', views.get_ajax_promotion, name='get_promotion'),
	url(r'^ajax/question', views.post_question, name='post_question'),
	url(r'^enroll/(?P<course_id>\d+)/$', views.enroll, name='enroll'),
	url(r'^indicator_mt4/$', views.download_indicator_mt4, name='download_indicator_mt4'),
	url(r'^indicator_ctrader/$', views.download_indicator_ctrader, name='download_indicator_ctrader'),
	url(r'^ea_mt4/$', views.download_ea_mt4, name='download_ea_mt4'),
	url(r'^ea_ctrader/$', views.download_ea_ctrader, name='download_ea_ctrader'),
]
