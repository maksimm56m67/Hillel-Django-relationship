from django import forms

from task.models import Comment, Rating


class CommentForm(forms.Form):
	text = forms.CharField(max_length=2000)
	choices = forms.ChoiceField(
		choices=[
			('issues', 'Issues'),
			('comment', 'Comment')
		]
	)


class CommentModelForm(forms.ModelForm):
	class Meta:
		model = Comment  # Название модели
		fields = ['text']  # Список полей  '__all__'


class RatingModelForm(forms.ModelForm):
	class Meta:
		model = Rating
		fields = ['point']
		labels = {
			'point': 'Rate'
		}

