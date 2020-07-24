from django.shortcuts import render, redirect
from.models import Homepage
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def ok_to_load_in_a_frame(request):
    return HttpResponse("This page is safe to load in a frame on any site.")

def home(request):
	homepages = Homepage.objects.all()
	return render(request,'home.html', {'homepages':homepages})
