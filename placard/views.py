from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import *


class PersonaList(generic.ListView):
    model = Persona
    queryset = Persona.objects.order_by('created_on')
    template_name = 'index.html'
    paginate_by = 6


class PersonaDetail(View):

    def get(self, request, *args, **kargs):
        persona = get_object_or_404(slug=slug)
        comments = persona.comments.all()
        Liked = False
        if persona.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "persona": persona,
                "comments": comments,
                "likes": liked
            },
        )
