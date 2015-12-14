#from matplotlib import pyplot as plt
import numpy as np
#from  matplotlib import animation
#from pylab import *
import scipy.io as sio
import pandas as pd
from scipy.stats import norm
from math import exp,sqrt

data = sio.loadmat('/Volumes/maxlab/vibrotactile/04_Aim1/02_spatialLocalization/1000/20151118_1239-1000_block7.mat', struct_as_record=True)
trialOutput = data['trialOutput']
exptdesign = data['exptdesign']


#pull relevant data from structures
responseStartTime = data['trialOutput']['responseStartTime']
responseFinishedTime = data['trialOutput']['responseFinishedTime']
RT = data['trialOutput']['RT']
sResp = data['trialOutput']['sResp']
correctResponse = data['trialOutput']['correctResponse']
stimuli = data['trialOutput']['stimuli']
accuracy = data['trialOutput']['accuracy']

x= []
y= []
for i in range(accuracy.size):
    x.append([i])
    y.append([np.mean([accuracy[0,i]])])

#calculating dprime
i=0

hit = []
miss = []
false_alarm =[]
correct_rejection = []
generalMiss = []

for i in range(accuracy.size):
    hit= miss= false_alarm= correct_rejection= generalMiss = 0
    for counter in range(sResp[0,i].size):
        if sResp[0,i][0,counter]==2 and correctResponse[0,i][0,counter]==2:
            hit.append(1)
        elif sResp[0,i][0,counter]==1 and correctResponse[0,i][0,counter]==1:
            correct_rejection.append(1)
        elif sResp[0,i][0,counter]==2 and correctResponse[0,i][0,counter]==1:
            false_alarm.append(1)
        elif sResp[0,i][0,counter]==1 and correctResponse[0,i][0,counter]==2:
            miss.append(1)
        else:
            generalMiss += 1
#
# var trace1 = {
#   x: ['giraffes', 'orangutans', 'monkeys'],
#   y: [20, 14, 23],
#   name: 'SF Zoo',
#   type: 'bar'
# };
#
# var trace2 = {
#   x: ['giraffes', 'orangutans', 'monkeys'],
#   y: [12, 18, 29],
#   name: 'LA Zoo',
#   type: 'bar'
# };
#
# var data = [trace1, trace2];
#
# var layout = {barmode: 'group'};
#
# Plotly.newPlot('myDiv', data, layout);
