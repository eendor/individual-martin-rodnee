# The views.py file in a Django app contains the view functions that define what should happen when a user visits a specific URL

from django.shortcuts import render, redirect, get_object_or_404
from django.forms.models import model_to_dict
# Import HttpResponse to allow returning plain text or HTML content directly from a view
from django.http import HttpResponse
from .models import ToDoItem
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# A view function in Django accepts an HTTP request object as a parameter
def index(request):
	# The function returns an HttpResponse object containing the content you want to send back to the client.
	# return HttpResponse("Hello from views.py file.")
	todoitem_list = ToDoItem.objects.all()
	context = {
		'todoitem_list': todoitem_list,
		'user': request.user,
	}
	return render(request, "todolist/index.html", context)

def todoitem(request, todoitem_id):
	# %s is a placeholder replaced by todoitem_id
	# return HttpResponse("You are viewing the details of %s" % todoitem_id)
	todoitem = get_object_or_404(ToDoItem, pk=todoitem_id)
	context = model_to_dict(todoitem)
	context['user'] = request.user
	return render(request, "todolist/todoitem.html", context)

def register(request):
	is_user_registered = User.objects.filter(username="johndoe")

	if not is_user_registered:
		user = User.objects.create_user(
			username="johndoe",
			first_name="John",
			last_name="Doe",
			email="john@mail.com",
			password="john1234"
		)

		user.save()

		context = {
			"first_name": user.first_name,
			"last_name": user.last_name,
			"is_user_registered": False
		}
	else:
		context = {
			"is_user_registered": True
		}

	return render(request, "todolist/register.html", context)

def change_password(request):
	is_user_authenticated = False
	user = authenticate(username="johndoe", password="john1234")
	print(user)

	if user is not None:
		authenticated_user = User.objects.get(username="johndoe")
		authenticated_user.set_password("johndoe1")
		authenticated_user.save()
		is_user_authenticated = True

	context = {
		"is_user_authenticated": is_user_authenticated
	}

	return render(request, "todolist/change_password.html", context)

def login_view(request):
	username = "johndoe"
	password = "johndoe1"
	user = authenticate(username=username, password=password)
	context = {
		"is_user_authenticated": False
	}
	print(user)

	if user is not None:
		login(request, user)
		return redirect("index")
	else:
		return render(request, "todolist/login.html", context)

def logout_view(request):
	logout(request)
	return redirect("index")

