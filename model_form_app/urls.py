
from django.urls import path
from . import views

urlpatterns = [
    path("model/",views.model_form,name='model_form')
]
