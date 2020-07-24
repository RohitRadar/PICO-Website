from django.conf.urls import url
from .import views

app_name='Decade_Resistance_Box'

urlpatterns=[
	url(r'^$', views.products, name='Decade_Resistance_Box'),
	url(r'^(?P<slug>[\w-]+)/$', views.Prod, name="product"),
]
