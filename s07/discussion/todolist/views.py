# The views.py file in a Django app contains the view functions that define what should happen when a user visits a specific URL

from django.shortcuts import render
# Import HttpResponse to allow returning plain text or HTML content directly from a view
from django.http import HttpResponse
from .models import ToDoItem


# A view function in Django accepts an HTTP request object as a parameter
def index(request):
	# The function returns an HttpResponse object containing the content you want to send back to the client.
	# return HttpResponse("Hello from views.py file.")
	todoitem_list = ToDoItem.objects.all()
	context = {'todoitem_list': todoitem_list}
	return render(request, "todolist/index.html", context)

def todoitem(request, todoitem_id):
	# %s is a placeholder replaced by todoitem_id
	return HttpResponse("You are viewing the details of %s" % todoitem_id)
