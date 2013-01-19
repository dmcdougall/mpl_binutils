import sys
import imp
import hashlib
import io
from nose import with_setup
from nose.tools import make_decorator
from matplotlib import rcParams, rcdefaults
from docopt import docopt

sys.dont_write_bytecode = True
mpl_graph = imp.load_source("mpl-graph", '../mpl-graph')

class NewTestError(Exception):
    pass

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

def hash_setup(test):
    def hash_test():
        sys.stdout = output = io.BytesIO()

        test_hash = test()

        output.seek(0)
        test_hash = hashlib.md5(output.read()).hexdigest()
        output.close()

        # Get the true hash
        try:
            true_hash_file = open(test.__name__ + '.hash', 'r')
        except IOError:
            # File doesn't exist because it's a new test and there's no
            # true hash file
            true_hash_file = open(test.__name__ + '.hash', 'w')
            true_hash_file.write(test_hash + '\n')
            true_hash_file.close()
            true_hash_file = open(test.__name__ + '.hash', 'r')
            raise NewTestError("New test found. Run again.")

        true_hash = true_hash_file.read().strip()
        true_hash_file.close()

        assert true_hash == test_hash, 'Test "{}" failed with hash {}'.format(
                test.__name__, test_hash)

    return make_decorator(test)(hash_test)

@hash_setup
def defaults_test():
    # Run the utility with specified options
    args = docopt(mpl_graph.usage, argv=['-T', 'png', 'data.txt'])

    # mpl-graph dumps to stdout, so we capture it in the decorator
    mpl_graph.produce_plot(args, rcParams)

@hash_setup
def abscissa_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'png', '-a', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@hash_setup
def fontsize_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'png', '-f', '15', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@hash_setup
def grid_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'png', '-g', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@hash_setup
def linewidth_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'png', '-W', '40', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@hash_setup
def linemode_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'png', '-m', '1', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

    args = docopt(mpl_graph.usage, argv=['-T', 'png', '-m', '2', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

    args = docopt(mpl_graph.usage, argv=['-T', 'png', '-m', '3', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

    args = docopt(mpl_graph.usage, argv=['-T', 'png', '-m', '4', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@hash_setup
def ticksize_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'png', '-k', '10', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@hash_setup
def log_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'png', '-l', 'x,y', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@hash_setup
def size_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'png', '-s', '4.0,4.0', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@hash_setup
def noticks_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'png', '-N', 'x,y', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@hash_setup
def color_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'png', '-C', 'red', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@hash_setup
def toplabel_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'png', '-L', 'hello', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@hash_setup
def xlim_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'png', '-x', '0,5', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

    args = docopt(mpl_graph.usage, argv=['-T', 'png', '-x', '0,5,11', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@hash_setup
def ylim_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'png', '-y', '0,2', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

    args = docopt(mpl_graph.usage, argv=['-T', 'png', '-y', '0,2,9', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@hash_setup
def xlabel_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'png', '-X', 'hello', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@hash_setup
def ylabel_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'png', '-Y', 'hello', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@hash_setup
def titlefontsize_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'png', '-L', 'hello', '--title-font-size', '28', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@hash_setup
def tight_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'png', '--tight', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@hash_setup
def hdf5_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'png', 'data.h5:/a/b/c/my_data'])
    mpl_graph.produce_plot(args, rcParams)
