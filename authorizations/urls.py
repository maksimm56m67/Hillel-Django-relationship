from django.urls import path

from authorizations import views

urlpatterns = [
    path('login', views.authorization, name='login'),
    path('logout', views.logout_user, name='logout'),
]
