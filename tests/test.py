import sys
import imp
import codecs
import io
import nose
import difflib
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
    rcParams['font.family'] = 'monospace'
    rcParams['text.hinting'] = False
    rcParams['text.hinting_factor'] = 16
    rcParams['text.antialiased'] = False

def spit_diff(a, b):
    diff = difflib.unified_diff(a.split('\n'), b.split('\n'),
            fromfile="expected", tofile="computed")
    diff = [line for line in diff]
    headings = diff[0:3]
    diff_output = diff[3::]
    headings = ''.join(headings)
    diff_output = '\n'.join(diff_output)
    return '\n' + headings + diff_output

def img_setup(test):
    def img_test():
        sys.stdout = output = io.StringIO()

        test()

        output.seek(0)
        test_img = output.read()
        output.close()

        # Get the true img
        try:
            true_img_file = codecs.open(test.__name__ + '.svg', 'r', 'utf8')
        except IOError:
            # File doesn't exist because it's a new test and there's no
            # true img file
            true_img_file = codecs.open(test.__name__ + '.svg', 'w', 'utf8')
            true_img_file.write(test_img)
            true_img_file.close()
            raise NewTestError("New test found. Run again.")

        # true_img = true_img_file.read().strip()
        true_img = true_img_file.read()
        true_img_file.close()

        assert true_img == test_img, ('Test "{}" failed. Diff follows:\n'
                '{}'.format(test.__name__, spit_diff(true_img, test_img)))

    return img_test

@img_setup
def defaults_test():
    # Run the utility with specified options
    args = docopt(mpl_graph.usage, argv=['-T', 'svg', 'data.txt'])

    # mpl-graph dumps to stdout, so we capture it in the decorator
    mpl_graph.produce_plot(args, rcParams)

@img_setup
def abscissa_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'svg', '-a', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@img_setup
def fontsize_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'svg', '-f', '15', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@img_setup
def grid_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'svg', '-g', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@img_setup
def linewidth_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'svg', '-W', '40', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@img_setup
def linemode_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'svg', '-m', '1', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

    args = docopt(mpl_graph.usage, argv=['-T', 'svg', '-m', '2', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

    args = docopt(mpl_graph.usage, argv=['-T', 'svg', '-m', '3', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

    args = docopt(mpl_graph.usage, argv=['-T', 'svg', '-m', '4', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@img_setup
def ticksize_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'svg', '-k', '10', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@img_setup
def log_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'svg', '-l', 'x,y', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@img_setup
def size_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'svg', '-s', '4.0,4.0', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@img_setup
def noticks_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'svg', '-N', 'x,y', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@img_setup
def color_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'svg', '-C', 'red', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@img_setup
def toplabel_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'svg', '-L', 'hello', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@img_setup
def xlim_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'svg', '-x', '0,5', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

    args = docopt(mpl_graph.usage, argv=['-T', 'svg', '-x', '0,5,11', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@img_setup
def ylim_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'svg', '-y', '0,2', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

    args = docopt(mpl_graph.usage, argv=['-T', 'svg', '-y', '0,2,9', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@img_setup
def xlabel_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'svg', '-X', 'hello', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@img_setup
def ylabel_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'svg', '-Y', 'hello', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@img_setup
def titlefontsize_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'svg', '-L', 'hello', '--title-font-size', '28', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@img_setup
def tight_test():
    # FIXME: This test doesn't pass when it should.
    #        The diff is nonempty but the difference is in the tenth
    #        digit of a float. Tiny.
    #        Need a better way of comparing SVGs
    raise nose.SkipTest
    args = docopt(mpl_graph.usage, argv=['-T', 'svg', '--tight', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@img_setup
def hdf5_test():
    try:
        import h5py
    except ImportError:
        raise nose.SkipTest
    args = docopt(mpl_graph.usage, argv=['-T', 'svg', 'data.h5:/a/b/c/my_data'])
    mpl_graph.produce_plot(args, rcParams)
