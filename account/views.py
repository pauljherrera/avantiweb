from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from braces.views import LoginRequiredMixin

from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .forms import CourseEnrollForm
from .models import Profile, Contact
from courses.models import Course
from common.decorators import ajax_required
from actions.utils import create_action
from actions.models import Action


def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'],
								password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponse('Authenticated succesfully')
				else:
					return HttpResponse('Disabled account')
			else:
				return HttpResponse('Invalid login')
	else:
		form = LoginForm()

	return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
	# Display all actions by default
	actions = Action.objects.exclude(user=request.user)
	following_ids = request.user.following.values_list('id', flat=True)
	
	if following_ids:
		# If user is following others, retrieve only their actions
		actions = actions.filter(user_id__in=following_ids)\
						 .select_related('user', 'user__profile')\
						 .prefetch_related('target')
		actions = actions[:10]

	return render(request, 'account/dashboard.html', {'section': 'dashboard',
													  'actions': actions})


def register(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			# Create a new user object but avoid saving it yet
			new_user = user_form.save(commit=False)
			# Set the chosen password
			new_user.set_password(user_form.cleaned_data['password'])
			# Save the User object
			new_user.save()
			profile = Profile.objects.create(user=new_user)
			create_action(new_user, 'has created an account')

			return render(request, 'account/register_done.html',
						  {'new_user': new_user})
	else:
		user_form = UserRegistrationForm()
	
	return render(request, 'account/register.html',
				  {'user_form': user_form})


@login_required
def edit(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user,
								 data=request.POST)
		profile_form = ProfileEditForm(instance=request.user.profile,
									   data=request.POST,
									   files=request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, 'Profile updated succesfully')
		else:
			messages.error(request, 'Error updating your profile')
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)
		
	return render(request,	'account/edit.html',
				  {'user_form': user_form, 'profile_form': profile_form})


@login_required
def user_list(request):
	users = User.objects.filter(is_active=True)
	return render(request, 'account/user/list.html',
				  {'section': 'people',	'users': users})


@login_required
def user_detail(request, username):
	user = get_object_or_404(User, username=username, is_active=True)
	return render(request, 'account/user/detail.html',
				  {'section': 'people',	'user': user})


@ajax_required
@require_POST
@login_required
def user_follow(request):
	user_id = request.POST.get('id')
	action = request.POST.get('action')
	if user_id and action:
		try:
			user = User.objects.get(id=user_id)
			if action == 'follow':
				Contact.objects.get_or_create(
					user_from=request.user,
					user_to=user)
				create_action(request.user, 'is following', user)
			else:
				Contact.objects.filter(user_from=request.user,
									   user_to=user).delete()
			return JsonResponse({'status':'ok'})
		except User.DoesNotExist:
			return JsonResponse({'status':'ko'})
	return JsonResponse({'status':'ko'})


class StudentEnrollCourseView(LoginRequiredMixin, FormView):
	course = None
	form_class = CourseEnrollForm

	def form_valid(self, form):
		self.course = form.cleaned_data['course']
		self.course.students.add(self.request.user)
		return super(StudentEnrollCourseView, self).form_valid(form)

	def get_success_url(self):
		return reverse_lazy('account:student_course_detail', args=[self.course.id])


class StudentCourseListView(LoginRequiredMixin, ListView):
	model = Course
	template_name = 'account/course/list.html'

	def get_queryset(self):
		qs = super(StudentCourseListView, self).get_queryset()
		return qs.filter(students__in=[self.request.user])


class StudentCourseDetailView(DetailView):
	model = Course
	template_name = 'account/course/detail.html'

	def get_queryset(self):
		qs = super(StudentCourseDetailView, self).get_queryset()
		return qs.filter(students__in=[self.request.user])

	def get_context_data(self, **kwargs):
		context = super(StudentCourseDetailView, self).get_context_data(**kwargs)
		# get course object
		course = self.get_object()
		if 'module_id' in self.kwargs:
			# get current module
			context['module'] = course.modules.get(
									id=self.kwargs['module_id']
								)
		else:
			# get first module
			context['module'] = course.modules.all()[0]
		return context
