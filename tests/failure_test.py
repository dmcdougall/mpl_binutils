import sys
import io
import imp
from nose.tools import make_decorator
from matplotlib import rcParams
from docopt import docopt

sys.dont_write_bytecode = True
mpl_graph = imp.load_source("mpl-graph", '../mpl-graph')

def failure_setup(test):
    def failure_test():
        # This is just to kill print output
        sys.stderr = io.BytesIO()
        test()
    return make_decorator(test)(failure_test)

@failure_setup
def manyoptions_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'png', '-x', '0,1,1,1', 'data.txt'])
    try:
        mpl_graph.produce_plot(args, rcParams)
    except SystemExit as e:
        assert e.code == mpl_graph.ERR_NUM_OPTIONS

@failure_setup
def floatoption_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'png', '-W', 'asd', 'data.txt'])
    try:
        mpl_graph.produce_plot(args, rcParams)
    except SystemExit as e:
        assert e.code == mpl_graph.ERR_ARG_TYPE

@failure_setup
def filetype_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'asd', 'data.txt'])
    try:
        mpl_graph.produce_plot(args, rcParams)
    except SystemExit as e:
        assert e.code == mpl_graph.ERR_OUTPUT_TYPE

@failure_setup
def badfile_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'png', 'badfile.txt'])
    try:
        mpl_graph.produce_plot(args, rcParams)
    except SystemExit as e:
        assert e.code == mpl_graph.ERR_INPUT_FILE

@failure_setup
def h5py_test():
    # Simulate missing optional dependency
    sys.modules['h5py'] = None

    args = docopt(mpl_graph.usage, argv=['-T', 'png', 'data.h5:/a/b/c/my_data'])
    try:
        mpl_graph.produce_plot(args, rcParams)
    except SystemExit as e:
        assert e.code == mpl_graph.ERR_OPTIONAL_DEP
    finally:
        del sys.modules['h5py']
