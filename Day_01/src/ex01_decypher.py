import argparse
parser = argparse.ArgumentParser()
parser.add_argument("sentence", help="input sentence")
args = parser.parse_args()
for i in args.sentence.split(" "):
    if len(i[0]) != 0:
        print(i[0], end='')
