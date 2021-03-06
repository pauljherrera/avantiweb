from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
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


def main(request):
	if request.user.is_authenticated():
		return redirect('courses:strategies')
		
	return render(request, 'account/login.html')


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

			return render(request, 'account/register_done.html',
						  {'new_user': new_user})
	else:
		user_form = UserRegistrationForm()
	
	return render(request, 'account/register.html',
				  {'user_form': user_form})

def terms(request):
	return render(request, 'account/terms.html')



