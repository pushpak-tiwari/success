from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'pushpak/home.html', {})

def aboutme(request):
	return render(request, 'pushpak/aboutme.html', {})

def contactme(request):
	return render(request, 'pushpak/contactme.html', {})

def languages(request):
	return render(request, 'pushpak/languages.html', {})
