import sys
import io
import imp
from nose.tools import make_decorator

sys.dont_write_bytecode = True

def failure_setup(test):
    def failure_test():
        # This is just to kill print output
        sys.stderr = io.BytesIO()
        test()
    return make_decorator(test)(failure_test)

@failure_setup
def docopt_test():
    # Simulate missing required dependency
    sys.modules['docopt'] = None

    try:
        mpl_graph = imp.load_source("mpl-graph", '../mpl-graph')
    except SystemExit as e:
        # FIXME: Hard-coding the error code is very bad.
        assert e.code == -6
    finally:
        del sys.modules['docopt']

@failure_setup
def mpl_test():
    # Simulate missing required dependency
    sys.modules['matplotlib'] = None

    try:
        mpl_graph = imp.load_source("mpl-graph", '../mpl-graph')
    except SystemExit as e:
        # FIXME: Hard-coding the error code is very bad.
        assert e.code == -6
    finally:
        del sys.modules['matplotlib']
