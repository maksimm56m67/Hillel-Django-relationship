from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from authorizations.forms import UserForm


def authorization(request):
	context = {
		'form': UserForm(),
		'error': None,
		'is_authenticated': request.user.is_authenticated,
		'user': request.user
	}
	if request.method == 'GET':
		return render(request, 'login.html', context)
	if request.method == 'POST':
		form = UserForm(request.POST)
		user = authenticate(
			username=form.data['username'],
			password=form.data['password']
		)
		if user is None:
			context['error'] = 'Invalid username or password'
			return render(request, 'login.html', context)
		else:
			login(request, user)
			return redirect('all_tasks')


def logout_user(request):
	logout(request)
	return redirect('login')
