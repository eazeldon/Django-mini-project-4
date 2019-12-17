from django.shortcuts import render,get_object_or_404, redirect
from .models import home
from .forms import Djangoproject4Forms

# Create your views here.
def get_index(request):
    """A view that displays the index page"""
    return  render(request, "index.html")

def get_contact(request):
    return  render(request, "contact.html")

def get_about(request):
    return  render(request, "about.html")