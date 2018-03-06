from django.shortcuts import render


def home(request):
	return render(request, 'ComingSoon/index.html')
