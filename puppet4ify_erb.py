#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# A script to convert ERB templates to a format Puppet 4 accepts. Currently this
# only converts non-instance variables to instance variables by adding a "@" to
# the beginning of the variable name as necessary.
#
# In debug mode (see -h) changes to be made are printed in a unified diff-like
# format.
#
from shutil import move
import argparse
import re
import sys

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Convert ERB templates into Puppet 4 format')
    parser.add_argument('infile', nargs=1, type=file, help='file to read from')
    parser.add_argument('-o', '--outfile', nargs=1, help='file to write to')
    parser.add_argument('-d', '--debug', action='store_true', help='use debug mode')
    parser.add_argument('--noop', action='store_true', help='use no-operation mode')

    try:
        args = parser.parse_args()
    except IOError:
        print 'ERROR: Input file could not be opened!'
        sys.exit(1)

    # Only overwrite the input file if -o is not defined
    overwrite = False
    try:
        if not args.noop:
            outfile = open(args.outfile[0], 'w')
    except IOError:
        print 'ERROR: unable to write to output file!'
        sys.exit(1)
    except TypeError:
        # Outfile was probably not defined, so we write to a temporary name and
        # overwrite the input file at the end.
        overwrite = True
        if not args.noop:
            outfile = open(args.infile[0].name+'.tmp', 'w')

    # Match non-instance variables (<%= variable %>) in the ERB template and
    # convert them to instance variables (<%= @variable %>.
    #
    # The regular expression captures the entire variable definition and the
    # variable name inside it, naming the latter as "varname". Then a "@" is
    # added in front of the variable name if not yet present.
    p=re.compile(r'(?P<prepad><%=\s*)(?P<varname>[\d\w]+)(?P<postpad>\s*-?%>)')

    # The args.infile contains an array, even if we only allow one input file
    for file in args.infile:
        for line in file:
            replaced = p.sub('\g<prepad>@\g<varname>\g<postpad>', line)
            if not line == replaced and args.debug:
                print '-'+line.rstrip()
                print '+'+replaced.rstrip()
            if not args.noop:
                outfile.write(replaced)
        file.close()

    # Copy the temporary file over the input file, if no output file is defined
    if not args.noop:
        outfile.close()
        if overwrite:
            move(outfile.name, args.infile[0].name)
