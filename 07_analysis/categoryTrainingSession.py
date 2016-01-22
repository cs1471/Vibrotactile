#packages to import
import numpy as np
import scipy.io as sio
import plotly.plotly as py
import statistics as stat
import math as m
import plotly.graph_objs as go
import plotly.tools as tls
import glob
import os

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

fileDirectory = '/Users/courtney/GoogleDrive/Riesenhuber/05_2015_scripts/Vibrotactile/01_CategoryTraining/data/1000/'
session = '1'

os.chdir(fileDirectory)

fileList = []
for file in glob.glob("*6.mat"):
    fileList.append(file)
    # if not file:
    #     print("Sorry there is no matfile with 6 blocks of data for the session indicated")
    #     try:
    #         print("Searching for 5 blocks of data for the session indicated")
    #         file in glob.glob("*5.mat")
    #         fileList.append(file)
    #     except FileNotFoundError:
    #         print("Sorry it does not look like that session exists.")



data = []
for fileName in fileList:
    data.append(sio.loadmat(fileDirectory + fileName, struct_as_record=True))

#make list of frequencies tested
frequencyList = makeFrequency()
RT = []
sResp = []
correctResponse = []
accuracy = []
level = []
stimuli = []
nTrials = []
nBlocks = []

for iSession in range(len(data)):
    RT.append(data[iSession]['trialOutput']['RT'])
    sResp.append(data[iSession]['trialOutput']['sResp'])
    correctResponse.append(data[iSession]['trialOutput']['correctResponse'])
    accuracy.append(data[iSession]['trialOutput']['accuracy'])
    level.append(data[iSession]['trialOutput']['level'])
    stimuli.append(data[iSession]['trialOutput']['stimuli'])
    nTrials.append(data[iSession]['exptdesign']['numTrialsPerSession'][0,0][0])
    nBlocks.append(data[iSession]['exptdesign']['numSessions'][0,0][0])
    subjectNumber = data[iSession]['exptdesign']['number'][0,0][0]
    subjectName = data[iSession]['exptdesign']['subjectName'][0,0][0]

nBlocks[0] = 6
nBlocks[1] = 6
nBlocks[2] = 6
nBlocks[3] = 6
nBlocks[4] = 5
nBlocks[5] = 5

#calculate the mean overall accuracy by block
iSession = 0
iBlock = 0
s_accuracy = []
for iSession in range(len(data)):
    b_accuracy = []
    for iBlock in range(nBlocks[iSession]):
        b_accuracy.append(stat.mean(accuracy[iSession][0,iBlock][0]))
    s_accuracy.append(stat.mean(b_accuracy))

#calculate the mean RT overall by block
iSession = 0
iBlock = 0
s_reactionTime = []
for iSession in range(len(data)):
    b_reactionTime = []
    for iBlock in range(nBlocks[iSession]):
        b_reactionTime.append(stat.mean(RT[iSession][0,iBlock][0]))
    s_reactionTime.append(stat.mean(b_reactionTime))



#############################################################################
#Generating figures
#############################################################################

#x-axis label
x=[]
iSession = 0
for iSession in range(len(data)):
            x.append("Session: " + str(iSession+1)),

# (1.1) Define a trace-generating function (returns a Bar object)
def make_trace_bar(y, name):
    return go.Bar(
        x     = x,
        y     = y,            # take in the y-coords
        name  = name,      # label for hover
        xaxis = 'x1',                    # (!) both subplots on same x-axis
        yaxis = 'y1',
        marker = dict(
            color = 'rgb(255, 97, 3)',
            line = dict(
                width = 1.5,
                color = 'black'
            )
        )
    )

# (1.1) Define a trace-generating function (returns a line object)
def make_trace_line(y, name):
    return go.Scatter(
        x      = x,
        y      = y,            # take in the y-coords
        name   = name,      # label for hover
        xaxis  = 'x1',                    # (!) both subplots on same x-axis
        yaxis  = 'y1',
        marker = dict(
            color = 'white',
            line  = dict(
                width = 2
            )
        )
    )



trace1 = make_trace_bar(s_accuracy, "Session Accuracy")
trace2 = make_trace_line(s_reactionTime, "Session Reaction Time")

fig = go.Figure()

fig['data'] = [trace1, trace2]

fig['layout'].update(
    barmode       = 'group',
    bargroupgap   = 0,
    bargap        = 0.4,
    title         = "Accuracy and Reaction across Training Sessions",
    paper_bgcolor = 'rgba(0,0,0,0)',
    plot_bgcolor  = 'rgba(0,0,0,0)',
    font          = dict(
        color = 'white',
    )
)

py.image.save_as(fig, "/Users/courtney/Desktop/" + subjectName + "CategoryTrainingOverall.png")
