#packages to import
import numpy as np
import scipy.io as sio
import plotly.plotly as py
import statistics as stat
import math as m
import plotly.graph_objs as go
import plotly.tools as tls
from frequencyFunction_specific import FrequencySpecific

tls.set_credentials_file(username='cs1471', api_key='9xknhmjhas')

#################################################################################
#allows specified increments
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

#generates a list of frequencies that we test
def makeFrequency():
    frequencyList = [i for i in my_range(0, 2.05, 0.1)]

    for index,obj in enumerate(frequencyList):
        obj += m.log2(25)
        frequencyList[index] = round(2**obj)
    return frequencyList

#################################MAIN##########################################
# filename = input('Enter a filename: \n')
# fileDirectory = input('Enter the directory where you want your figure saved: /n')
# session = input('Enter the session number: \n')

#Use when debugging or manually editing
filename      = ('20160315_1108-MR1012_block6')
fileDirectory = '/Users/courtney/GoogleDrive/Riesenhuber/05_2015_scripts/Vibrotactile/01_CategoryTraining/data/1012/'
session       = '3'

#load matfile
data = sio.loadmat(fileDirectory + filename, struct_as_record=True)

#make list of frequencies tested
frequencyList = makeFrequency()

#pull relevant data from structures
RT              = data['trialOutput']['RT']
sResp           = data['trialOutput']['sResp']
correctResponse = data['trialOutput']['correctResponse']
accuracy        = data['trialOutput']['accuracy']
level           = data['trialOutput']['level']
stimuli         = data['trialOutput']['stimuli']
nTrials         = data['exptdesign']['numTrialsPerSession'][0,0][0]
nBlocks         = data['exptdesign']['numSessions'][0,0][0]
subjectName     = data['exptdesign']['subName'][0,0][0]


#############################################################################
#Calculations by Frequency Pair
#############################################################################

#FS = FrequencySpecific(stimuli=stimuli)
#FS.frequencyPair_parse(accuracy)


#############################################################################
#Calculations by morph
#############################################################################

#calculate the accuracy by morph
iBlock = iTrial = 0
b_catProto_accuracy = []
b_middleM_accuracy = []
b_catBound_accuracy = []
b_catProto_RT = []
b_middleM_RT = []
b_catBound_RT = []
for iBlock in range(sResp.size):
    catProto_accuracy = []
    middleM_accuracy = []
    catBound_accuracy = []
    catProto_RT = []
    middleM_RT = []
    catBound_RT = []
    for iTrial in range(sResp[0,iBlock].size):
        stimulus = round(stimuli[0,iBlock][0,iTrial])
        if stimulus == frequencyList[0] or stimulus == frequencyList[1] or stimulus == frequencyList[2]:
            catProto_accuracy.append(accuracy[0,iBlock][0,iTrial])
            catProto_RT.append(RT[0,iBlock][0,iTrial])
        elif stimulus == frequencyList[20] or stimulus == frequencyList[19] or stimulus == frequencyList[18]:
            catProto_accuracy.append(accuracy[0,iBlock][0,iTrial])
            catProto_RT.append(RT[0,iBlock][0,iTrial])
        elif stimulus == frequencyList[3] or stimulus == frequencyList[4] or stimulus == frequencyList[5]:
            middleM_accuracy.append(accuracy[0,iBlock][0,iTrial])
            middleM_RT.append(RT[0,iBlock][0,iTrial])
        elif stimulus == frequencyList[17] or stimulus == frequencyList[16] or stimulus == frequencyList[15]:
            middleM_accuracy.append(accuracy[0,iBlock][0,iTrial])
            middleM_RT.append(RT[0,iBlock][0,iTrial])
        elif stimulus == frequencyList[6] or stimulus == frequencyList[7] or stimulus == frequencyList[8]:
            catBound_accuracy.append(accuracy[0,iBlock][0,iTrial])
            catBound_RT.append(RT[0,iBlock][0,iTrial])
        elif stimulus == frequencyList[14] or stimulus == frequencyList[13] or stimulus == frequencyList[12]:
            catBound_accuracy.append(accuracy[0,iBlock][0,iTrial])
            catBound_RT.append(RT[0,iBlock][0,iTrial])
        else:
            print("There is something wrong with your morph parsing function and stimuli are not be classified")
            print("The following were stimuli were not parsed: ")
            print(stimulus)
    if catProto_accuracy != []:
        b_catProto_accuracy.append(stat.mean(catProto_accuracy))
        b_catProto_RT.append(stat.mean(catProto_RT))
    else:
        b_catProto_accuracy.append(0)
        b_catProto_RT.append(0)

    if middleM_accuracy != []:
        b_middleM_RT.append(stat.mean(middleM_RT))
        b_middleM_accuracy.append(stat.mean(middleM_accuracy))
    else:
        b_middleM_RT.append(0)
        b_middleM_accuracy.append(0)

    if catBound_accuracy != []:
        b_catBound_accuracy.append(stat.mean(catBound_accuracy))
        b_catBound_RT.append(stat.mean(catBound_RT))
    else:
        b_catBound_accuracy.append(0)
        b_catBound_RT.append(0)

