from django.http import HttpResponse


def index(request):
    return HttpResponse("Ceci est le début d'un jeu d'aventure")

