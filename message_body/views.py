from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from .models import MessagePost

class Homepage(ListView):
    model = MessagePost
    template_name = 'home.html'
    context_object_name = 'all_message_body_list'
