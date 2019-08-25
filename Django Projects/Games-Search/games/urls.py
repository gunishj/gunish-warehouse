from django.urls import path
from . import views


from .views import HomePageView, SearchResultsView


# / products
# /products
urlpatterns = [path('', views.index), path('db', views.database_search), path('db1', views.game_detail_view),

               path('search/', SearchResultsView.as_view(), name='search_results'),
               path('home', HomePageView.as_view(), name='home'),
               ]

