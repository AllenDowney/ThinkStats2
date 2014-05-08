from Filist import *
import re

pattern = '^(.*)\{\\\\tt ([^\}]*\\\\_[^\}]*)\}(.*\\n)'
print pattern
prog = re.compile(pattern)

fl = Filist('book.tex')

for i in range(len(fl)):
    line = fl[i]
    if line.find('\\_') != -1:
        if line.startswith('\\section'): continue
        ro = prog.match(line)
        if ro:
            before, name, after = ro.groups()

            name = name.replace('\\_' ,'_')
            name = '\\verb"%s"' % name
            line = before + name + after
            print line
            fl[i] = line

fl.writeback()
