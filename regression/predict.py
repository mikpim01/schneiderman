#!/usr/bin/env python
import numpy as np

#open models
model_file = open('models','r')
positions = {1:'PG', 2:'SG', 3:'SF', 4:'PF', 5:'C'}
models = {}
i = 1
for line in model_file:
    print i
    line = line.strip()
    line = line.split(',')
    a = np.zeros(len(line) - 1)
    for ii in range(len(line) - 1):
        a[ii] = float(line[ii])
    models[positions[i]] = a
    i += 1

#read in today's games csv into lines
a = open('../data/cleaned/todays_games.csv', 'r')
#format is
#position, name, salary, x1,x2,..
name_indices = {} #key index, value names
lines = []
for line in a:
    line = line.split(',')
    for i in range(len(line)):
        line[i] = line[i].strip()
        if(i>1):
            line[i] = float(line[i])
    lines.append(line)
                      
#conver lines to numpy array
num_data = len(lines)
num_features = len(lines[0]) - 3
                               
X = np.zeros((num_data,num_features))
                        
for i in range(num_data):
    for ii in range(num_features):
        X[i][ii] = lines[i][ii + 3]

#maybe we have to normalize?
"""
means = {}
stds = {}
for i in range(0, num_features):
    means[i] = np.mean(X[:][i])
    stds[i] = np.std(X[:][i])
    X[:][i] -= mean[i]
    X[:][i] /= std[i]
"""


"""
diffs = {} #key playername, value [diff1, diff2, ...]
variances = {} #key playersname, value variance
#for each game

#predict a score with our model
for p in diffs.keys:
    rss = 0
    for i in range(0, len(diffs[p])):
        rss += diffs[p][i]**2
    variances[p] = rss/len(diffs[p])
"""

preds = {}
print X
for i in range(1,6):
    preds[positions[i]] = X.dot(models[positions[i]])

b = open('expectedvals', 'w')
for i in range(num_data):
    b.write(lines[i][1]+','+lines[i][0]+',')
    b.write(str(preds[lines[i][0]][i])+',')
    b.write('0'+',')
    b.write(str(lines[i][2])+'\n')
#a,PG,40.0,20,4,10000 
