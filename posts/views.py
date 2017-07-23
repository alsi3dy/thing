from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import Post
from django.shortcuts import get_object_or_404
# Create your views here.

def post_create(request):
	return render(request,'create.html' ,{})
"""render takes three parameters request, 
name of html page, and dictionary"""
def post_update(request):
	return HttpResponse("<h1> World </h1>") 

def post_delete(request):
	return HttpResponse("<h1> Delete </h1>") 

def post_detail(request):
	return HttpResponse("<h1> Detail </h1>")

def post_list(request):
	return HttpResponse("<h1> List </h1>") 

def post_bye(request):
	return render(request, 'bye.html' , {})

def post_why(request):
	return render(request, 'why.html' , {})

def post_sassy(request):
	return render(request, 'sassy.html' , {})

def post_dict(request):
	post_group = Post.objects.all()
	post_second_group = Post.objects.all()[0:2]
	post_instance = Post.objects.all()[0]
	context = {
		"title" : "Post Page",
		"content" : "asdfasdfasdfsdf",
		
		"listt" : post_group,
		"list_2" : post_second_group,
		"inst" : post_instance,
	}

	return render (request, 'experiment.html', context)

def post_i(request, post_id):
	obj = get_object_or_404(Post, id = post_id)

	contexts = {
	"inp" : obj,
	}
	return render (request, 'id.html', contexts) 



	