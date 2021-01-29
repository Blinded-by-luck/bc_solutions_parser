from django.urls import path

from .views import *

urlpatterns = [
	path('', BlocksView, name='blocks')
]