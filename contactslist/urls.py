"""contactslist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from contact import views as viewsContact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', viewsContact.home, name='home'),
    path('add-contact/', viewsContact.add_contact, name='add-contact'),
    path('edit-contact/<str:pk>', viewsContact.edit_contact, name='edit-contact'),
    path('contact-edited/<str:pk>', viewsContact.contact_edited, name='contact-edited'),
    path('delete-contact/<str:pk>', viewsContact.delete_contact, name='delete-contact'),
    path('contact-deleted/', viewsContact.contact_deleted, name='contact-deleted'),
    path('profile/<str:pk>', viewsContact.contact_profile, name='profile'),
    path('contact-profile/<str:pk>', viewsContact.contact_profile, name='contact-profile'),
]
