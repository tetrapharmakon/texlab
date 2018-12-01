import re
import subprocess
COMMAND = "awk '/^$/ { if (blank++) next; print }1' to-be-tidied.tex >> 'clean.tex'"
subprocess.call(COMMAND, shell=True)

REGEXES = [
    (r"\\emph{(\[{2}(\w+)\:(.*?)(?:\|(.*?)?)?]{2})}", r"\1"),
    # \emph{[[foo:bar|baz]]} -> [[foo:bar|baz]]
    (r"\[{2}(\w+)\:(.*?)(?:\|(.*?)?)?]{2}", r"\\LabRef[\3]{\1}{\2}"),
    # [[foo:bar|baz]] -> \LabRef[baz]{foo}{bar}
    (r"\n*\$(?:\\[,.;:])*\$\n*", r"\n"),
    # remove $\,\,\,\,\,\,$
    (r"\[\]", r""),
    # remove []
    (r" *\\,\. *\n", r""),
    (r"\\[,;]", r""),
    (r"^ {2,}", r"")
    # remove unwanted newlines before end env
    # (r"\n{2,}\\begin", r"\n\\begin"),
    # # remove unwanted newlines before begin env
    # (r"(\\begin\{.*?\})\n{2,}", r"\1\n")
    # # remove unwanted newlines after begin env
    ]
    # (r"", r""),
    # (r"", r""),
    # (r"", r""),
    # (r"", r""),
    # (r"", r""),
    # (r"", r"")
INFILE = open('clean.tex', 'r')
outfile = open('tidied.tex', 'w')

for line in INFILE:
    for rex, sub in REGEXES:
        line = re.sub(rex, sub, line, flags=re.M)
    outfile.write(line)
