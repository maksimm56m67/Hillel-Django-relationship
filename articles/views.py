from django.http import HttpResponse
from django.shortcuts import render

from articles.models import Article


def get_all_articles(request):
	articles = Article.objects.all()
	response = ', '.join([x.title for x in articles])

	# response = ''
	# for article in articles:
	# 	response += f'{article.title},'

	return HttpResponse(response)


def get_article_detail(request, article_id):
	try:
		article = Article.objects.get(id=article_id)
	except Article.DoesNotExist:
		return HttpResponse('Такой статьи нет')
	return HttpResponse(article.content)
