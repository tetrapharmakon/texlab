import re

REGEXES = [(r"\\emph{(\[{2}(\w+)\:(.*?)(?:\|(.*?)?)?]{2})}", r"\1"),
           # \emph{[[foo:bar|baz]]} -> [[foo:bar|baz]]
           (r"\[{2}(\w+)\:(.*?)(?:\|(.*?)?)?]{2}", r"\\LabRef[\3]{\1}{\2}"),
           # [[foo:bar|baz]] -> \LabRef[baz]{foo}{bar}
           (r"\n{3,}", r"\n\n"),
           # remove iterated newlines
           (r"\n*\$(?:\\[,.;:])*\$\n*", r"\n")]
        #    remove $\,\,\,\,\,\,$
INFILE = open('to-be-tidied.tex', 'r')
outfile = open('tidied.tex', 'w')

for line in INFILE:
    for rex, sub in REGEXES:
        line = re.sub(rex, sub, line)
    outfile.write(line)
