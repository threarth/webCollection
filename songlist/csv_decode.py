import io
from csv import DictReader
from .models import Tablist

def load_csv_to_Tablist(filename):
    with open(filename, "r", encoding="iso-8859-1", errors="ignore") as f:
        load_open_file_to_Tablist(f)
        # reader = DictReader(f, delimiter=";")
        # l = []
        # for line in reader:
        #     l.append(line)
        #
        # Tablist.objects.all().delete()
        #
        # for i in l:
        #     j = Tablist(
        #     id = int(i['id']),
        #     artist = i['artista'],
        #     title = i['titolo'],
        #     songbook = i['canzoniere'],
        #     type = i['tipo'],
        #     count = int(i['n']),
        #     chords = i['accordi'],
        #     to_study = i['da_studiare'],
        #     rank = int(i['rank']),
        #     db_name = i['db_name'],
        #     )
        #     j.save()

must_have_keys = ('id', 'artist', 'title',
               'songbook', 'type', 'count',
               'chords', 'study', 'rank',
               'db_name')

def load_open_file_to_Tablist(file):
    keep_output = ""
    change_output = ""

    date_string = file.readline().strip()

#    reader = DictReader(io.StringIO(file.read()code('iso-8859-1')), delimiter=";")
    reader = DictReader(io.StringIO(file.read()), delimiter=";")

    l = []
    for line in reader:
        l.append(line)



    new_keys = tuple(l[0].keys())

    if (must_have_keys != new_keys):
        error_msg = f'Error! CSV must include the following exact keys: {str(must_have_keys)}<br>\n'
        error_msg += f'But you submitted a CSV with the following keys: {str(new_keys)}\n'

        return (error_msg, date_string, None, 0)

    else:
        return ("", date_string, l, len(l))

    for i in l:
        change = False
        db_elem = Tablist.objects.filter(id=i['id'])[0]

        for k in must_have_keys:
            original = getattr(db_elem, k)
            new = i[k]
            if (str(original) != str(new)):
                print('Original: ' + str(original) + "; " + "New: " + str(new))
                change = True

        if (change):
            change_output += "I'm gonna changing #ID " + i['id'] + '!\n'

            for k in must_have_keys:
                setattr(db_elem, k, i[k])
                db_elem.save()
        else:
            keep_output += "I'm keeping #id" + i['id'] + ' as is!\n'

    return (change_output, keep_output)
#    Tablist.objects.all().delete()

    # for i in l:
    #     j = Tablist(
    #     id = int(i['id']),
    #     artist = i['artista'],
    #     title = i['titolo'],
    #     songbook = i['canzoniere'],
    #     type = i['tipo'],
    #     count = int(i['n']),
    #     chords = i['accordi'],
    #     to_study = i['da_studiare'],
    #     rank = int(i['rank']),
    #     db_name = i['db_name'],
    #     )
    #     j.save()
