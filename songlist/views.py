#from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
#from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
#from django.views import generic
from django.utils import timezone
from django.template import Template

#from django import forms

from .models import Song, Artist, Album, Track, Tablist

from iommi import (
    Page,
    Table,
    Column,
    Action,
    Fragment,
    html,
    Field,
    Form,
)

from iommi.style_bootstrap import bootstrap
from .csv_decode import load_open_file_to_Tablist

from django.conf import settings
from pathlib import Path
import os
import logging
import codecs

# for file uploading
CSV_FILE = os.path.join(settings.BASE_DIR, 'songlist/media/current_csv')

class FileForm(Form):
    filename = Field.file(attrs__style__color='blue', display_name='Seleziona file...')

    class Meta:
         @staticmethod
         def actions__submit__post_handler(form, **_):
             if not form.is_valid():
                 return

             if (form.get_request().method == 'POST'):
                 print(form.fields.filename.value)
                 print('Richiesta POST!')

                 request = form.get_request()
                 file = request.FILES['filename']

                 # with codecs.open(CSV_FILE, "wb+", "ISO-8859-1") as destination:
                 with open(CSV_FILE, 'wb+') as destination:
                     today = timezone.now()
                     date_string = f'date: {today.day}/{today.month}/{today.year}, {today.hour}:{today.minute}:{today.second}\n'
                     destination.write(date_string.encode('utf_8'))
                     for chunk in file.chunks():
                         destination.write(chunk)

                 return HttpResponseRedirect('update')

         attrs__class = {'container': True,}
         attrs__enctype = 'multipart/form-data'
         attrs__style = {'max-width': '100%'}
        # actions__submit__attrs__class = {'row': True,
        #                                  'btn-primary': False,
        #                                  'btn-outline-primary': True,}
         fields__filename__attrs__class = {'row': True,}


class UpdatePage(Page):
    title = html.h1('Carica il CSV...', attrs__class={'text-primary': True})
    file_form = FileForm()

    context = {'errors': "",
               'count': "",
               'date': "",
               'update': "",}
    content = Template("""
    <br>
       {% if date %}<div class="alert alert-info">file {{date}}</div>{% endif %}

    {% if errors %}
        <div class="alert alert-warning">{{errors}}</div>
    {% else %}
        {% if update %}
            <div class="alert alert-success">{{update}}</div>
        {% else %}
               <script>
                   function updateDB(){
                       let pass = "?pass=" + $('#input_pass').val();
                       alert('Se la parola chiave è corretta, ci vorranno alcuni minuti prima che il database sia aggiornato; per piacere, attendi senza ricaricare la pagina!')

                       window.location.search = pass;
                   }
               </script>
               <button class='btn btn-outline-primary' onclick='updateDB()'>Update DB</button>
               <input type='text' placeholder='Insert passphrase' id='input_pass'>
              <br><br>
        {% endif %}
        <div class="alert alert-success">Records found: {{count}}</div>
        <div class="alert alert-info">Content of CSV:</div>
        <div class="alert alert-light">{{dict}}</div>
    {% endif %}
    """)

def update_view(request):
    dict = []
    dict_len = 0
    errors = ""
    update_result = ""
    pass_string = ""
    date_string = ""
    bulk_array = []

    try:
        with open(CSV_FILE, "r", encoding="utf_8") as f:
            errors, date_string, dict, dict_len = load_open_file_to_Tablist(f)
    except IOError:
        errors = "CSV_FILE non disponibile.\n"

    query_string = request.META['QUERY_STRING']

    if (query_string):
        pass_string = request.GET['pass']

#    print(pass_string)

    if (pass_string == 'sierraUniform'):
        print('Updating DB!')
        Tablist.objects.all().delete()

        for i in dict:
             j = Tablist(
                 id = int(i['id']),
                 artist = i['artist'],
                 title = i['title'],
                 songbook = i['songbook'],
                 type = i['type'],
                 count = int(i['count']),
                 chords = i['chords'],
                 study = i['study'],
                 rank = int(i['rank']),
                 db_name = i['db_name'],
                 )
             bulk_array.append(j)

        Tablist.objects.bulk_create(bulk_array)
        update_result = 'Successful update!'
        print("Update Complete!")

    return UpdatePage(context__errors = errors, context__update = update_result, context__count = dict_len,
                      context__dict = dict, context__date = date_string)




class IndexPage(Page):
    custom_script = Fragment(template='songlist/custom_form.html')
#    file_form = FileForm()
    link = html.a('Update the DB!', attrs__href='update')
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
            <td class='cellContent'>
                <a href='http://www.grilliconsulting.com/a/music/viewer.html?id={{ row.id }}&db=all_all' target='_blank'>{{ row.title }}</a>
            </td>
         '''),

        #  container and header style attrs
        #  container__attrs__style={'max-width': '100%'},
        columns__id__header__attrs__style__width='3%',
        columns__artist__header__attrs__style__width='15%',
        columns__title__header__attrs__style__width='15%',
        columns__songbook__header__attrs__style__width='15%',
        columns__type__header__attrs__style__width='3%',
        columns__count__header__attrs__style__width='2%',
        columns__chords__header__attrs__style__width='27%',
        columns__study__header__attrs__style__width='18%',
        columns__rank__header__attrs__style__width='2%',

        #  query form other actions buttons
        #  query__form__fields__hidden1=Field.hidden(),

        #  query__form__fields__hidden1__attrs__style={'color': 'white',},
        #  query__form__fields__hidden1__input__attrs__style={'pointer-events': 'none;',
        #                                              'border': 'none',},

        query__form__actions__reset=Action.button(display_name='Reset', attrs_type='button', attrs__onclick='resetForm()', attrs__class={
                                                            'btn': True, 'btn-primary': True, 'btn-secondary': False,}),

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
