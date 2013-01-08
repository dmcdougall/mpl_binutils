import sys
import io
import imp
from matplotlib import rcParams
from docopt import docopt

sys.dont_write_bytecode = True
mpl_graph = imp.load_source("mpl-graph", '../mpl-graph')

def failure_setup(test):
    def failure_test():
        try:
            sys.stderr = output = io.BytesIO()
            test()
            output.close()
        except SystemExit:
            assert True
    return failure_test

@failure_setup
def manyoptions_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'png', '-x', '0,1,1,1', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@failure_setup
def floatoption_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'png', '-W', 'asd', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@failure_setup
def filetype_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'asd', 'data.txt'])
    mpl_graph.produce_plot(args, rcParams)

@failure_setup
def badfile_test():
    args = docopt(mpl_graph.usage, argv=['-T', 'png', 'badfile.txt'])
    mpl_graph.produce_plot(args, rcParams)
