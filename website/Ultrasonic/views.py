from django.shortcuts import render, HttpResponse
from .models import Ultrasonic
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
def ok_to_load_in_a_frame(request):
    return HttpResponse("This page is safe to load in a frame on any site.")

def products(request):
	types = Ultrasonic.objects.all()
	return render(request,'Ultrasonic/Products.html', {'types':types})

def Prod(request, slug):
	appname={'name':'Ultrasonic'}
	details = Ultrasonic.objects.get(slug=slug)
	types = Ultrasonic.objects.all()
	return render(request, 'Ultrasonic/ProductPage.html', {'details':details, 'types':types, 'appname':appname})

