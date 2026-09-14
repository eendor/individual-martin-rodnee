# The views.py file in a Django app contains the view functions that define what should happen when a user visits a specific URL

from django.shortcuts import render
# Import HttpResponse to allow returning plain text or HTML content directly from a view
from django.http import HttpResponse


# A view function in Django accepts an HTTP request object as a parameter
def index(request):
	# The function returns an HttpResponse object containing the content you want to send back to the client.
	return HttpResponse("Hello from views.py file.")
