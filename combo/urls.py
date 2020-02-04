from django.contrib import admin
from django.urls import path,include

from .import views





app_name = "combo"
urlpatterns = [
   	path('',views.list, name='list'),
   	path('new/',views.new, name ='new'),
   	path('<int:pk>/poll/',views.polldetail, name='polldetail'),
   	path('<int:question_id>/results/', views.results, name='results'),
   	path('<int:pk>/vote/',views.vote, name='vote'),
   	path('<int:pk>/edit/', views.edit, name='edit'),
	path('<int:pk>/',views.detail, name='detail'),	
	path('poll/',views.poll, name='poll'),
	
	



]



