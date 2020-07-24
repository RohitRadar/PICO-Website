from django.shortcuts import render, HttpResponse
from .models import Halleffect
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
def ok_to_load_in_a_frame(request):
    return HttpResponse("This page is safe to load in a frame on any site.")

def products(request):
	types = Halleffect.objects.all()
	return render(request,'halleffect/Products.html', {'types':types})

def Prod(request, slug):
	appname={'name':'Hall Effect'}
	details = Halleffect.objects.get(slug=slug)
	types = Halleffect.objects.all()
	return render(request, 'halleffect/ProductPage.html', {'details':details, 'types':types, 'appname':appname})

