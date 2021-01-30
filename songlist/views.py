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
from django.template import Template

from .models import Song, Artist, Album, Track, Tablist

from iommi import (

    Page,
    Table,
    Column,
    html,
)

class TabTable(Table):

    id = Column()
    artist = Column()
    title = Column()
    songbook = Column()
    type = Column()
    count = Column()
    chords = Column()
    to_study = Column()
    rank = Column()

    class Meta:
        title = "Canzoniere"
        rows = Tablist.objects.all()
        page_size = 100
#   filters
        columns__id__filter__include=True
        columns__artist__filter__include=True
        columns__title__filter__include=True
        columns__songbook__filter__include=True
        columns__rank__filter__include=True
        columns__count__filter__include=True
        columns__type__filter__include=True
        columns__chords__filter__include=True
        columns__to_study__filter__include=True

        columns__title__cell__template=Template('''
            <td>
                <a href='http://www.grilliconsulting.com/a/music/viewer.html?id={{ row.id }}&db=all_all' target='_blank'>{{ row.title }}</a>
            </td>
         ''')
#        header__template__th_width_list = {"th_width_list": "2"}
        header__template=Template('''
             <thead>
                 {% for headers in table.header_levels %}
                 <tr>
                 {% for header in headers %}
                         <th id=th_{{ header.display_name }}>
                             {% if header.url %}
                                 <a href="{{ header.url }}">
                             {% endif %}
                             {{ header.display_name }}
                             {% if header.url %}
                                 </a>
                             {% endif %}
                         </th>
                     {% endfor %}
                     </tr>
                     {% endfor %}
             </thead>
         ''')


#     auto__model=Tablist
#     page_size=100
#
#     columns__title__cell__template=Template('''
#         <td>
#             <a href='http://www.grilliconsulting.com/a/music/viewer.html?id={{ row.id }}&db=all_all' target='_blank'>{{ row.title }}</a>
#         </td>
#     '''),
# #    columns__title__cell__url=lambda row, **_: row.get_absolute_url(),
# #    columns__chords__cell__template=Template('''
# #        <td style="color:red">{{ row.chords }}
# #        </td>
# #    '''),
# #   columns to render and order of columns
#     columns__db__render_column=False
#     columns__db_name__render_column=False
#     columns__db_source__render_column=False
#     columns__title__after = 'artist'
#
#
# #    columns__rank__filter__include=True,


class IndexPage(Page):
    container_style = html.style(".container{max-width:100%;}")
    th_style = html.style('''
    #th_Id{width: 3%;}
    #th_Artist{width: 15%;}
    #th_Title{width: 15%;}
    #th_Songbook{width: 15%;}
    #th_Type{width: 3%;}
    #th_Count{width: 2%;}
    #th_Chords{width: 27%;}
    #th_To_study{width: 18%;}
    #th_To_rank{width: 2%;}
    ''')
    tablist = TabTable()
    #attrs__div="style: max-width: 100%;"

#    table = Tablist()

#    parts__tablist__context = {"th_width_list": "prova"}

#    parts__tablist__query__form__fields__rank__input__attrs=('prova')



class SonglistTable(Table):
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
