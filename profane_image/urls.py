from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'profane_image'
urlpatterns = [
    path('', views.index, name = 'index'),
]