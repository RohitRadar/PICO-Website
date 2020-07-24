from django.shortcuts import render, HttpResponse
from .models import photogallery
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def ok_to_load_in_a_frame(request):
    return HttpResponse("This page is safe to load in a frame on any site.")


def gallery(request):
	photos = photogallery.objects.all()
	return render(request,'gallery.html', {'photos':photos})


