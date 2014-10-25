#!/usr/bin/env python

'''
dsearch.py -- search for interesting Django questions
'''
# http://api.stackexchange.com/docs/advanced-search

import datetime

import stackexchange


HOUR = 60*60

def format_age(age):
    hours = age.seconds / HOUR
    if age.days > 0:
        return 'x'
    elif hours > 12:
        return 'd'
    elif hours == 0:
        return '**'
    return '{:02d}'.format(hours)


def format_num(num):
    return num if num < 1000 else '!!'


def calc_awesome(q):
    return (
        q.view_count 
        + q.up_vote_count 
        + 5*q.favorite_count
        - (5 * (q.age.seconds/HOUR)**2)
        )


def annotate(res, now_dt):
    for q in res:
        q.age = now_dt - q.creation_date
        q.awesome = calc_awesome(q)


def print_res(res, now_dt):
    annotate(res, now_dt)

    day_td = datetime.timedelta(days=1)
    res = [ q for q in res if q.age < day_td ]

    print 'awe hr ^^ viw fav ans'
    for q in sorted(
            res, 
            key=lambda qq: qq.awesome,
            reverse=True,
    )[:15]:
        print '{:3} {:2} {:2d} {:>3} {:3d} {:3}  {}'.format(
            q.awesome,
            format_age(q.age),
            q.up_vote_count,
            format_num(q.view_count),
            q.favorite_count,
            q.json.get('answer_count', '?'),
            q.title,
        )

def main():

    so = stackexchange.Site(stackexchange.StackOverflow)
    res = list( so.search(
            q='django',
        tagged='django',
            closed=False,
    )[:100] )

    print_res(res, now_dt=datetime.datetime.now())


if __name__=='__main__':
    main()
