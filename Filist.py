"""

A class for reading the contents of a file, modifying it in
memory, and writing it back.

A Filist is a list of strings that contains the contents of
a file.  All the usual list operations can be applied to a Filist.

Because this class loads the entire file into memory, it uses
more space than it might need to, and it is limited to working with
files that fit into memory.  The advantage is that it is easy to
implement algorithms that need random access to the contents of the
file, and it is convenient to debug because all the data is
available all the time.

Some of the methods I included are here because of specific
operations I was interested in.

Copyright 2005 Allen B. Downey

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, see http://www.gnu.org/licenses/gpl.html
    or write to the Free Software Foundation, Inc., 51 Franklin St, 
    Fifth Floor, Boston, MA  02110-1301  USA

"""

import sys
import re

class Filist(list):
    def __init__(self, filename=None, t=None):
        """ if a filename is provided, read the contents """
        if filename:
            self.filename = filename
            lines = open(filename).readlines()
            self.extend(lines)
        # add any lines that are provided
        if t:
            self.extend(t)

    def __str__(self):
        return ''.join(self)

    def join(self):
        """collapse the list of strings into a single long string"""
        self[:] = [str(self)]

    def search_lines(self, pattern):
        """traverse lines in order until one of them matches,
        return the index and the match object
        """
        pat = re.compile(pattern)
        for i in range(0, len(self)):
            match = pat.search(self[i])
            if match:
                return i, match

    def decapitate(self, pattern='<BODY >\n'):
        """find the first line that matches the pattern;
        remove it and all the previous lines
        """
        i = self.index(pattern)
        del self[:i+1]

    def depeditate(self, pattern='</BODY>\n'):
        """find the first line that matches the pattern;
        remove it and all the following lines
        """
        i = self.index(pattern)
        del self[i:]

    def prefile(self, filename):
        """prepend the contents of the given file"""
        ft = Filist(filename)
        self.insert(0, ft)

    def suffile(self, filename):
        """append the contents of the given file"""
        ft = Filist(filename)
        self.extend(ft)

    def writeto(self, filename):
        """write the contents of the Filist to a file"""
        fp = open(filename, 'w')
        for line in self:
            fp.write(line)

    def writeback(self):
        """write the contents of the Filist back to the file it came from"""
        self.writeto(self.filename)

def change_suffix(filename, suffix):
    """return a new filename that is the same as the given name
    with the file extension replaced with the given suffix
    """
    filename.split('.')
    t[-1] = suffix
    return '.'.join(t)

def cp(source, dest):
    """copy a file from source to destination, returning a Filist"""
    ft = Filist(source)
    ft.writeto(dest)
    return ft

def main(name, filename, *argv):
    # print the contents of the given file
    ft = Filist(filename)
    print ft

if __name__ == '__main__':
    main(*sys.argv)
