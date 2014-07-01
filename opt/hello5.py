'''
INSTALL:
	sudo apt-get install python-scipy
	sudo apt-get install pyflakes python-django
'''

import sys
sys.path.insert(0, '/usr/lib/python2.7/dist-packages/') # scipy

import os, multiprocessing, random, subprocess, time

import hyperopt
hp = hyperopt.hp

SAMPLE_SIZE = 5

def p_title():
    print 'CONC ELAPSED\tTIME PER PROC'

def p_sample(conc, elapsed):
    print '{:4}\t{:4.2}\t{:.2}'.format(
        conc, elapsed, elapsed/conc,
        )

def objective(concurrency):
    '''
    run several jobs in parallel, return elapsed clock time
    '''
    paths = random.sample(PATHS, SAMPLE_SIZE)
    cmd = 'echo {} | xargs -n1 -P{} pyflakes 2> /dev/null'.format(
        ' '.join(paths),
        concurrency,
        )
    if 0:
        print '>>>',cmd
    # ignore Pyflakes issues
    start = time.time()
    subprocess.call(
        cmd, 
        shell=True, 
        stderr=open(os.devnull,'w'),
        stdout=open(os.devnull,'w'),
        )
    elapsed = time.time() - start
    p_sample(concurrency, elapsed)
    return elapsed


PATHS = subprocess.check_output(
    'find /usr/lib/*/dist-packages/django -name "*.py"',
    shell=True,
    ).split('\n')

print '{} source files, sampled {} at a time'.format(
    len(PATHS), SAMPLE_SIZE,
    )

ncpus = multiprocessing.cpu_count()
space = hp.choice(
    'concurrency', [
        1, 3, 5, 10, 20, 40, 60, # TODO: fibonacci!
    ] + [
        1, ncpus, ncpus*2, ncpus*2-1, ncpus*2+1
    ]
    )

                  
# minimize the objective over the space
p_title()
best = hyperopt.fmin(
    objective, space, algo=hyperopt.tpe.suggest, max_evals=50,
    )


print 'ANSWER: for files {} at a time, do {} jobs in parallel'.format(
    SAMPLE_SIZE, hyperopt.space_eval(space, best),
)
