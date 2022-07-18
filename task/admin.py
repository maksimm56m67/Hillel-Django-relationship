from django.contrib import admin
from task.models import *

admin.site.register(Task)
admin.site.register(Rating)
admin.site.register(Comment)

