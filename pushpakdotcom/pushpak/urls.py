from django.urls import path
from . import views 

urlpatterns = [
	path('home/',views.home, name='home'),
	path('aboutme/',views.aboutme, name='aboutme'),	
	path('contactme/',views.contactme, name='contactme'),
	path('languages/',views.languages, name='languages'),

]
