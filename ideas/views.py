from django.shortcuts import render

from .models import Idea

# Create your views here.


def index(request):
    return render(request, "ideas/index.html", {"ideas": Idea.objects.all()})


def idea(request, idea_id):
    idea = Idea.objects.get(pk=idea_id)
    return render(request, "ideas/idea.html", {"idea": idea})
