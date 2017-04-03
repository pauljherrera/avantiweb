from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import TemplateResponseMixin, View
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.db.models import Count
from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from common.decorators import ajax_required
from .forms import ModuleFormSet, QuestionForm
from .models import Course, Module, Questions
from account.models import Profile

# Create your views here.
class CourseListView(LoginRequiredMixin, TemplateResponseMixin, View):
	model = Course
	template_name = 'courses/strategies.html'

	def get(self, request, subject=None):
		courses = Course.objects.annotate(total_modules=Count('modules'))
		courses_joined = [c.id for c in request.user.courses_joined.all()]
		form = QuestionForm()

		return self.render_to_response({'courses': courses,
										'courses_joined': courses_joined,
										'form': form})	


@ajax_required
def get_ajax_content(request):
	course = request.GET['course']
	module = request.GET['module']

	profile = Profile.objects.filter(user_id=request.user.id)[0]
	profile.course_bookmark = course
	profile.module_bookmark = module
	profile.save()

	return render(request, 'courses/content/{}_{}.html'.format(course, 
															   module))


@ajax_required
@require_http_methods(['POST'])
def post_question(request):
	question = Questions(question=request.POST.get('question'), 
						 owner=request.user)
	question.save()

	return JsonResponse({'status': 'ok'})

