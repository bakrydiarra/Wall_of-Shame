from . import views
from .views import *
from django.urls import path


urlpatterns = [
    path('', views.PersonaList.as_view(), name='home'),
    path('contact/', CreateContactView.as_view(), name='contact')
  
]