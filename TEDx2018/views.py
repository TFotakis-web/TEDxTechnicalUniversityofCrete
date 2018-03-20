from django.shortcuts import render

from TEDx2018.models import Event


def home(request):
	events = Event.objects.order_by('-StartDateTime')
	return render(request=request, template_name='TEDx2018/home.html', context={'events': events})


def about(request):
	return render(request=request, template_name='TEDx2018/about.html')


def custom_404(request):
	return render(request=request, template_name='TEDx2018/404.html')


def custom_500(request):
	return render(request=request, template_name='TEDx2018/500.html')
