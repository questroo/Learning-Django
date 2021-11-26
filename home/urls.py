from django.contrib import admin
from django.urls import path, include
from home import views

# Django admin header customization

admin.site.site_header = "My Awesome Admin"
admin.site.site_title = "My Awesome Site Secret Section"
admin.site.index_title = "My Title"

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
]
