from Filist import *
import re

pattern = "^(.*)\{\\\\tt ([^\}]*'[^\}]*)\}(.*\\n)"
prog = re.compile(pattern)

fl = Filist('book.tex')

for i in range(len(fl)):
    line = fl[i]
    ro = prog.match(line)
    if ro:
        before, term, after = ro.groups()

        term = '\\verb"%s"' % term
        line = before + term + after
        print line
        fl[i] = line

fl.writeback()
