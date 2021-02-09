from django.urls import path
from django.shortcuts import render

from . import views
from .models import Tablist
from iommi import Table


app_name = 'songlist' # this adds songlist namespace to following urls and prevents
                   # name collision

urlpatterns = [
    # ex: /polls/
    path('main', Table(auto__model=Tablist, title="Canzoniere!").as_view(), name='index'),
    path('', views.IndexPage().as_view()),
    path('update', views.update_view, name='update'),
    path('update?pass=sierraUniform', views.update_view, name='update_db'),

    # ex: /polls/5
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #
    # # ex: /polls/5/results
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
