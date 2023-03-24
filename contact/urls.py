from . import views
from .views import *
from django.urls import path


urlpatterns = [
    path('contact/', CreateContactView.as_view(), name='contact')
]
