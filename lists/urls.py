from django.conf.urls import url
from lists import views

urlpatterns = [
	url(r'^new$', views.view_new_list, name='view_new_list'),
	url(r'^(\d+)/$', views.view_list, name='view_list'),
]
