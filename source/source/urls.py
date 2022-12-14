"""source URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from webapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>', ProductView.as_view(), name='product_view'),
    path('add/', ProductCreate.as_view(), name='add'),
    path('<int:pk>/edit', ProductUpdate.as_view(), name='edit'),
    path('<int:pk>/delete', ProductDelete.as_view(), name='delete'),
    path('<int:pk>/', add_to_cart_view, name='cart_add'),
    path('cart/', CartView.as_view(), name='cart_view'),
]
