# XXXX: 'sudo apt-get install python-scipy'
import sys
sys.path.insert(0, '/usr/lib/python2.7/dist-packages/') # scipy

import fnmatch, os, subprocess, time

import hyperopt
hp = hyperopt.hp

# define an objective function
def objective(pnum):
    start = time.time()
    path = PATHS[int(pnum*len(PATHS))] # XX silly
    cmd = 'pyflakes {} 2> /dev/null'.format(path)
    if 0:
        print '>>>',cmd
    try:
        subprocess.check_call(cmd, shell=True)
    except OSError as exc:
        print '? {}: {}'.format(exc, cmd)
        return 1000
    except subprocess.CalledProcessError:
        pass                    # XX pyflakes found issues
    elapsed = time.time() - start
    print pnum,path,elapsed
    return elapsed

# define a search space
# space = hp.uniform('x', -10, 10)
PATHS = subprocess.check_output(
    'find /usr/lib/python2.7/dist-packages/django -name "*.py"',
    shell=True,
    ).split('\n')

space = hp.uniform('pathnum', 0, 1.0)

                  
# minimize the objective over the space
best = hyperopt.fmin(
    objective, space, algo=hyperopt.tpe.suggest, max_evals=10,
    )

print best
# -> {'a': 1, 'c2': 0.01420615366247227}
print hyperopt.space_eval(space, best)
# -> ('case 2', 0.01420615366247227}
