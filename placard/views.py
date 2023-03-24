from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils.text import slugify
from django.db.models import Q
from .models import *
from .forms import *


""" @login_required
def get_landing_page(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect('accounts/login') """


""" @login_required
def index(request):
    return render(request, 'index.html') """

"""
Reference for method decorator
https://player.uacdn.net/lesson-raw/W8VMBBPXM7RQRAAUXHGY/pdf/4571659735.pdf
"""


@method_decorator(login_required, name='dispatch')
class PersonaList(generic.ListView):
    """
    Class to show list of personas
    """
    model = Persona
    queryset = Persona.objects.order_by('created_on')
    template_name = 'index.html'
    paginate_by = 6


class PersonaDetail(View):
    """
    Class to show selected persona in detail view
    """

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
    """
    Class to add a Persona view to the list
    """
    model = Persona
    # form_class to style the view
    form_class = PersonaForm
    template_name = 'create_persona.html'
    # fields = ('shamefull_nickname', 'shameful_song', 'shameful_tv_show', 'shameful_habit', 'shameful_story', 'shameful_pic')
    success_url = reverse_lazy('home')
    """
    to make sure that the shamefull_nickname entry
    from the user is turned into a slug
    """
    prepopulated_fields = {'slug': ('shamefull_nickname',)}

    """
    to set the author field of the form instance
    to the current user before the form is saved.
    """

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Persona created successfully!')
        return super().form_valid(form)


class EditPersonaView(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'edit_persona.html'
    prepopulated_fields = {'slug': ('shamefull_nickname',)}
    success_url = reverse_lazy('home')

    """
    to get the original queryset of all Persona objects
    to filter onlyto include objects where the author
    matches the currently logged in user
    """

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Persona updated successfully!')
        return super().form_valid(form)


class DeletePersonaView(DeleteView):
    model = Persona
    template_name = 'delete_persona.html'
    success_url = reverse_lazy('home')


def PersonaSearch(request):
    """
    To search with keywords a persona
    """
    q = request.Get.get('q')

    results = []
    if q:
        results = Post.objects.filter(Q(shamefull_nickname__icontains=q) | Q(shameful_song__icontains=q) | Q(shameful_tv_show__icontains=q) | Q(shameful_habit__icontains=q) | Q(shameful_story__icontains=q))
        return render(request, 'search.html', {
            'q': q, 'results': results
            })


