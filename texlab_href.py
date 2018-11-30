import re

REGEXES = [(r"\\emph\{(\[{2}(\w+)\:(.*?)(?:\|(.*?)?)?]{2})\}", r"\1"),
           (r"\[{2}(\w+)\:(.*?)(?:\|(.*?)?)?]{2}", r"\\LabRef[\3]{\1}{\2}"),
           (r"\n{2,}", r"\n"),
           (r"\n*\$(?:\\[,.;:])*\$\n*", r"\n")]
INFILE = open('to-be-tidied.tex', 'r')
outfile = open('tidied.tex', 'w')

for line in INFILE:
    for rex, sub in REGEXES:
        newl = re.sub(rex, sub, line)
    print(newl)
    outfile.write(newl)
