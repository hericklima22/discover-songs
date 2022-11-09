from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def musicas(request):
  return HttpResponse("Musicas")