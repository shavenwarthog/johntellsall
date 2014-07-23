import logging, multiprocessing
from multiprocessing import Pool

def split_list(L, n):
    return [L[i::n] for i in xrange(n)]

def coreFunc(mylist):
    proclog = multiprocessing.get_logger()

    proclog.info("listlen = %d", len(mylist))
    for path in mylist:
        proclog.info("input1 = %s", path)

    return 1


if __name__=="__main__":

    if 0:
        array = [line.rstrip() for line in open("myfilelist")]
    else:
        import string
        array = string.uppercase

    mylog = multiprocessing.log_to_stderr()
    mylog.setLevel(logging.INFO)

    numC = multiprocessing.cpu_count()
    lists = split_list(array, numC)

    p = Pool(numC)
    print p.map(coreFunc, lists)
    p.close()
    p.join()
