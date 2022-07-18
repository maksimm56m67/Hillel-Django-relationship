from django.urls import path

from articles import views

urlpatterns = [
    path('', views.get_all_articles),
    path('detail/<int:article_id>', views.get_article_detail),
]