#############################################################################
#Calculating mean acc and RT overall
#############################################################################
#calculate the mean overall accuracy by block
O_accuracy = []
iBlock = 0
for iBlock in range(accuracy.size):
    O_accuracy.append(np.mean([accuracy[0,iBlock]]))

#calculate the mean RT overall by block
O_reactionTime = []
iBlock = 0
for iBlock in range(RT.size):
    O_reactionTime.append(np.mean(RT[0,iBlock]))

#x-axis label
x = []
i=0
for i in range(5):
            x.append("Block: " + str(i+1) + ", Level: " + str(level[0,i][0,0])),

#############################################################################
#Generating figures
#############################################################################

# (1.1) Define a trace-generating function (returns a Bar object)
def make_trace_bar(x, y, name):
    return go.Bar(
        x     = x,
        y     = y,            # take in the y-coords
        name  = name,      # label for hover
        xaxis = 'x1',                    # (!) both subplots on same x-axis
        yaxis = 'y1',
    )

# (1.1) Define a trace-generating function (returns a line object)
def make_trace_line(y, name, dash):
     if dash == 'y':
        return go.Scatter(
            x     = x,
            y     = y,            # take in the y-coords
            name  = name,      # label for hover
            xaxis = 'x1',                    # (!) both subplots on same x-axis
            yaxis = 'y1',
                line = dict(
                    dash  = 'dash'
                )
        )
     else:
         return go.Scatter(
            x     = x,
            y     = y,            # take in the y-coords
            name  = name,      # label for hover
            xaxis = 'x1',                    # (!) both subplots on same x-axis
            yaxis = 'y1',
    )

#make trace containing each frequency pair
x2 = ['[25,100]', '[27,91]', '[29,91]', '[31,83]', '[33,77]', '[36,71]', '[38,67]', '[40,62.5]', '[43,59]']

#trace_ACC_FP = make_trace_bar(x2, mF, '')

#make trace containing acc and RT for morph
trace1 = make_trace_bar(x, b_catProto_accuracy,  "Category Prototype Acc")
trace2 = make_trace_bar(x, b_middleM_accuracy, "Middle Morph Acc")
trace3 = make_trace_bar(x, b_catBound_accuracy, "Category Boundary Acc")
trace4 = make_trace_line(b_catProto_RT, "Category Prototype RT", 'n')
trace5 = make_trace_line(b_middleM_RT, "Middle Morph RT", 'n')
trace6 = make_trace_line(b_catBound_RT, "Category Boundary RT", 'n')

#make trace containing overall acc and rt
trace7 = make_trace_line(O_accuracy, "Overall Accuracy", 'y')
trace8 = make_trace_line(O_reactionTime, "Overall RT", 'y')

# Generate Figure object with 2 axes on 2 rows, print axis grid to stdout
fig  = tls.make_subplots(rows=1, cols=1, shared_xaxes=True)
#fig_FP = tls.make_subplots(rows=1, cols=1, shared_xaxes=True)

#set figure layout to hold mutlitple bars
fig['layout'].update(barmode='group', bargroupgap=0, bargap=0.25,
    title = subjectName + " Accuracy and RT By Morph Session " + session, yaxis = dict(dtick = .1))

#fig_FP['layout'].update(barmode='group', bargroupgap=0, bargap=0.25,
#    title = subjectName + " Accuracy and RT By Frequency Pair, Session " + session,  yaxis = dict(dtick = .1))

fig['data']  = [trace1, trace2, trace3, trace7, trace4, trace5, trace6, trace8]
#fig_FP['data'] = [go.Bar(x=x2, y=mF)]
#bread crumbs to make sure entered the correct information
print("Your graph will be saved in this directory: " + fileDirectory + "\n")
print("Your graph will be saved under: " + filename + "\n")
print("The session number you have indicated is: " + session + "\n")



#save images as png in case prefer compared to html
py.image.save_as(fig, fileDirectory + filename + "_CategTrainingMorphAccSession" + session + ".jpeg")
#py.image.save_as(fig_FP, fileDirectory + filename + "_FP_AccSession" + session + ".jpeg")

#close all open files
# f.close()

print("Done!")
