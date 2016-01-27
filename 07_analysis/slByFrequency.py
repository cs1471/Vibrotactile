#packages to import
import numpy as np
import scipy.io as sio
import plotly.plotly as py
import statistics as stat
import math as m
import plotly.graph_objs as go
import plotly.tools as tls

tls.set_credentials_file(username='cs1471', api_key='9xknhmjhas')

#################################################################################
#allows specified increments
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

#generates a list of frequencies that we test
def makeFrequency():
    frequencyList = [i for i in my_range(0, 2, 0.1)]

    for index,obj in enumerate(frequencyList):
        obj += m.log2(25)
        frequencyList[index] = round(2**obj)
    return frequencyList

#################################MAIN##########################################
#################################MAIN##########################################
# filename = input('Enter a filename: \n')
# fileDirectory = input('Enter the directory where you want your figure saved: /n')
# session = input('Enter the session number: \n')

#Use when debugging or manually editing
filename = ('20151202_1354-998_block7')
fileDirectory = '/Users/courtneysprouse/GoogleDrive/Riesenhuber/05_2015_scripts/Vibrotactile/03_spatialLocalization/data/998/'


#load matfile
data = sio.loadmat(fileDirectory + filename, struct_as_record=True)

#make list of frequencies tested
frequencyList = makeFrequency()

#pull relevant data from structures
RT = data['trialOutput']['RT']
sResp = data['trialOutput']['sResp']
correctResponse = data['trialOutput']['correctResponse']
accuracy = data['trialOutput']['accuracy']
stimuli = data['trialOutput']['stimuli']
nTrials = data['exptdesign']['numTrialsPerSession'][0,0][0]
nBlocks = data['exptdesign']['numBlocks'][0,0][0]
subjectNumber = data['exptdesign']['number'][0,0][0]
subjectName = data['exptdesign']['subjectName'][0,0][0]

if int(data['trialOutput']['preOrPostTrain'][0,0][0]) == 1:
    session = "Pre"
else:
    session = "post"

#############################################################################
#Calculations by category type
#############################################################################

#calculate accuracy by frequency
b_categoryA = []
b_categoryB = []
iTrial = iBlock = 0
for iBlock in range(sResp.size):
    categoryA = []
    categoryB = []
    for iTrial in range(sResp[0,iBlock].size):
        stimulus = round(stimuli[0,iBlock][1,iTrial])
        if stimulus in frequencyList and stimulus < 47:
            categoryA.append(accuracy[0,iBlock][0,iTrial])
        else:
            categoryB.append(accuracy[0,iBlock][0,iTrial])
    b_categoryA.append(categoryA)
    b_categoryB.append(categoryB)

#calculate accuracy by block for category A
i = 0
mAcc_categoryA = []
for i in range(len(b_categoryA)):
    mAcc_categoryA.append(stat.mean(b_categoryA[i]))

#calculate accuracy by block for category B
i = 0
mAcc_categoryB = []
for i in range(len(b_categoryB)):
    mAcc_categoryB.append(stat.mean(b_categoryB[i]))

#calculate reaction time by category type
b_categoryA_RT = []
b_categoryB_RT = []
iTrial = iBLock = 0
for iBlock in range(sResp.size):
    categoryA_RT = []
    categoryB_RT = []
    for iTrial in range(len(RT[0,iBlock][0])):
        stimulus = round(stimuli[0,iBlock][1,iTrial])
        if stimulus in frequencyList and stimulus < 47:
            categoryA_RT.append(RT[0,iBlock][0,iTrial])
        else:
            categoryB_RT.append(RT[0,iBlock][0,iTrial])
    b_categoryA_RT.append(categoryA_RT)
    b_categoryB_RT.append(categoryB_RT)

#calculate RT by block for category A
iBlock = 0
mRT_categoryA = []
for iBlock, time in enumerate(b_categoryA_RT):
        mRT_categoryA.append(stat.mean(time))

#calculate RT by block for category B
iBlock = 0
mRT_categoryB = []
for iBlock, time in enumerate(b_categoryB_RT):
    mRT_categoryB.append(stat.mean(time))

#make trace containing acc and RT by category
trace15 = make_trace_bar(mAcc_categoryA, "Accuracy Category A")
trace16 = make_trace_bar(mAcc_categoryB, "Accuracy Category B")
trace17 = make_trace_line(mRT_categoryA, "RT Category A")
trace18 = make_trace_line(mRT_categoryB, "RT Category B")