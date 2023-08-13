from django.urls import path
from .views import home, character

urlpatterns = [
    path("", home, name="home"),
    path("character", character, name="character"),
    path("character/<int:character_id>/", character, name="character_with_id"),
]
