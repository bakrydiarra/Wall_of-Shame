from . import views
from django.urls import path
from .views import PersonaList


urlpatterns = [
    path('persona_list.html/', views.PersonaList.as_view(), name='persona-list')
]