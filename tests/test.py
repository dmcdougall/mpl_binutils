import sys
import imp
import hashlib
import io
from nose import with_setup
from matplotlib import rcParams, rcdefaults
from docopt import docopt

sys.dont_write_bytecode = True
mpl_graph = imp.load_source("mpl-graph", '../mpl-graph')

def setup():
    # These setting were taken from the matplotlib codebase to ensure
    # the user's rc file does not interfere with the produced output
    # of the tests.
    #
    # The settings *must* be hardcoded for running the comparison
    # tests and are not necessarily the default values as specified in
    # rcsetup.py
    rcdefaults() # Start with all defaults
    rcParams['font.family'] = 'Bitstream Vera Sans'
    rcParams['text.hinting'] = False
    rcParams['text.hinting_factor'] = 8
    rcParams['text.antialiased'] = False

@with_setup(setup, None)
def defaults_test():
    # Get the true hash
    true_hash_file = open('defaults_test.hash', 'r')
    true_hash = true_hash_file.read().strip()
    true_hash_file.close()

    # Run the utility with specified options
    args = docopt(mpl_graph.usage, argv=['-T', 'png', 'data.txt'])
    sys.stdout = output = io.BytesIO()
    mpl_graph.produce_plot(args, rcParams)
    output.seek(0)

    # Check true has against test hash
    test_hash = hashlib.md5(output.read()).hexdigest()
    assert true_hash == test_hash
