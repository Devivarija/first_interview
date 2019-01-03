from django.urls import path
from firstapp import views


urlpatterns = [

				path('', views.index, name = 'index'),
				path('post/new', views.post_new, name ='post_new')
				
				]