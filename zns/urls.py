"""zns URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from zns_project.views import *


router = routers.SimpleRouter()
router.register(r'contacts', ContactsViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))  # http://127.0.0.1:8000/api/v1/contacts
    # path('api/v1/contactslist/', ContactsViewSet.as_view({'get': 'list'})),
    # path('api/v1/contactslist/<int:pk>/', ContactsViewSet.as_view({'put': 'update'}))
]
