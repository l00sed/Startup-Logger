from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Idea


class NewIdeaForm(forms.Form):
    idea_name = forms.CharField(label="New Idea")
    idea_description = forms.CharField(widget=forms.Textarea)


# Create your views here.


def index(request):
    return render(request, "ideas/index.html", {"ideas": Idea.objects.all()})


def idea(request, idea_id):
    idea = Idea.objects.get(pk=idea_id)
    return render(request, "ideas/idea.html", {"idea": idea})


def add(request):
    if request.method == "POST":
        form = NewIdeaForm(request.POST)
        if form.is_valid():
            idea_name = form.cleaned_data["idea_name"]
            idea_description = form.cleaned_data["idea_description"]
            idea = Idea(name=idea_name, description=idea_description)
            idea.save()
            return HttpResponseRedirect(reverse("ideas:index"))
        else:
            return render(request, "ideas/add.html", {"form": form})
    return render(request, "ideas/add.html", {"form": NewIdeaForm()})
