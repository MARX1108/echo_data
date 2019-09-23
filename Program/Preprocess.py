# this is for preprocess data
import numpy as np

f = open("../echo4/static-147-20190904_072253895067.txt", "r")
a = f.readline()

with f as tsv:
    line = [elem.strip().split('\t') for elem in tsv]
dict = {}

vals = np.asarray(line)
mic0 = vals[::2]
mic1 = vals[1::2]
dict[0] = f.name;


print(dict)

