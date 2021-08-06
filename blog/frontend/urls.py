from django.urls import path, re_path
from frontend import views

urlpatterns = [

	# The home page
	# owner page
	# view dashboard
	path('/', views.index, name='index'),
]