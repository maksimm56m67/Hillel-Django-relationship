from django.urls import path

from task import views

urlpatterns = [
    path('test/', views.TaskView.as_view(), name='test'),
    path('', views.get_all_tasks, name='all_tasks'),  # localhost:8000/tasks/
    path('comment/<int:task_id>', views.comment_views, name='comment'),  # localhost:8000/tasks/<int:task_id>/comment
    path('rating/<int:task_id>', views.rating_views, name='rating'),  # localhost:8000/tasks/rating
    path('<str:status>', views.get_all_tasks_by_status),  # localhost:8000/tasks/all/
    path('detail/<int:task_id>', views.get_task_detail),  # localhost:8000/tasks/detail/13
	# path('путь', views.функция, имя_запроса)
]
