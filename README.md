mpl_binutils
============

This is `mpl_binutils`, a command-line front-end for matplotlib line-plotting.

Installing mpl_binutils
=======================

To install, just execute the following command from the source root:

    $ chmod u+x mpl-graph  # makes the script executable by you
    $ cp mpl-graph /usr/local/bin/  # put the script in a sensible place

You should copy the script to a directory that is in yout `PATH` environment
variable.

Using mpl_binutils
==================

To learn how to use `mpl-graph`, execute

    $ mpl-graph --help

for usage information. The interface is very similar to that of the `graph`
utility in GNU plotutils.

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
