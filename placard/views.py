from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import *
from .forms import CommentForm


class PersonaList(generic.ListView):
    model = Persona
    queryset = Persona.objects.order_by('created_on')
    template_name = 'index.html'
    paginate_by = 6


class PersonaDetail(View):

    def get(self, request, slug, *args, **kargs):
        queryset = Persona.objects
        persona = get_object_or_404(queryset, slug=slug)
        comments = persona.comments.all()
        liked = False
        if persona.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "persona_detail.html",
            {
                "persona": persona,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
