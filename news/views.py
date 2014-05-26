from django.shortcuts import render_to_response
from django.http import HttpResponse
# Create your views here.
import models

def myFirstview(request):
	return HttpResponse('Ola Mundo!')