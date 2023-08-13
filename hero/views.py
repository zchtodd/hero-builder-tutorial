from django.shortcuts import render, redirect, get_object_or_404
from .models import Character
from .forms import CharacterForm


def home(request):
    form = CharacterForm()
    return render(request, "hero/home.html", {"form": form})


def character(request, character_id=None):
    if request.method == "POST":
        form = CharacterForm(request.POST)
        if form.is_valid():
            character = Character(
                strength=form.cleaned_data["strength"],
                dexterity=form.cleaned_data["dexterity"],
                health=form.cleaned_data["health"],
                intelligence=form.cleaned_data["intelligence"],
                charisma=form.cleaned_data["charisma"],
            )
            character.save()
            return redirect("character_with_id", character_id=character.pk)
    else:
        character = get_object_or_404(Character, id=character_id)

    return render(request, "hero/character.html", {"character": character})
