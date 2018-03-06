from django.shortcuts import render


def home(request):
	return render(request, 'TEDx2018/home.html')


def about(request):
	return render(request, 'TEDx2018/about.html')
