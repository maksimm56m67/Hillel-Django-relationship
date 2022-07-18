from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import ListView, CreateView

from task.forms import CommentForm, CommentModelForm, RatingModelForm
from task.models import Task, Comment, Rating


def index(request):
	return render(request, 'base.html')


class TaskView(ListView):

	def get(self, *args, **kwargs):
		print('GET', args, kwargs)



@login_required(login_url='login')
def get_all_tasks(request):
	context = {
		'tasks': Task.objects.order_by('status', '-id'),
		'title': 'All tasks',
		'is_authenticated': request.user.is_authenticated,
		'user': request.user
	}
	return render(request, 'all.html', context)
	# tasks = Task.objects.order_by('status', '-id')
	# response = f'<h1>Всего задач найдено {len(tasks)}<br></h1>'
	# for task in tasks:
	# 	response += f'{task.title} {task.status}<br>'
	# return HttpResponse(response)


@login_required(login_url='login')
def get_all_tasks_by_status(request, status):
	tasks = Task.objects.filter(status=status)
	response = f'<h1>Всего задач найдено {len(tasks)}<br></h1>'
	for task in tasks:
		response += f'{task.title}<br>'
	return HttpResponse(response)


@login_required(login_url='login')
def get_task_detail(request, task_id):
	try:
		task = Task.objects.get(id=task_id)
	except Task.DoesNotExist:
		return HttpResponse(f'Задачи с номером {task_id} не существует!')
	ratings = Rating.objects.filter(task_id=task_id).order_by('-id').all()
	context = {
		'title': task.title,
		'task': task,
		'comments': Comment.objects.filter(task_id=task_id).order_by('-id').all(),
		'rattings': Rating.objects.filter(task_id=task_id).order_by('-id').all(),
		'rating': round(sum([int(x.point) for x in ratings]) / len(ratings), 2),
		'comment_form': CommentModelForm(),
		'rating_form': RatingModelForm(),
		'is_authenticated': request.user.is_authenticated,
		'user': request.user

	}
	return render(request, 'detail.html', context)


@login_required(login_url='login')
def comment_views(request, task_id):
	if request.method == 'POST':
		form = CommentModelForm(request.POST)
		if form.is_valid():
			Comment.objects.create(
				user=request.user,
				text=form.data['text'],
				task_id=task_id
			)
		return redirect(request.headers.get('Referer'))  # Вернуть пользователя на пред. страницу
	else:
		return redirect('all_tasks')


@login_required(login_url='login')
def rating_views(request, task_id):
	if request.method == 'POST':
		form = RatingModelForm(request.POST)
		if form.is_valid():
			Rating.objects.create(
				user=request.user,
				point=form.data['point'],
				task_id=task_id
			)
		return redirect(request.headers.get('Referer'))  # Вернуть пользователя на пред. страницу
	else:
		return redirect('all_tasks')

"""
Задание:

Создать приложение articles с помощью команды python manage.py startapp articles
Создать модель Article с полями:
 * id
 * title
 * content
 * creator_name
 * updated_at
 * created_at

Создать 2 запроса
/articles - который возвращает заголовки всеъ статей
/articles/detail/<int:article_id> - который возвращает content статьи по ид

Код необходимо загрузить в github репозиторий
"""

