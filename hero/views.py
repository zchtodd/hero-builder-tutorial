from django.shortcuts import render


def home(request):
    return render(request, "hero/home.html")
