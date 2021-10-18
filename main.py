import argparse
import csv
import json

parser = argparse.ArgumentParser()
parser.add_argument("-t", help="type convert JSON or CSV", default="")
parser.add_argument("-f", help="File log", default="")
parser.add_argument("-p", help="pindah path", default="")
args = parser.parse_args()

file = args.f
path = args.p

if args.t == 'JSON':
    result = []
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            r = line.split('\t\t')
            result.append(
                {'timestamp': r[0]})
    print(result)
    if args.p == '':
        with open('error.json', 'w') as fp:
            json.dump(result, fp)
    else:
        with open('{}/error.json', 'w') as fp:
            json.dump(result, fp)

elif args.t == 'CSV':
    with open(file) as file:
        lines = file.read().splitlines()
        lines = [lines[x:x + 3] for x in range(0, len(lines), 3)]

        with open('error.csv', 'w+') as csvfile:
            w = csv.writer(csvfile)
            w.writerows(lines)
else:
    with open(file) as f:
        lines = f.readlines()
    print (lines)
