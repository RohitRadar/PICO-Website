from django.conf.urls import url
from .import views

app_name='Ultrasonic'

urlpatterns=[
	url(r'^$', views.products, name='ultrasonic'),
	url(r'^(?P<slug>[\w-]+)/$', views.Prod, name='product'),
]
