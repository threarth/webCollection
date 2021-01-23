from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
#from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Song, Artist, Album, Track, Tablist

from iommi import (
    Table,
    Column,
)

class AlbumsTable(Table):
    title = Column()
    artist = Column()
    chords = Column()
    pattern = Column()
    fpath = Column()
    note = Column()

    class Meta:
        title = 'Canzoniere'
        rows = Tablist.objects.all()


# def index(request):
#     return AlbumsTable(
#         title='Albums',
#         rows=Album.objects.all(),
#     )

# def index(request):
#     return render(
#         request,
#         template_name='songlist/index.html',
#         context=dict(
#             title='Canzoniere 2.0 realizzato con Django e Iommi in Python!',
#             content=AlbumsTable(
#                 rows=Album.objects.all(),
#             ).bind(request=request),
#         )
#     )

#
#
# class IndexView(generic.ListView):
#     model = Song
#     template_name = 'songlist/index.html'

    # ovveride default context from question_list to latest_question_list
#    context_object_name = 'latest_question_list'

    # def get_queryset(self):
    #     """
    #     Return the last five published questions
    #     not including those set to be published in the future
    #     """
    #     return Question.objects.filter(
    #         pub_date__lte=timezone.now()
    #     ).order_by('-pub_date')[:5]

# class DetailView(generic.DetailView):
#     model = Question
#     # change default template_name from polls/question_detail.html
#     template_name = 'polls/detail.html'
#
#     def get_queryset(self):
#         """
#         Excludes any questions that aren't published yet.
#         """
#         return Question.objects.filter(pub_date__lte=timezone.now())
#
# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'
#
#
# # def index(request):
# #     latest_question_list = Question.objects.order_by('-pub_date')[:5]
# #
# #     context = {'latest_question_list': latest_question_list,}
# #     return render(request, 'polls/index.html', context)
# #
# #
# # def detail(request, question_id):
# #     question = get_object_or_404(Question, pk=question_id)
# #     return render(request, 'polls/detail.html', {'question': question})
# #
# # def results(request, question_id):
# #     response = "You,re looking at the results of question %s."
# #     return HttpResponse(response % question_id)
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#
#     try:
#         selected = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # redisplay the question voting form.
#         return render(request, 'polls/detail.html',
#         {
#             'question': question,
#             'error_message': "You didn't select a choice."
#         })
#     else:
#         selected.votes += 1
#         selected.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
