from django.shortcuts import render


def home(request):
	return render(request, 'TEDx2018/home.html')


def about(request):
	return render(request, 'TEDx2018/about.html')


def custom_404(request):
	return render(request, 'TEDx2018/404.html')


def custom_500(request):
	return render(request, 'TEDx2018/500.html')
