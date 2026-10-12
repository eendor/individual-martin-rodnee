# The urls.py file in a Django app is where you define the URL patterns for the todolist application

# Import path to define URL patterns for routing requests to view functions
from django.urls import path

# Import views to connect URL paths to the view functions defined in views.py
from . import views

app_name = 'todolist'

# urlpatterns is a list that hold the URL patterns
# Each pattern maps a specific URL path to view a function

urlpatterns = [
	# path() is a function used to define a URL pattern
	# route: the URL pattern as string
	# view: the function that handles the request
	# optional name: used to refer to this URL elsewhere
	path("", views.index, name="index"),
	# <int:todoitem_id> captures an integer from the URL and passes it to the view
	path("<int:todoitem_id>/", views.todoitem, name="viewtodoitem"),
	path("register", views.register, name="register"),
	path("change_password", views.change_password, name="change_password"),
	path("login", views.login_view, name="login"),
	path("logout", views.logout_view, name="logout"),
	path("add_task", views.add_task, name="add_task"),
]