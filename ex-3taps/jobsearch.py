import json, os, urllib
from pprint import pprint

# http://docs.3taps.com/search_api.html

def format_url(argdict):
    return 'http://search.3taps.com/?auth_token={}&{}'.format(
        os.environ['API_3TAPS_KEY'],
        urllib.urlencode(argdict),
        )

# source='CRAIG'

def search(**kwargs):
    # 'location_metro' => 'location.metro' for 3taps.com
    for ukey in (key for key in kwargs.iterkeys() if '_' in key):
        dotkey = '.'.join( ukey.split('_') )
        kwargs[dotkey] = kwargs.pop(ukey)

    url = format_url(kwargs)
    print url
    data = urllib.urlopen(url).read()
    return json.loads(data)
    


block = search(
    heading='accordion',
    location_metro='USA-LAX',
    source='CRAIG',
    )
for post in block['postings']:
    pprint(post)


