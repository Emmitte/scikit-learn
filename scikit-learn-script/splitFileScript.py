__author__ = 'wangyida_'
"""
split file into trainset and testset
train(train_x,train_y),test(test_x,test_y),split:"\t"
"""

def printListToFile(output,data,start,end):
    for i in range(start,end):
        if i == (end-1):
            output.write(data[i])
        else:
            output.write(data[i])
            output.write('\t')
    output.write('\n')

path = "dataset"
train_dir = "train/"
test_dir = "test/"
train_X_path = train_dir + "train_x"
train_Y_path = train_dir + "train_y"
test_X_path = test_dir + "test_x"
test_Y_path = test_dir + "test_y"
ratio = 0.6
fr = open(path)
lines = fr.readlines()
fr.close()

train_X = open(train_X_path,'w')
train_Y = open(train_Y_path,'w')
test_X = open(test_X_path,'w')
test_Y = open(test_Y_path,'w')

size = len(lines)
train_size = size * ratio
test_size = size * (1 - ratio)
i = 0
for line in lines:
    data = []
    line = line.strip('\n')
    data = line.split('\t')
    if i < train_size:
        printListToFile(train_X,data,0,len(data)-1)
        printListToFile(train_Y,data,len(data)-1,len(data))
    else:
        printListToFile(test_X,data,0,len(data)-1)
        printListToFile(test_Y,data,len(data)-1,len(data))
    i += 1
train_X.close()
train_Y.close()
test_X.close()
test_Y.close()