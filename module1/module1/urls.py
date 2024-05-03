"""
URL configuration for module1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
# from . import views

# urlpatterns = [
#     path("admin/", admin.site.urls),

#     # http://127.0.0.1:8000/hello/
#     path('hello/', views.hello_world, name='hello_world'),
# ]

from django.contrib import admin
from django.urls import path
from django.urls import path, include    # Import include module
from . import views

urlpatterns = [
    # Add view function for the root URL
    path('', views.home, name='home'),

    # http://127.0.0.1:8000/about/
    path('about/', views.about, name='about'),

    # http://127.0.0.1:8000/contact/
    path('contact/', views.contact, name='contact'),
]
