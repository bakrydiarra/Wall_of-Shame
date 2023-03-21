from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from .models import *
from .forms import CommentForm


def get_landing_page(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect('accounts/login')


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

    def post(self, request, slug, *args, **kargs):
        queryset = Persona.objects
        persona = get_object_or_404(queryset, slug=slug)
        comments = persona.comments.all()
        liked = False
        if persona.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.persona = persona
            comment.save()
        else:
            comment_form = CommentForm()

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


class PersonaLike(View):

    def post(self, request, slug):
        persona = get_object_or_404(Persona, slug=slug)

        if persona.likes.filter(id=request.user.id).exists():
            persona.likes.remove(request.user)
        else:
            persona.likes.add(request.user)

        return HttpResponseRedirect(reverse('persona_detail', args=[slug]))


class CreatePersonaView(CreateView):
    model = Persona
    template_name = 'create_persona.html'
    fields = ('shamefull_nickname', 'shameful_song', 'shameful_tv_show', 'shameful_habit','shameful_story', 'shameful_pic')
