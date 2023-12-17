import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("n", type=int, help="the number of lines to read")
args = parser.parse_args()
lines = []
for i in range(args.n):
    try:
        l = sys.stdin.readline().rstrip("\n")
        if (len(l) == 32) & (l[:5] == "00000") & (l[5] != "0"):
            lines.append(l)
    except EOFError:
        break
    except IndexError:
        pass
print(*lines, sep="\n")
