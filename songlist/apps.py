from django.apps import AppConfig

from iommi.style import Style
from iommi import register_style
from iommi.style_bootstrap import bootstrap

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
        register_style('my_style', my_style)
