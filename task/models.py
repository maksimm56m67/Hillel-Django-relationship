from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    OPEN_STATUS = 'open'
    TASK_STATUSES = (
        (OPEN_STATUS, 'Open'),
        ('in_progress', 'In progress'),
        ('done', 'Done'),
    )

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)  # Текстовое поле
    description = models.TextField()  # Текстовое поле
    status = models.CharField(
        max_length=20,
        choices=TASK_STATUSES,
        default=OPEN_STATUS,
    )  # Текстовое поле с возможность выбора
    # Дата и время которая задается автоматически при изменении записи
    updated_at = models.DateTimeField(auto_now=True)
    # Дата и время которая задается автоматически при создании записи
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


class Rating(models.Model):
    # @TODO Связать рейтинг с задачами(одна задача, но рейтингов много)
    # @TODO Связать рейтинг с пользователями(один пользыватель, но много рейтингов)
    id = models.AutoField(primary_key=True)
    point = models.CharField(max_length=20, choices=(
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ))

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'оценка:{self.point}, {self.user}, {self.task}'


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.task}, {" ".join(self.text.split(" ")[:4])}...'
