import sys
import io
import imp

sys.dont_write_bytecode = True

def failure_setup(test):
    def failure_test():
        # This is just to kill print output
        sys.stderr = io.BytesIO()
        test()
    return failure_test

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
