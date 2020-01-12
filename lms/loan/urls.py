from django.urls import path
from django.conf.urls import url
from .views import CreateApplication, ListApplications, UpdateApplication, DeleteApplication

urlpatterns = [
	path('create/', CreateApplication.as_view(), name="create-application"),
	path('list/', ListApplications.as_view(), name="list-application"),
	url(r'^update/(?P<pk>[0-9]+)/$', UpdateApplication.as_view(), name="update-application"),
	url(r'^delete/(?P<pk>[0-9]+)/$', DeleteApplication.as_view(), name="delete-application"),
]