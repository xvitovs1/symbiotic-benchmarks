#!/usr/bin/env python

import sys
import os
import getopt
import signal
import subprocess

debug = False
timeout = 0
slce = True
prp = None
pta = None
optimize = None
arch = None
noopt = False

running_processes = []

class bcolors:
    ERROR = '\033[1;31m'
    OK = '\033[1;32m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'

class Timeout(Exception):
    pass

def start_timeout(sec):
    def alarm_handler(signum, data):
        raise Timeout

    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(sec)

def stop_timeout():
    # turn off timeout
    signal.signal(signal.SIGALRM, signal.SIG_DFL)
    signal.alarm(0)

def run_symbiotic(benchmark, outputfile):
	# must be run from symbiotic/install/bin folder for now
    cmd = ['./symbiotic']
    cmd.append('--no-integrity-check')
    if debug:
        cmd.append('--debug=all')

    if noopt:
        cmd.append('--no-optimize')

    if not prp is None:
       cmd.append('--prp={0}'.format(prp))

    if not slce:
        cmd.append('--no-slice')

    if arch == '64bit':
        cmd.append('--64')

    if timeout != 0:
        cmd.append('--timeout={0}'.format(timeout))

    optimize='before-O3,after-O3'
    if optimize:
        cmd.append('--optimize={0}'.format(optimize))

    # we run on sv-comp benchmarks where we assume that
    # malloc never fails
    cmd.append('--malloc-never-fails')

	# we do not need witness for now
    cmd.append('--no-witness')

    if not pta is None:
        cmd.append('--pta')
        cmd.append(pta)

    cmd.append(benchmark)

    outfl = open(outputfile, 'w')

    p = subprocess.Popen(cmd, stdout=outfl, stderr=subprocess.STDOUT)
    global running_processes
    running_processes.append(p)

    return p

def parse_args():
    try:
        opts, args = getopt.getopt(sys.argv[1:], '', ['timeout=', 'debug', 'no-slice',
                                                      '64', 'prp=', 'pta=', 'optimize=', 
                                                      'no-optimize'])
    except getopt.GetoptError as e:
        print('{0}'.format(str(e)))
        sys.exit(1)

    global prp
    for opt, arg in opts:
        if opt == '--debug':
            global debug
            debug = True
        elif opt == '--timeout':
            global timeout
            timeout = int(arg)
        elif opt == '--no-slice':
            global slce
            slce = False
        elif opt == '--no-optimize':
            global noopt
            noopt = True
        elif opt == '--64':
            global arch
            arch = '64bit'
        elif opt == '--prp':
            prp = arg
        elif opt == '--pta':
            global pta
            pta = arg
        elif opt == '--optimize':
            global optimize
            optimize = arg

    return args

def say_result(res, filename):
    fn = filename.replace('.c', '')
    result = res.replace('RESULT: ', '')
    if (fn.endswith('false') and result.startswith('true')) or (fn.endswith('true') and result.startswith('false')) or result.startswith('ERROR'):
        print(bcolors.ERROR + res + bcolors.ENDC)
    elif (result.startswith('unknown') or result.startswith('timeout')):
        print(bcolors.WARNING + res + bcolors.ENDC)
    else:
        print(bcolors.OK + res + bcolors.ENDC)
    
    return res

def sigpipe_handler(signum, data):
    global running_processes
    for p in running_processes:
        p.kill(2) # SIGINT
        p.terminate()
        p.kill()

if __name__ == "__main__":
    signal.signal(signal.SIGPIPE, sigpipe_handler)
    signal.signal(signal.SIGINT, sigpipe_handler)

    print('Starting')

    # kill the processes for sure after some time
    # (klee sometimes ignores signals)
    if timeout:
        subprocess.call(['ulimit', '-t', 3 * timeout])

    pths = parse_args()

    #os.chdir('/tmp')

    if len(pths) == 1:
        benchmarks_dir = pths[0]
    else:
        print('=== RESULT')
        print('ERROR')
        print('Usage: run_symbiotic [--timeout=n] [--debug] [--no-slice]'
              '[--prp=property] [--64] folder')
        sys.exit(1)

    for filename in os.listdir(benchmarks_dir):
        if not filename.lower().endswith(('.c')):
            continue

        src = os.path.join(benchmarks_dir, filename)
        print(src)
    
        sys.stdout.flush()
    
        outputfile = '{0}.output'.format(src)
        p = run_symbiotic(src, outputfile)
    
        p.communicate()
        running_processes.remove(p)
        result = None
    
        if p.returncode != 0:
            print('Symbiotic returned with {0}'.format(p.returncode))
            print(bcolors.ERROR + 'ERROR' + bcolors.ENDC)
        else:
            outf = open(outputfile, 'r')
            for line in iter(outf.readlines()):
                if line.startswith('RESULT'):
                    result = say_result(line, filename)

    sys.stdout.flush()

    print('Total end')
