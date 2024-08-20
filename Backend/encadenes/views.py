from django.shortcuts import render
from django.views import generic

from django.http import HttpResponse,HttpResponseRedirect

from .models import Route, Sector, Crag

def mainView(request):
	return HttpResponse("<H1>Page for loggin ascent</H1>")

class RoutesView(generic.ListView):
	template_name = "encadenes/ListView.html"
	model = Route
	title = "Rutas"
	def get_context_data(self, **kwargs):
	    # Call the base implementation first to get a context
	    context = super().get_context_data(**kwargs)
	    context["title"] = self.title
	    return context

class CragsView(generic.ListView):
	template_name = "encadenes/ListView.html"
	model = Crag
	title = "Crags"
	def get_context_data(self, **kwargs):
	    # Call the base implementation first to get a context
	    context = super().get_context_data(**kwargs)
	    context["title"] = self.title
	    return context

class SectorsView(generic.ListView):
	template_name = "encadenes/ListView.html"
	model = Sector
	title = "Sectors"
	def get_context_data(self, **kwargs):
	    # Call the base implementation first to get a context
	    context = super().get_context_data(**kwargs)
	    context["title"] = self.title
	    return context
		