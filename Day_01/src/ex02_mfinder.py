import re
import sys
lines = []
for line in sys.stdin:
    lines.append(line.rstrip("\n"))
if ((len(lines) == 3)
    and (len(lines[0]) == 5)
    and (len(lines[1]) == 5)
        and (len(lines[2]) == 5)):
    if ((re.match(r'\*[^\*][^\*][^\*]\*', lines[0]))
            and (re.match(r'\*\*[^\*]\*\*', lines[1]))
            and (re.match(r'\*[^\*]\*[^\*]\*', lines[2]))):
        print("True")
    else:
        print("False")
else:
    print("Error")
