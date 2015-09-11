# puppet4ify

Scripts to convert (ERB) files into a format that Puppet 4 accepts.

# Usage

## puppet4ify_erb.py

Show help:

    $ ./puppet4ify_erb.py -h

Show changes that would be made, using a test file:

    $ ./puppet4ify_erb.py -d --noop test.erb

Create a new file with the corrected content:

    $ ./puppet4ify_erb.py -o outfile.erb infile.erb

Change content of real file in-place:

    $ ./puppet4ify_erb.py infile.erb

# TODO

* Handle array variables / iterators
