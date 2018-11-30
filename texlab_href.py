import re

REGEX = r"\[{2}(\w+)\:(.*?)(?:\|(.*?)?)?]{2}"
SUB = r"\\LabRef[\3]{\1}{\2}"
INFILE = open('to-be-tidied.tex', 'r')
outfile = open('tidied.tex', 'w')

for line in INFILE:
    newl = re.sub(REGEX, SUB, line)
    outfile.write(newl)