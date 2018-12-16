from pathlib import Path
from urllib.parse import urlencode
import csv
DATA_PATH = Path('.', 'static', 'data.csv')

def get_records():
    with DATA_PATH.open('r') as f:
        return list(csv.DictReader(f))

def get_record_by_id(id):
    return next(r for r in get_records() if r['id'] == id)

STREET_VIEW_ENDPOINT = 'https://maps.googleapis.com/maps/api/streetview'
def make_google_streetview_url(x, y):
    loc = '{0},{1}'.format(y, x)
    params = {'size': '700x400', 'location': loc}
    url = STREET_VIEW_ENDPOINT + '?' + urlencode(params)
    return url

MAP_VIEW_ENDPOINT = 'https://maps.googleapis.com/maps/api/staticmap'
def make_google_map_url(x, y):
    loc = '{0},{1}'.format(y, x)
    params = {'size': '700x400', 'markers': loc, 'zoom': 12}
    url = MAP_VIEW_ENDPOINT + '?' + urlencode(params)
    return url
