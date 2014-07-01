# XXXX: 'sudo apt-get install python-scipy'
import sys
sys.path.insert(0, '/usr/lib/python2.7/dist-packages/') # scipy

import fnmatch, os, subprocess, time

import hyperopt
hp = hyperopt.hp
scope = hyperopt.pyll.scope

# @scope.define
# def mychoice(label, options):
#     if not isinstance(label, basestring):
#         raise TypeError('require string label')
#     ch = scope.hyperopt_param(label,
#         scope.randint(len(options)))
#     return scope.switch(ch, *options)


# define an objective function
def objective(path):
    start = time.time()
    cmd = 'pyflakes {} 2> /dev/null'.format(path)
    if 0:
        print '>>>',cmd
    os.system(cmd)  # ignore Pyflakes issues
    # try:
    # # except OSError as exc:
    # #     print '? {}: {}'.format(exc, cmd)
    # #     return 1000
    # except subprocess.CalledProcessError:
    #     pass                    # ignore issues
    elapsed = time.time() - start
    if 0:
        print path,elapsed
    return elapsed

# define a search space
PATHS = subprocess.check_output(
    'find /usr/lib/python2.7/dist-packages/django -name "*.py"',
    shell=True,
    ).split('\n')

space = hp.choice(
    'path', PATHS
    )

                  
# minimize the objective over the space
best = hyperopt.fmin(
    objective, space, algo=hyperopt.tpe.suggest, max_evals=10,
    )

print best
# -> {'a': 1, 'c2': 0.01420615366247227}
print hyperopt.space_eval(space, best)
# -> ('case 2', 0.01420615366247227}
