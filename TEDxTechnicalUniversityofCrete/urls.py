"""TEDxTechnicalUniversityofCrete URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include, re_path

from TEDx2018 import views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('2017/', include(('TEDx2017.urls', 'TEDx2017'), namespace='TEDx2017')),
	path('', include(('TEDx2018.urls', 'TEDx2018'), namespace='TEDx2018')),
	# path('', include(('ComingSoon.urls', 'ComingSoon'), namespace='ComingSoon')),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += staticfiles_urlpatterns()
handler404 = 'TEDx2018.views.custom_404'
handler500 = 'TEDx2018.views.custom_500'
urlpatterns += [
	re_path(r'(?P<path>.*)', views.custom_404View, name='custom404')
]
