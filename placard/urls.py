from . import views
from django.urls import path


urlpatterns = [
    path('', views.PersonaList.as_view(), name='home'),
    path('persona_detail/<slug:slug>/', views.PersonaDetail.as_view(), name='persona_detail'),
    path('like/<slug:slug>', views.PersonaLike.as_view(), name='persona_like'),
    path('create_persona/', CreatePersonaView.as_view(), name='create_persona'),
]
