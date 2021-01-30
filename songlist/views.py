from django.shortcuts import render

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
    #th_Study{width: 18%;}
    #th_Rank{width: 2%;}
    ''')

    tablist = Table(
        auto__model = Tablist,
        page_size = 100,
    #   hide
        columns__db__render_column=False,
        columns__db_name__render_column=False,
        columns__db_source__render_column=False,

    #   filters
        columns__id__filter__include=True,
        columns__artist__filter__include=True,
        columns__title__filter__include=True,
        columns__songbook__filter__include=True,
        columns__type__filter__include=True,
        columns__count__filter__include=True,
        columns__chords__filter__include=True,
        columns__study__filter__include=True,
        columns__rank__filter__include=True,
        columns__title__cell__template=Template('''
            <td>
                <a href='http://www.grilliconsulting.com/a/music/viewer.html?id={{ row.id }}&db=all_all' target='_blank'>{{ row.title }}</a>
            </td>
         '''),

        header__template=Template('''
             <script>
             function resetForm(){
                 document.querySelectorAll('input[type=text]').forEach(x => x.value="")
                 var evt = document.createEvent("HTMLEvents");
                 evt.initEvent("change", false, true);
                 $("form")[0].dispatchEvent(evt);
             }
             </script>
             <br>
             <div class="btn-group">
                <button id="id_reset" class="btn btn-primary" type="button" onclick="resetForm()" title="Reset">Reset
                </button>
             </div>
             <br><br>
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
         '''),
      )


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
