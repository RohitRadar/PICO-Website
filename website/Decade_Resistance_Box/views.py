from django.shortcuts import render, HttpResponse
from .models import Decade_Resistance_Box
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
def ok_to_load_in_a_frame(request):
    return HttpResponse("This page is safe to load in a frame on any site.")

def products(request):
	types = Decade_Resistance_Box.objects.all()
	return render(request,'DRB/Products.html', {'types':types})

def Prod(request, slug):
	appname={'name':'Decade_Resistance_Box'}
	details = Decade_Resistance_Box.objects.get(slug=slug)
	types = Decade_Resistance_Box.objects.all()
	return render(request, 'DRB/ProductPage.html', {'details':details, 'types':types, 'appname':appname})

