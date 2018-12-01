import re
import subprocess
COMMAND = "awk '/^$/ { if (blank++) next; print }1' to-be-tidied.tex > 'clean.tex'"
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
    # remove the horrible \,.
    (r"\\[,;]", r""),
    # remove manually included spacing
    (r"^ {2,}", r""),
    # remove unwanted spaces at beginline
    (r"\\math(bb|sf|bf|cal)\{([A-Z])\}", r"\\\1\2"),
    # \math<roba>{<[A-Z]>} -> \<roba>[A-Z]
    (r"&\#643;", r"\\esh "),
    # ʃ -> \esh
    ]
INFILE = open('clean.tex', 'r')
outfile = open('tidied.tex', 'w')

for line in INFILE:
    for rex, sub in REGEXES:
        line = re.sub(rex, sub, line, flags=re.M)
    outfile.write(line)
