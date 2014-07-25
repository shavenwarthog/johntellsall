import json, os, urllib
from pprint import pprint

# http://docs.3taps.com/search_api.html

# http://reference.3taps.com/category_groups
# http://reference.3taps.com/categories

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
    data = urllib.urlopen(url).read()
    return json.loads(data)
    

for term in ['python','java','django','php']:
    block = search(
        # XXXXX: doesnt work: category_group='JJJJ',
        category='JWEB|JCON|JENG',
        count='category_group', # X: count mode
        heading=term,
        location_metro='USA-LAX',
        # source='CRAIG',
        # price='..500',
        retvals='external_url,heading,category,category_group,status,price',
    )
    if 'postings' in block:
        print '{:10} {}'.format(term, len(block['postings']))
        for post in block['postings']:
            if 1:
                pprint(post)
            else:
                print post['heading']
    else:
        print term,':'
        pprint(block)


