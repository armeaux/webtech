from django.shortcuts import render
from django.utils import timezone
from .models import Task
import json
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url="login/")
def home(request):
	tasks = Task.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	return render(request,"home.html", {'tasks': Task.objects.all})
	current_user = request.user



def ajax(request):
	if request.method == 'POST':
		post_text = request.POST.get('the_post')

		post=Task()
		post.title=post_text
		post.author=request.user
		post.created_date=timezone.now()
		post.priority='middle'
		post.category='default'
		post.save()

		response_data = 'Create post successful nigga!'

		return HttpResponse(
			json.dumps(response_data),
			content_type="application/json"
		)
	else:
		return HttpResponse(
			json.dumps({"nothing to see": "this isn't happening"}),
			content_type="application/json"
		)
