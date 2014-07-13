#!/usr/bin/env python

'''
INSTALL:
- for "hyperopt" library:
	sudo apt-get install python-scipy
- for sample data:
	sudo apt-get install pyflakes python-django
'''
# TODO: allow ^C interrupt in objective()

# TODO: clean up
import sys
sys.path.insert(0, '/usr/lib/python2.7/dist-packages/') # scipy

import argparse, functools, itertools, json, logging
import os, random, subprocess, time

import hyperopt
hp = hyperopt.hp


def get_sample(batch_size):
    """
    return large dataset and batch size to optimize
    """
    sample = dict(
        batch_size=batch_size,
        data=subprocess.check_output(
            'find /usr/lib/*/dist-packages/django -name "*.py"',
            shell=True,
        ).split('\n'),
    )
    if not sample['data']:
        # sudo apt-get install python-django
        sys.exit('Install Django to provide sample data')
    return sample


def p_title():
    print 'CONC ELAPSED\tTIME PER PROC'


def p_sample(conc, elapsed):
    print '{:4}\t{:4.2}\t{:.2}'.format(
        conc, elapsed, elapsed/conc,
        )


def write_header(info, outf):
    print >>outf, '# {}'.format( json.dumps(info) )
    print >>outf, '# CONC\tELAPSED'


# TODO: use csv module?
def write_sample(conc, elapsed, outf):
    print >> outf, '{}\t{}'.format(
        conc, elapsed
        )


def write_footer(best_val, best, outf):
    print >>outf, '# best: {} ({})'.format(
        best_val,
        best,
        )

def fibonacci():
    # skip 0, 1
    a,b = 0,1
    while True:
        a, b = b, a + b
        yield b


# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


def get_numprocs_fibonacci(batchsize):
    """
    Use Fibonacci sequence to speed feedback loop, skipping nprocs that
    won't give us distinct, valuable information.
    """
    num_procs = list( itertools.takewhile(
        lambda num: num <= batchsize,
        fibonacci()
    ) )
    if batchsize not in num_procs:
        num_procs.append(batchsize)
    return num_procs


def get_numprocs_traditional():
    """
    use simple, popular heuristic based on # cpus
    """
    import multiprocessing
    ncpus = multiprocessing.cpu_count()
    return [
        1, ncpus, ncpus*2, ncpus*2-1, ncpus*2+1
    ]


# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


def format_command(cmd_type, paths, concurrency):
    if cmd_type == 'pyflakes':
        return 'echo {} | xargs -n1 -P{} pyflakes 2> /dev/null'.format(
            ' '.join(paths),
            concurrency,
        )
    elif cmd_type == 'pylint':
        return 'echo {} | xargs -n1 -P{} pyflakes 2> /dev/null'.format(
            ' '.join(paths),
            concurrency,
        )
    raise KeyError(cmd_type)


def objective(concurrency, sample, cmd_type, outf):
    '''
    run several jobs in parallel, return elapsed clock time
    '''
    paths = random.sample(
        sample['data'], sample['batch_size'],
    )
    start = time.time()
    # ignore Pyflakes warnings
    _status = subprocess.call(
        format_command(cmd_type, paths, concurrency),
        shell=True, 
        stderr=open(os.devnull,'w'),
        stdout=open(os.devnull,'w'),
    )
    elapsed = time.time() - start
    p_sample(concurrency, elapsed)
    write_sample(concurrency, elapsed, outf)
    return elapsed


def parse_opts():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--batch_size', type=int, default=5,
        help='') # TODO
    parser.add_argument(
        '--cmd_type', type=str, default='pyflakes',
        help='') # TODO
    parser.add_argument(
        '--max_evals', type=int, default=15,
        help='') # TODO
    parser.add_argument('--verbose', '-v', action='count')
    # parser.add_argument(
    #     '--output', type=file, default=
    #     help='') # TODO
    return parser.parse_args()


def main():
    opts = parse_opts()
    print opts.__dict__

    if opts.verbose:
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    # TODO: make more flexible
    outf = open('optimize.dat', 'w')

    sample = get_sample(batch_size=opts.batch_size)
    num_procs = get_numprocs_fibonacci(sample['batch_size'])

    print '{} source files, sampled {} at a time'.format(
        len(sample['data']), sample['batch_size'],
    )
    print 'processes:', num_procs
    p_title()
    write_header(
        info=dict(max_evals=opts.max_evals,
                  batch_size=sample['batch_size'],
                  num_procs=num_procs),
        outf=outf,
        )

    # minimize the time taken to process batch of files
    space = hp.choice(
        'concurrency', num_procs
        )
    best = hyperopt.fmin(
        functools.partial(
            objective, sample=sample, outf=outf,
            cmd_type=opts.cmd_type,
        ),
        space,
        algo=hyperopt.tpe.suggest, 
        max_evals=opts.max_evals,
        )

    best_val = hyperopt.space_eval(space, best)
    print 'ANSWER: for files {} at a time, do {} jobs in parallel'.format(
        sample['batch_size'],
        best_val,
    )
    write_footer(best_val, best, outf)
    outf.close()


if __name__=='__main__':
    main()
