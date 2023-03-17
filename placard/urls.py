from . import views
from django.urls import path


urlpatterns = [
    path('persona_list.html/', views.PersonaList.as_view(), name='persona-list')
]