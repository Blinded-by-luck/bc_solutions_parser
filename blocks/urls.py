from django.urls import path

from .views import *

urlpatterns = [
	path('blocks/', BlocksView, name='blocks'), 
	path('blocks/block_<int:height>/', BlockView, name='block')
]