from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from .models import *
from .forms import *


class CreateContactView(CreateView):

    """
    class to show a contact form
    """

    model = ContactForm
    form_class = EnquiryForm
    template_name = 'contact.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Your message has been sent successfully!')
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'Please fill up the form completely.')
        return response
