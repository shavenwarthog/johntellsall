import json, os, urllib
from pprint import pprint

# http://docs.3taps.com/search_api.html

def format_url(argdict):
    return 'http://search.3taps.com/?auth_token={}&{}'.format(
        os.environ['API_3TAPS_KEY'],
        urllib.urlencode(argdict),
        )


def search(**kwargs):
    url = format_url(kwargs)
    data = urllib.urlopen(url).read()
    return json.loads(data)
    


block = search(location='los angeles')
for post in block['postings']:
    pprint(post)


