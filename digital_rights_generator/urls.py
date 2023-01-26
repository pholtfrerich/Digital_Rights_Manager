from django.urls import path
from . import views

urlpatterns = [
    path('', views.digital_rights_generator, name='digital_rights_generator')
]