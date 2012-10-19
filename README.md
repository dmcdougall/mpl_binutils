mpl_binutils
============

This is `mpl_binutils`, a command-line front-end for matplotlib line-plotting.

Dependencies
============

You will need:

- [matplotlib](https://github.com/matplotlib/matplotlib): 1.1 or higher
- [docopt](https://github.com/docopt/docopt): 0.5 or higher

Installing mpl_binutils
=======================

To install, execute the following commands from the source root

    $ chmod u+x mpl-graph  # makes the script executable by you
    $ cp mpl-graph /usr/local/bin/  # put the script in a sensible place

You should copy the `mpl-graph` script to a directory that is in yout `PATH`
environment variable.

Using mpl_binutils
==================

To learn how to use `mpl-graph`, execute

    $ mpl-graph --help

for usage information. You should get output like the following

    Usage: mpl-graph [options] <file>
           mpl-graph --help
           mpl-graph --version

    Options:
        -T, --output-format=<filetype>  Specify output filetype [default: pdf]
        -s, --size-of-plot=<size>       Specify plot size in inches: width,height
        -x, --x-limits=<xlimits>        Specify x-axis limits: xmin,xmax,xnum
        -y, --y-limits=<ylimits>        Specify y-axis limits: ymin,ymax,ynum
        -X, --x-label=<xlabel>          Specify x-axis label
        -Y, --y-label=<ylabel>          Specify y-axis label

The interface is very similar to that of the `graph` utility in GNU plotutils.

The following `bash` commands show an explicit example of `mpl-graph` usage.

    $ cat << EOF > data.dat
    > 1.0 0.0
    > 2.0 1.0
    > 3.0 2.0
    EOF
    $ mpl-graph -T pdf -s 6,6 -x 1,4 -y 0,3 -X 'x label' -Y 'y label' data.dat > plot.pdf

Contributing
============

There are plenty of things to do to contribute. The main goal is to mimic most
of the functionality of the GNU plotutils `graph` utility, of which there is
ample. Support for several files (and even file types!) is yet to be
implemented. Lastly, and probably most importantly, validation on the passed
command-line options should be more strict. `mpl-graph` should be helpful to
the user and should fail gracefully. Currently it does not.
