# Here is the views file
from django.shortcuts import render
# import


def home(request):
	import json
	import requests

	api_request = requests.get("https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=89129&date=2025-09-05&distance=10&API_KEY=72A00659-85BF-4F88-B8A2-08FBDC90795E")
	
	try:
		api = json.loads(api_request.content)
	except Exception as e:
		api="Error..."
	return render(request, 'home.html', {'api': api})

def about(request):
	return render(request, 'about.html', {})