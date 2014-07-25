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

def do_search(query):
    query = query.copy()
    # 'location_metro' => 'location.metro' for 3taps.com
    for ukey in (key for key in query.iterkeys() if '_' in key):
        dotkey = '.'.join( ukey.split('_') )
        query[dotkey] = query.pop(ukey)

    url = format_url(query)
    return url, json.loads( urllib.urlopen(url).read() )


class TTapsResult(object):
    def __init__(self, **kwargs):
        self.query = kwargs
        self.url, self.block = do_search(self.query)


    def __iter__(self):
        return iter(self.block)


    def __getitem__(self, key):
        return self.block[key]


    
# XXXXX: doesnt work: category_group='JJJJ',
# count='category_group', # X: count mode
# source='CRAIG',
# price='..500',
# source='CRAIG'


for term in ['python','java','django','php']:
    result = TTapsResult(
        category='JWEB|JCON|JENG',
        heading=term,
        count='category_group', # X: count mode
        location_metro='USA-LAX',
        retvals='external_url,heading,category,category_group,status,price',
    )
    if 'postings' in result:
        print '{:10} {}'.format(term, len(result['postings']))
        pprint(result.block); continue
        for post in result['postings']:
            if 1:
                pprint(post)
            else:
                print post['heading']
    else:
        print '{:12} {:3d}'.format(
            term,
            result.block['num_matches'],
            )


