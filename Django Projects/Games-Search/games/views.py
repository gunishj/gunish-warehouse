from django.http import HttpResponse
from django.shortcuts import render
from .models import Games


def index(request):
    games = Games.objects.all()
    return render(request, 'index.html', {'games': games})
# Create your views here.


def database_search(request):
    return HttpResponse("search the name you wish to search")


def game_detail_view(request):
    #  games = Games.objects.get(id=98)
    games = Games.objects.filter(id=9)
    return render(request, 'index.html', {'games': games})


# cities/views.py


from django.views.generic import TemplateView, ListView
from django.db.models import Q

class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsView(ListView):
    model = Games
    template_name = 'search_results.html'

    def get_queryset(self):  # new
        #  return Games.objects.filter(title__icontains='Wild')  # new
        query = self.request.GET.get('q')
        return Games.objects.filter(Q(title__icontains=query) | Q(score__icontains=query))

    #  queryset = Games.objects.filter(title__icontains='Wild')  # new




