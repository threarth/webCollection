from django.apps import AppConfig

from iommi.style import Style
from iommi import register_style
from iommi.style_bootstrap import bootstrap
from iommi.from_model import register_search_fields
#from .models import Tablist

my_style = Style(
	bootstrap,
	Container__attrs__style={'max-width': '100%',
		},

	# Table__attrs__style={'color': '#de513c'},
	# Form__attrs__style={'color': 'red'},
	# Fields__shortcuts__input__attrs__style={'width': '50%'},
	# h1__tag__style={'color': 'green'},

)

class SonglistConfig(AppConfig):
    name = 'songlist'

    def ready(self):
        from .models import Tablist
        register_style('my_style', my_style)
        register_search_fields(model=Tablist, search_fields=['id'])
        #register_search_fields(model=Tablist, search_fields=['artist'])
		#,'title','songbook','type','count','chords','study','rank'])
