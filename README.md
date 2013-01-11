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

You should copy the `mpl-graph` script to a directory that is in your `PATH`
environment variable.

For completeness, `mpl-graph` comes with a man page too. You can install it
in much the same way as the executable described above, into a directory in
your `MANPATH` variable. From the repository root, execute

    $ cp docs/mpl-graph.3 /usr/local/share/man/man3/
    $ gzip /usr/local/share/man/man3/mpl-graph.3

Use of `/usr/local/share` is just an example. Anywhere that is in your
`MANPATH` will do. To view the man page, execute

    $ man mpl-graph

Using mpl_binutils
==================

To learn how to use `mpl-graph`, execute

    $ mpl-graph --help

for usage information. You should get output like the following

    Usage: mpl-graph [options] <file>
           mpl-graph --help
           mpl-graph --version

    Options:
        -a, --auto-abscissa             Automatically generate the abscissa
        -q, --fill-fraction=<alpha>     Specifies the alpha of a filled polygon
        -T, --output-format=<filetype>  Specify output filetype [default: pdf]
        -f, --font-size=<fontsize>      Set font size for ticks and labels
        -g, --grid                      Turn on grid
        -W, --line-width=<linewidth>    Set line-width of plotted lines
        -m, --line-mode=<linemode>      Value from 1-4 specifying line style [default: 1]
        -k, --tick-size=<ticksize>      Set tick length
        -l, --toggle-log-axis=<axes>    Toggle log axis for the given comma-separated list of axes
        -s, --size-of-plot=<size>       Specify plot size in inches: width,height
        -N, --toggle-no-ticks=<axes>    Turn off ticks for the given comma-separated list of axes
        -C, --color=<color>             Set line color
        -L, --top-label=<title>         Set plot title
        -x, --x-limits=<xlimits>        Specify x-axis limits: xmin,xmax,xnum
        -y, --y-limits=<ylimits>        Specify y-axis limits: ymin,ymax,ynum
        -X, --x-label=<xlabel>          Specify x-axis label
        -Y, --y-label=<ylabel>          Specify y-axis label
        --title-font-size=<titlesize>   Set font size of the axes title
        --tight                         Make the figure use most available whitespace

The interface is very similar to that of the `graph` utility in GNU plotutils.

Plotting ASCII text files
-------------------------

The following `bash` commands show an explicit example of `mpl-graph` usage.

    $ cat << EOF > data.dat
    > 1.0 0.0
    > 2.0 1.0
    > 3.0 2.0
    EOF
    $ mpl-graph -T pdf -s 6,6 -x 1,4 -y 0,3 -X 'x label' -Y 'y label' data.dat > plot.pdf

Plotting HDF5 datasets
----------------------

The example above shows how to plot a text file. HDF5 files are also supported
but boast a slightly different syntax. 

    $ mpl-graph -T pdf filename:/path/to/dataset > plot.pdf

A single colon followed by a forward slash delimits the the name of the file
and the path to the dataset inside the HDF5 file. For example, to plot the
`/group1/group2/my_dataset` dataset in the file called `my_data.h5`, one would
execute:

    $ mpl-graph -T pdf my_data.h5:/group1/group2/dataset > plot.pdf

To plot without the `--auto-abscissa` option, the dataset must be two
dimensional, with the first dimension being an array of abscissa, and the
second dimension being the array of line data to be plotted. If, instead, the
`--auto-abscissa` option is provided, the dataset must be one-dimensional (an
array) containing only the line data to be plotted.

Contributing
============

There are plenty of things to do to contribute. The main goal is to mimic most
of the functionality of the GNU plotutils `graph` utility, of which there is
ample. Support for several files (and even file types!) is yet to be
implemented. Lastly, and probably most importantly, validation on the passed
command-line options should be more strict. `mpl-graph` should be helpful to
the user and should fail gracefully. Currently it does not.

The branching model used for `mpl_binutils` can be found
[here](http://nvie.com/posts/a-successful-git-branching-model/).
