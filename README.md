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

# Bugs

The puppet4ify_erb.py script converts variables into instance variables also 
where is shouldn't. This affects iteration first and foremost:

    <% @locales.each do |locale| -%>
    <%= @locale %>
    <% end -%>

This will not work, because @locale is set to undef here. the correct syntax is

    <% @locales.each do |locale| -%>
    <%= locale %>
    <% end -%>

Trying to catch these in a generic way would be difficult, so please check the 
diffs (-d --noop) carefully and make the fixes that are necessary afterwards.
