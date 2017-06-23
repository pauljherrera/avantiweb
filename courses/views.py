from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import TemplateResponseMixin, View
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.db.models import Count
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
import os

from common.decorators import ajax_required
from .forms import ModuleFormSet, QuestionForm
from account.forms import UserEditForm
from .models import Course, Module, Questions
from account.models import Profile

# Create your views here.
@login_required
def plans(request):
	u = request.user
	# Redirect to the strategies views if the user is already 
	# enrolled in a course.
	if u.courses_joined.all():
		return redirect('courses:strategies')

	# Checks if the e-mail and names are already registered.
	if bool(u.email) & bool(u.first_name) & bool(u.last_name):
		completeRegistration = True
		form = False
	else:
		obj = get_object_or_404(User, pk=request.user.id)
		form = UserEditForm(instance=obj)
		completeRegistration = False

	return render(request, 'courses/complete_registry.html', {'complete_registration' : completeRegistration,
												  'form' : form})




@login_required
def enroll(request, course_id):
	course = Course.objects.filter(id=1)[0] #Only used for free course enrollment.
	course.students.add(request.user)

	return redirect('courses:strategies')


class CourseListView(LoginRequiredMixin, TemplateResponseMixin, View):
	model = Course
	template_name = 'courses/strategies.html'

	def get(self, request, subject=None):
		if not request.user.courses_joined.all():
			return redirect('courses:plans')
			
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

	print('courses/content/{}_{}.html'.format(course, module))

	return render(request, 'courses/content/{}_{}.html'.format(course, 
															   module))


@ajax_required
def get_ajax_promotion(request):
	course = request.GET['course']

	return render(request, 'courses/content/promotion_{}.html'.format(course))


@ajax_required
@require_http_methods(['POST'])
def post_question(request):
	question = Questions(question=request.POST.get('question'), 
						 owner=request.user)
	question.save()

	# Sending email to client-support.
	send_mail('Answer to your question', 
			  'Usuario: {} \nPregunta: {}'.format(request.user.username, request.POST.get('question')),
			  request.user.email,
			  ['services@avantifs.com'])

	return JsonResponse({'status': 'ok'})


@login_required
def download_indicator_mt4(request):
	file_path = os.path.join(settings.PROJECT_ROOT, 'static/courses/files', 'Knoxville_Divergence.ex4')
	if os.path.exists(file_path):
		with open(file_path, 'rb') as fh:
			response = HttpResponse(fh.read(), content_type="application/octet-stream")
			response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)

	return response


@login_required
def download_indicator_ctrader(request):
	file_path = os.path.join(settings.PROJECT_ROOT, 'static/courses/files', 'Knoxville_Divergence.algo')
	if os.path.exists(file_path):
		with open(file_path, 'rb') as fh:
			response = HttpResponse(fh.read(), content_type="application/octet-stream")
			response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)

	return response


@login_required
def download_ea_mt4(request):
	file_path = os.path.join(settings.PROJECT_ROOT, 'static/courses/files', 'SMA_Knoxville.ex4')
	if os.path.exists(file_path):
		with open(file_path, 'rb') as fh:
			response = HttpResponse(fh.read(), content_type="application/octet-stream")
			response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)

	return response


@login_required
def download_ea_ctrader(request):
	file_path = os.path.join(settings.PROJECT_ROOT, 'static/courses/files', 'SMA_Knoxville.algo')
	if os.path.exists(file_path):
		with open(file_path, 'rb') as fh:
			response = HttpResponse(fh.read(), content_type="application/octet-stream")
			response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)

	return response

@ajax_required
@require_http_methods(['POST'])
def save_registration_data(request):
	user = get_object_or_404(User, id=request.user.id)
	data = request.POST
	user.first_name = data['id_first_name']
	user.last_name = data['id_last_name']
	user.email = data['id_email']
	user.save()

	return JsonResponse({'status': 'ok'})
