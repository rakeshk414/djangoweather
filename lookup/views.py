# Here is the views file
from django.shortcuts import render
# import


def home(request):
	return render(request, 'home.html', {})

def about(request):
	return render(request, 'about.html', {})