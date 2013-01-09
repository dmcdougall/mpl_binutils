import sys
import io
import imp
from matplotlib import rcParams
from docopt import docopt

sys.dont_write_bytecode = True
mpl_graph = imp.load_source("mpl-graph", '../mpl-graph')

def failure_setup(test):
    def failure_test():
        # This is just to kill print output
        sys.stderr = io.BytesIO()
        test()
    return failure_test

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
