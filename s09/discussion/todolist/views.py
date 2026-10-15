# The views.py file in a Django app contains the view functions that define what should happen when a user visits a specific URL

from django.shortcuts import render, redirect, get_object_or_404
from django.forms.models import model_to_dict
# Import HttpResponse to allow returning plain text or HTML content directly from a view
from django.http import HttpResponse
from .models import ToDoItem
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from .forms import LoginForm, AddTaskForm, UpdateTaskForm


# A view function in Django accepts an HTTP request object as a parameter
def index(request):
	# The function returns an HttpResponse object containing the content you want to send back to the client.
	# return HttpResponse("Hello from views.py file.")
	todoitem_list = ToDoItem.objects.filter(user_id=request.user.id)
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

	form = LoginForm(request.POST or None)

	context = { "form": form }

	if request.method == 'POST':

		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user = authenticate(username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect("todolist:index")
			else:
				context["error"] = "Invalid username or password"

	return render(request, "todolist/login.html", context)

	# username = "johndoe"
	# password = "johndoe1"

def logout_view(request):
	logout(request)
	return redirect("todolist:index")

# View function to add a task
def add_task(request):
	# Initialize the AddTaskForm.
	# If POST data is present (form submitted), bind it to the form for validation.
	form = AddTaskForm(request.POST or None)

	# Create a context dictionary to send the form and other data to the template.
	context = {"form": form}

	# Check if the request came from a form submission (POST method).
	if request.method == 'POST':
		# Validate the submitted data according to the form's rules.
		if form.is_valid():
			# Extract validated data (cleaned data) from the form fields.
			task_name = form.cleaned_data['task_name']
			description = form.cleaned_data['description']

			# Check if a task with the same name already exists for the logged-in user.
			# This prevents duplicate task names per user.
			if not ToDoItem.objects.filter(task_name=task_name, user=request.user).exists():
				# Create a new task record in the database.
				# 'timezone.now()' sets the current date and time automatically.
				# 'user=request.user' links the task to the currently logged-in user.
				ToDoItem.objects.create(
					task_name=task_name,
					description=description,
					date_created=timezone.now(),
					user=request.user
				)
				# After successful creation, redirect the user to the ToDoList index page.
				return redirect("todolist:index")
			else:
				# If a duplicate task name is found, add an error message to the context.
				context["error"] = "A task with this name already exists."

	# Render the "add_task.html" template with the form and context data.
	return render(request, "todolist/add_task.html", context)

def update_task(request, todoitem_id):
	todoitem = ToDoItem.objects.get(pk=todoitem_id, user=request.user)
	form = UpdateTaskForm(request.POST or None)

	context = {
		'form': form,
		'todoitem': todoitem,
		'task_name': todoitem.task_name,
		'description': todoitem.description,
		'status': todoitem.status,
	}

	if request.method == 'POST':
		if form.is_valid():
			task_name = form.cleaned_data['task_name']
			description = form.cleaned_data['description']
			status = form.cleaned_data['status']

			todoitem.task_name = task_name
			todoitem.description = description
			todoitem.status = status
			todoitem.save()

			return redirect("todolist:index")
		else:
			context["error"] = "Please correct the errors below"

	return render(request, "todolist/update_task.html", context)

def delete_task(request, todoitem_id):
	todoitem = ToDoItem.objects.filter(id=todoitem_id, user=request.user)
	todoitem.delete()
	return redirect("todolist:index")

