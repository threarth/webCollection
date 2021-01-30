from csv import DictReader
from .models import Tablist

def load_csv_to_Tablist(filename):
    with open(filename, "r", encoding="iso-8859-1", errors="ignore") as f:
        reader = DictReader(f, delimiter=";")
        l = []
        for line in reader:
            l.append(line)

        Tablist.objects.all().delete()

        for i in l:
            j = Tablist(
            id = int(i['id']),
            artist = i['artista'],
            title = i['titolo'],
            songbook = i['canzoniere'],
            type = i['tipo'],
            count = int(i['n']),
            chords = i['accordi'],
            to_study = i['da_studiare'],
            rank = int(i['rank']),
            db_name = i['db_name'],
            )
            j.save()
