from . import views
from django.urls import path


urlpatterns = [
    path('', views.PersonaList.as_view(), name='home'),
    path('persona_detail/<slug:slug>/', views.PersonaDetail.as_view(), name='persona_detail'),
]
