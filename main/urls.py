from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.first_html),
    path('process', views.random_int)
    
]