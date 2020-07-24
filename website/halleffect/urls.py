from django.conf.urls import url
from .import views

app_name='halleffect'

urlpatterns=[
	url(r'^$', views.products, name='halleffect'),
	url(r'^(?P<slug>[\w-]+)/$', views.Prod, name='product'),
]
