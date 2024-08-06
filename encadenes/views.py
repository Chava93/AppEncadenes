from django.shortcuts import render
from django.views import generic

from django.http import HttpResponse,HttpResponseRedirect

from .models import Route, Sector, Crag

def mainView(request):
	return HttpResponse("<H1>Page for loggin ascent</H1>")

class RoutesView(generic.ListView):
	template_name = "encadenes/ListView.html"
	model = Route

class CragsView(generic.ListView):
	template_name = "encadenes/ListView.html"
	model = Crag
		