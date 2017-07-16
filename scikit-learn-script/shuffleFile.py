__author__ = 'wangyida_'

import random

inputPath = "iris.txt"
outputPath = "dataset"
fr = open(inputPath)
lines = fr.readlines()
size = len(lines)
fr.close()

random.shuffle(lines)

fr = open(outputPath,'w')

for line in lines:
    fr.write(line)

fr.close()
