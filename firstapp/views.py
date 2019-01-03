from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from firstapp.models import firstapp_model
from firstapp.forms import Firstapp_forms
# Create your views here.

def index(request):
	context = {"data":firstapp_model.objects.all()}
	return render(request, "firstapp/index.html", context)


def post_new(request):
	


	form = Firstapp_forms()
	return render(request, "firstapp/form.html", {'form':form})

	