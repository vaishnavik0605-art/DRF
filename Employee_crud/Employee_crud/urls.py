"""
URL configuration for Employee_crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.contrib.syndication import views
from django.urls import path,include
from django.views import View

from app import views

from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('employees',views.EmployeeView)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include(router.urls)),
    path('search',views.SearchAPI.as_view()), #search
    path('register',views.RegisterView.as_view()),  #register



    # path('create',views.EmployeeCreate.as_view()),
    # path('list',views.EmployeeList.as_view()),
    # path('details/<int:pk>',views.EmployeeDetails.as_view()),
    # path('put/<int:pk>',views.EmployeeUpdate.as_view()),
    # # path('patch/<int:pk>',views.EmployeePartialUpdate.as_view()),
    # path('delete/<int:pk>',views.EmployeeDelete.as_view()),
]
