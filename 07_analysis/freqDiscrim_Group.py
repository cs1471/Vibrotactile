#packages to import
import scipy.io as sio
import plotly.plotly as py
import statistics as stat
import math as m
import plotly.graph_objs as go
import plotly.tools as tls
import glob
import os
from frequencyGenerator import FrequencyGenerator as FG
from dPrime import Dprime

tls.set_credentials_file(username='cs1471', api_key='9xknhmjhas')

# filename = input('Enter a filename: \n')
# fileDirectory = input('Enter the directory where you want your figure saved: /n')
# session = input('Enter the session number: \n')

#Use when debugging or manually editing
filename = ['20160209_1659-MR865_block7', '20160128_1530-MR873_block7', '20160127_1651-MR888_block7', '20160202_1521-MR946_block7',
            '20151119_1059-983_block7', '20151120_1522-998_block5', '20151120_1031-1000_block5', '20160205_1552-MR1008_block7']
fileDirectory = '/Users/courtney/GoogleDrive/Riesenhuber/05_2015_scripts/Vibrotactile/06_frequencyDiscrimination/data/'

data865  = sio.loadmat(fileDirectory + '865/' + filename[0], struct_as_record=True)
data873  = sio.loadmat(fileDirectory + '873/' + filename[1], struct_as_record=True)
data888  = sio.loadmat(fileDirectory + '888/' + filename[2], struct_as_record=True)
data946  = sio.loadmat(fileDirectory + '946/' + filename[3], struct_as_record=True)
data983  = sio.loadmat(fileDirectory + '983/' + filename[4], struct_as_record=True)
data998  = sio.loadmat(fileDirectory + '998/' + filename[5], struct_as_record=True)
data1000 = sio.loadmat(fileDirectory + '1000/' + filename[6], struct_as_record=True)
data1008 = sio.loadmat(fileDirectory + '1008/' + filename[7], struct_as_record=True)

#make list of frequencies tested
FreqObj = FG()
FreqObj.setFrequencyList()

#pull relevant data from structures
#pull relevant data from structures
RT            = [ data865['trialOutput']['RT'], data873['trialOutput']['RT'], data888['trialOutput']['RT'], data946['trialOutput']['RT'],
                  data983['trialOutput']['RT'], data998['trialOutput']['RT'], data1000['trialOutput']['RT'], data1008['trialOutput']['RT']]
accuracy      = [ data865['trialOutput']['accuracy'], data873['trialOutput']['accuracy'], data888['trialOutput']['accuracy'], data946['trialOutput']['accuracy'],
                  data983['trialOutput']['accuracy'], data998['trialOutput']['accuracy'], data1000['trialOutput']['accuracy'], data1008['trialOutput']['accuracy']]
stimuli       = [ data865['trialOutput']['stimuli'], data873['trialOutput']['stimuli'], data888['trialOutput']['stimuli'], data946['trialOutput']['stimuli'],
                  data983['trialOutput']['stimuli'], data998['trialOutput']['stimuli'], data1000['trialOutput']['stimuli'], data1008['trialOutput']['stimuli']]
subjectNumber = [ data865['exptdesign']['number'][0,0][0], data873['exptdesign']['number'][0,0][0], data888['exptdesign']['number'][0,0][0], data946['exptdesign']['number'][0,0][0],
                  data983['exptdesign']['number'][0,0][0], data998['exptdesign']['number'][0,0][0], data1000['exptdesign']['number'][0,0][0], data1008['exptdesign']['number'][0,0][0]]

#############################################################################
#Calculations by Acc category type
#############################################################################

#calculate accuracy by frequency
s_sameAcc = []
s_m3w5Acc = []
s_m3w95Acc = []
s_m3bAcc = []
s_m6_95Acc = []
s_m6_5Acc = []
s_sameRT = []
s_m3w5RT = []
s_m3w95RT = []
s_m3bRT = []
s_m6_95RT = []
s_m6_5RT = []

FL = [FreqObj.frequencyList[1], FreqObj.frequencyList[7], FreqObj.frequencyList[13], FreqObj.frequencyList[19]]

iTrial = iBlock = iSubject = 0
for iSubject in range(len(accuracy)):
    for iBlock in range(accuracy[iSubject].size):
        sameAcc = []
        m3w5Acc = []
        m3w95Acc = []
        m3bAcc = []
        m6_5Acc = []
        m6_95Acc = []
        sameRT = []
        m3w5RT = []
        m3w95RT = []
        m3bRT = []
        m6_95RT = []
        m6_5RT = []
        for iTrial in range(accuracy[iSubject][0,iBlock].size):
            stim1 = int(round(stimuli[iSubject][0,iBlock][0,iTrial]))
            stim2 = int(round(stimuli[iSubject][0,iBlock][2,iTrial]))

            if stim1 == stim2:
                sameAcc.append(accuracy[iSubject][0,iBlock][0,iTrial])
                sameRT.append(RT[iSubject][0,iBlock][0,iTrial])
            elif (stim1 == FL[3] and stim2 == FL[1]) or (stim1 == FL[3] and stim2 == FL[1]):
                m6_5Acc.append(accuracy[iSubject][0,iBlock][0,iTrial])
                m6_5RT.append(RT[iSubject][0,iBlock][0,iTrial])
            elif (stim1 == FL[2] and stim2 == FL[0]) or (stim1 == FL[0] and stim2 == FL[2]):
                m6_95Acc.append(accuracy[iSubject][0,iBlock][0,iTrial])
                m6_95RT.append(RT[iSubject][0,iBlock][0,iTrial])
            elif (stim1 == FL[3] and stim2 == FL[2]) or (stim1 == FL[2] and stim2 == FL[3]):
                m3w5Acc.append(accuracy[iSubject][0,iBlock][0,iTrial])
                m3w5RT.append(RT[iSubject][0,iBlock][0,iTrial])
            elif (stim1 == FL[0] and stim2 == FL[1]) or (stim1 == FL[1] and stim2 == FL[0]):
                m3w95Acc.append(accuracy[iSubject][0,iBlock][0,iTrial])
                m3w95RT.append(RT[iSubject][0,iBlock][0,iTrial])
            elif (stim1 == FL[1] and stim2 == FL[2]) or (stim1 == FL[2] and stim2 == FL[1]):
                m3bAcc.append(accuracy[iSubject][0,iBlock][0,iTrial])
                m3bRT.append(RT[iSubject][0,iBlock][0,iTrial])

    s_sameAcc.append(stat.mean(sameAcc))
    s_m3w5Acc.append(stat.mean(m3w5Acc))
    s_m3w95Acc.append(stat.mean(m3w95Acc))
    s_m3bAcc.append(stat.mean(m3bAcc))
    s_m6_5Acc.append(stat.mean(m6_5Acc))
    s_m6_95Acc.append(stat.mean(m6_95Acc))
    s_sameRT.append(stat.mean(sameRT))
    s_m3w5RT.append(stat.mean(m3w5RT))
    s_m3w95RT.append(stat.mean(m3w95RT))
    s_m3bRT.append(stat.mean(m3bRT))
    s_m6_95RT.append(stat.mean(m6_95RT))
    s_m6_5RT.append(stat.mean(m6_5RT))

#############################################################################
#Calculations by position
#############################################################################

#calculate the reaction time by position
iBlock = iTrial = iSubject = 0
sD_pos3or4_RT = []
sD_pos5or6_RT = []
sD_pos9or10_RT = []
sD_pos11or12_RT = []
sS_pos3or4_RT = []
sS_pos5or6_RT = []
sS_pos9or10_RT = []
sS_pos11or12_RT = []
for iSubject in range(len(accuracy)):
    for iBlock in range(accuracy[iSubject].size):
        D_pos3or4_RT = []
        D_pos5or6_RT = []
        D_pos9or10_RT = []
        D_pos11or12_RT = []
        S_pos3or4_RT = []
        S_pos5or6_RT = []
        S_pos9or10_RT = []
        S_pos11or12_RT = []
        for iTrial in range(accuracy[iSubject][0,iBlock].size):
            pos1 = int(stimuli[iSubject][0,iBlock][1,iTrial])
            pos2 = int(stimuli[iSubject][0,iBlock][3,iTrial])
            stim1 = stimuli[iSubject][0,iBlock][0,iTrial]
            stim2 = stimuli[iSubject][0,iBlock][2,iTrial]
            if stim1 != stim2:
                if (pos1 == 3 or pos1 == 4):
                    D_pos3or4_RT.append(RT[iSubject][0,iBlock][0,iTrial])
                elif (pos1 == 5 or pos1 == 6 or pos1 == 1 or pos1 == 2):
                    D_pos5or6_RT.append(RT[iSubject][0,iBlock][0,iTrial])
                elif (pos1 == 9 or pos1 == 10 or pos1 == 13 or pos1 == 14):
                    D_pos9or10_RT.append(RT[iSubject][0,iBlock][0,iTrial])
                # elif pos1 == 1 or pos1 == 2:
                #     D_pos5or6_RT.append(RT[0,iBlock][0,iTrial])
                # elif pos1 == 13 or pos1 == 14:
                #     D_pos9or10_RT.append(RT[0,iBlock][0,iTrial])
                elif (pos1 == 11 or pos1 == 12):
                    D_pos11or12_RT.append(RT[iSubject][0,iBlock][0,iTrial])
                else:
                    print("Your script is broked and stimuli are not meeting criteria for position of different stimuli")
                    print(stim1, stim2)
                    print(pos1, pos2)
            else:
                if (pos1 == 3 or pos1 == 4):
                    S_pos3or4_RT.append(RT[iSubject][0,iBlock][0,iTrial])
                elif (pos1 == 5 or pos1 == 6 or pos1 == 1 or pos1 == 2):
                    S_pos5or6_RT.append(RT[iSubject][0,iBlock][0,iTrial])
                elif (pos1 == 9 or pos1 == 10 or pos1 == 13 or pos1 == 14):
                    S_pos9or10_RT.append(RT[iSubject][0,iBlock][0,iTrial])
                # elif (pos1 == 1 or pos1 == 2):
                #      S_pos5or6_RT.append(RT[0,iBlock][0,iTrial])
                # elif (pos1 == 13 or pos1 == 14):
                #     S_pos9or10_RT.append(RT[0,iBlock][0,iTrial])
                elif (pos1 == 11 or pos1 == 12):
                    S_pos11or12_RT.append(RT[iSubject][0,iBlock][0,iTrial])
                else:
                    print("Your script is broked and stimuli are not meeting criteria for position of same stimuli")
                    print(stim1, stim2)
                    print(pos1, pos2)

    sD_pos3or4_RT.append(stat.mean(D_pos3or4_RT))
    sD_pos5or6_RT.append(stat.mean(D_pos5or6_RT))
    sD_pos9or10_RT.append(stat.mean(D_pos9or10_RT))
    sD_pos11or12_RT.append(stat.mean(D_pos11or12_RT))
    sS_pos3or4_RT.append(stat.mean(S_pos3or4_RT))
    sS_pos5or6_RT.append(stat.mean(S_pos5or6_RT))
    sS_pos9or10_RT.append(stat.mean(S_pos9or10_RT))
    sS_pos11or12_RT.append(stat.mean(S_pos11or12_RT))

#calculate the accuracy by position
iBlock = iTrial = iSubject = 0
sD_pos3or4_accuracy = []
sD_pos5or6_accuracy = []
sD_pos9or10_accuracy = []
sD_pos11or12_accuracy = []
sS_pos3or4_accuracy = []
sS_pos5or6_accuracy = []
sS_pos9or10_accuracy = []
sS_pos11or12_accuracy = []
for iSubject in range(len(accuracy)):
    for iBlock in range(accuracy[iSubject].size):
        D_pos3or4_accuracy = []
        D_pos5or6_accuracy = []
        D_pos9or10_accuracy = []
        D_pos11or12_accuracy = []
        S_pos3or4_accuracy = []
        S_pos5or6_accuracy = []
        S_pos9or10_accuracy = []
        S_pos11or12_accuracy = []
        for iTrial in range(accuracy[iSubject][0,iBlock].size):
            pos1 = int(stimuli[iSubject][0,iBlock][1,iTrial])
            pos2 = int(stimuli[iSubject][0,iBlock][3,iTrial])
            stim1 = stimuli[iSubject][0,iBlock][0,iTrial]
            stim2 = stimuli[iSubject][0,iBlock][2,iTrial]
            if stim1 != stim2:
                if (pos1 == 3 or pos1 == 4):
                    D_pos3or4_accuracy.append(accuracy[iSubject][0,iBlock][0,iTrial])
                elif (pos1 == 5 or pos1 == 6 or pos1 == 1 or pos1 == 2):
                    D_pos5or6_accuracy.append(accuracy[iSubject][0,iBlock][0,iTrial])
                elif (pos1 == 9 or pos1 == 10 or pos1 == 13 or pos1 == 14):
                    D_pos9or10_accuracy.append(accuracy[iSubject][0,iBlock][0,iTrial])
                # elif pos1 == 1 or pos1 == 2:
                #     D_pos5or6_accuracy.append(accuracy[0,iBlock][0,iTrial])
                # elif pos1 == 13 or pos1 == 14:
                #     D_pos9or10_accuracy.append(accuracy[0,iBlock][0,iTrial])
                elif (pos1 == 11 or pos1 == 12):
                    D_pos11or12_accuracy.append(accuracy[iSubject][0,iBlock][0,iTrial])
                else:
                    print("Your script is broken and stimuli are not meeting criteria for position of different stimuli")
                    print(stim1, stim2)
                    print(pos1, pos2)
            else:
                if (pos1 == 3 or pos1 == 4):
                    S_pos3or4_accuracy.append(accuracy[iSubject][0,iBlock][0,iTrial])
                elif (pos1 == 5 or pos1 == 6 or pos1 == 1 or pos1 == 2):
                    S_pos5or6_accuracy.append(accuracy[iSubject][0,iBlock][0,iTrial])
                elif (pos1 == 9 or pos1 == 10 or pos1 == 13 or pos1 == 14):
                    S_pos9or10_accuracy.append(accuracy[iSubject][0,iBlock][0,iTrial])
                # elif pos1 == 1 or pos1 == 2:
                #     S_pos5or6_accuracy.append(accuracy[0,iBlock][0,iTrial])
                # elif pos1 == 13 or pos1 == 14:
                #     S_pos9or10_accuracy.append(accuracy[0,iBlock][0,iTrial])
                elif (pos1 == 11 or pos1 == 12):
                    S_pos11or12_accuracy.append(accuracy[iSubject][0,iBlock][0,iTrial])
                else:
                    print("Your script is broken and stimuli are not meeting criteria for position of same stimuli")
                    print(stim1, stim2)
                    print(pos1, pos2)

    sD_pos3or4_accuracy.append(stat.mean(D_pos3or4_accuracy))
    sD_pos5or6_accuracy.append(stat.mean(D_pos5or6_accuracy))
    sD_pos9or10_accuracy.append(stat.mean(D_pos9or10_accuracy))
    sD_pos11or12_accuracy.append(stat.mean(D_pos11or12_accuracy))
    sS_pos3or4_accuracy.append(stat.mean(S_pos3or4_accuracy))
    sS_pos5or6_accuracy.append(stat.mean(S_pos5or6_accuracy))
    sS_pos9or10_accuracy.append(stat.mean(S_pos9or10_accuracy))
    sS_pos11or12_accuracy.append(stat.mean(S_pos11or12_accuracy))

#############################################################################
#Calculating dPrime
#############################################################################
dPrimeObj = Dprime()
dPrimeObj.parseData(accuracy, stimuli)
dprime = dPrimeObj.dPrimeCalc()



x = ["Diff Pos3", "Diff Pos5", "Diff Pos9", "Diff Pos11", "Same Pos3", "Same Pos5", "Same Pos9", "Same Pos11"]
x2 = ["Same", "62.50 v 40.00", "90.91 v 62.50", "40.00 v 27.03", "90.91 v 40.00", "62.50 v 27.03"]
x3 = ['Dprime', 'True Positive Rate', 'False Positive Rate', 'True Negative Rate', 'False Negative Rate']

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
        yaxis = 'y1'
    )

# (1.1) Define a trace-generating function (returns a line object)
def make_trace_line(x, y, name):
    return go.Scatter(
        x     = x,
        y     = y,            # take in the y-coords
        name  = name,      # label for hover
        xaxis = 'x1',                    # (!) both subplots on same x-axis
        yaxis = 'y1'
    )

#make trace containing acc by frequency for Same and different Condition\
trace865_A_Freq   = make_trace_bar(x2, [s_sameAcc[0], s_m3bAcc[0], s_m3w5Acc[0], s_m3w95Acc[0], s_m6_5Acc[0], s_m6_95Acc[0]], "865")
trace865_RT_Freq  = make_trace_line(x2, [s_sameRT[0], s_m3bRT[0], s_m3w5RT[0], s_m3w95RT[0], s_m6_5RT[0], s_m6_95RT[0]], "865")
trace873_A_Freq   = make_trace_bar(x2, [s_sameAcc[1], s_m3bAcc[1], s_m3w5Acc[1], s_m3w95Acc[1], s_m6_5Acc[1], s_m6_95Acc[1]], "873")
trace873_RT_Freq  = make_trace_line(x2, [s_sameRT[1], s_m3bRT[1], s_m3w5RT[1], s_m3w95RT[1], s_m6_5RT[1], s_m6_95RT[1]], "873")
trace888_A_Freq   = make_trace_bar(x2, [s_sameAcc[2], s_m3bAcc[2], s_m3w5Acc[2], s_m3w95Acc[2], s_m6_5Acc[2], s_m6_95Acc[2]], "888")
trace888_RT_Freq  = make_trace_line(x2, [s_sameRT[2], s_m3bRT[2], s_m3w5RT[2], s_m3w95RT[2], s_m6_5RT[2], s_m6_95RT[2]], "888")
trace946_A_Freq   = make_trace_bar(x2, [s_sameAcc[3], s_m3bAcc[3], s_m3w5Acc[3], s_m3w95Acc[3], s_m6_5Acc[3], s_m6_95Acc[3]], "946")
trace946_RT_Freq  = make_trace_line(x2, [s_sameRT[3], s_m3bRT[3], s_m3w5RT[3], s_m3w95RT[3], s_m6_5RT[3], s_m6_95RT[3]], "946")
trace983_A_Freq   = make_trace_bar(x2, [s_sameAcc[4], s_m3bAcc[4], s_m3w5Acc[4], s_m3w95Acc[4], s_m6_5Acc[4], s_m6_95Acc[4]], "983")
trace983_RT_Freq  = make_trace_line(x2, [s_sameRT[4], s_m3bRT[4], s_m3w5RT[4], s_m3w95RT[4], s_m6_5RT[4], s_m6_95RT[4]], "983")
trace998_A_Freq   = make_trace_bar(x2, [s_sameAcc[5], s_m3bAcc[5], s_m3w5Acc[5], s_m3w95Acc[5], s_m6_5Acc[3], s_m6_95Acc[5]], "998")
trace998_RT_Freq  = make_trace_line(x2, [s_sameRT[5], s_m3bRT[5], s_m3w5RT[5], s_m3w95RT[5], s_m6_5RT[5], s_m6_95RT[5]], "998")
trace1000_A_Freq  = make_trace_bar(x2, [s_sameAcc[6], s_m3bAcc[6], s_m3w5Acc[6], s_m3w95Acc[6], s_m6_5Acc[6], s_m6_95Acc[6]], "1000")
trace1000_RT_Freq = make_trace_line(x2, [s_sameRT[6], s_m3bRT[6], s_m3w5RT[6], s_m3w95RT[6], s_m6_5RT[6], s_m6_95RT[6]], "1000")
trace1008_A_Freq  = make_trace_bar(x2, [s_sameAcc[7], s_m3bAcc[7], s_m3w5Acc[7], s_m3w95Acc[7], s_m6_5Acc[7], s_m6_95Acc[7]], "1008")
trace1008_RT_Freq = make_trace_line(x2, [s_sameRT[7], s_m3bRT[7], s_m3w5RT[7], s_m3w95RT[7], s_m6_5RT[7], s_m6_95RT[7]], "1008")

trace865_A_Pos   = make_trace_bar(x, [sD_pos3or4_accuracy[0], sD_pos5or6_accuracy[0], sD_pos9or10_accuracy[0], sD_pos11or12_accuracy[0],
                                   sS_pos3or4_accuracy[0], sS_pos5or6_accuracy[0], sS_pos9or10_accuracy[0], sS_pos11or12_accuracy[0] ], "865")
trace865_RT_Pos  = make_trace_line(x, [sD_pos3or4_RT[0], sD_pos5or6_RT[0], sD_pos9or10_RT[0], sD_pos11or12_RT[0],
                                   sS_pos3or4_RT[0], sS_pos5or6_RT[0], sS_pos9or10_RT[0], sS_pos11or12_RT[0] ], "865")
trace873_A_Pos   = make_trace_bar(x, [sD_pos3or4_accuracy[1], sD_pos5or6_accuracy[1], sD_pos9or10_accuracy[1], sD_pos11or12_accuracy[1],
                                   sS_pos3or4_accuracy[1], sS_pos5or6_accuracy[1], sS_pos9or10_accuracy[1], sS_pos11or12_accuracy[1]], "873")
trace873_RT_Pos  = make_trace_line(x, [sD_pos3or4_RT[1], sD_pos5or6_RT[1], sD_pos9or10_RT[1], sD_pos11or12_RT[1],
                                   sS_pos3or4_RT[1], sS_pos5or6_RT[1], sS_pos9or10_RT[1], sS_pos11or12_RT[1] ], "873")
trace888_A_Pos   = make_trace_bar(x, [sD_pos3or4_accuracy[2], sD_pos5or6_accuracy[2], sD_pos9or10_accuracy[2], sD_pos11or12_accuracy[2],
                                   sS_pos3or4_accuracy[2], sS_pos5or6_accuracy[2], sS_pos9or10_accuracy[2], sS_pos11or12_accuracy[2]], "888")
trace888_RT_Pos  = make_trace_line(x, [sD_pos3or4_RT[2], sD_pos5or6_RT[2], sD_pos9or10_RT[2], sD_pos11or12_RT[2],
                                   sS_pos3or4_RT[2], sS_pos5or6_RT[2], sS_pos9or10_RT[2], sS_pos11or12_RT[2] ], "888")
trace946_A_Pos   = make_trace_bar(x, [sD_pos3or4_accuracy[3], sD_pos5or6_accuracy[3], sD_pos9or10_accuracy[3], sD_pos11or12_accuracy[3],
                                   sS_pos3or4_accuracy[3], sS_pos5or6_accuracy[3], sS_pos9or10_accuracy[3], sS_pos11or12_accuracy[3]], "946")
trace946_RT_Pos  = make_trace_line(x, [sD_pos3or4_RT[3], sD_pos5or6_RT[3], sD_pos9or10_RT[3], sD_pos11or12_RT[3],
                                   sS_pos3or4_RT[3], sS_pos5or6_RT[3], sS_pos9or10_RT[3], sS_pos11or12_RT[3] ], "946")
trace983_A_Pos   = make_trace_bar(x, [sD_pos3or4_accuracy[4], sD_pos5or6_accuracy[4], sD_pos9or10_accuracy[4], sD_pos11or12_accuracy[4],
                                   sS_pos3or4_accuracy[4], sS_pos5or6_accuracy[4], sS_pos9or10_accuracy[4], sS_pos11or12_accuracy[4]], "983")
trace983_RT_Pos  = make_trace_line(x, [sD_pos3or4_RT[4], sD_pos5or6_RT[4], sD_pos9or10_RT[4], sD_pos11or12_RT[4],
                                   sS_pos3or4_RT[4], sS_pos5or6_RT[4], sS_pos9or10_RT[4], sS_pos11or12_RT[4] ], "983")
trace998_A_Pos   = make_trace_bar(x, [sD_pos3or4_accuracy[5], sD_pos5or6_accuracy[5], sD_pos9or10_accuracy[5], sD_pos11or12_accuracy[5],
                                   sS_pos3or4_accuracy[5], sS_pos5or6_accuracy[5], sS_pos9or10_accuracy[5], sS_pos11or12_accuracy[5]], "998")
trace998_RT_Pos  = make_trace_line(x, [sD_pos3or4_RT[5], sD_pos5or6_RT[5], sD_pos9or10_RT[5], sD_pos11or12_RT[5],
                                   sS_pos3or4_RT[5], sS_pos5or6_RT[5], sS_pos9or10_RT[5], sS_pos11or12_RT[5] ], "998")
trace1000_A_Pos  = make_trace_bar(x, [sD_pos3or4_accuracy[6], sD_pos5or6_accuracy[6], sD_pos9or10_accuracy[6], sD_pos11or12_accuracy[6],
                                   sS_pos3or4_accuracy[6], sS_pos5or6_accuracy[6], sS_pos9or10_accuracy[6], sS_pos11or12_accuracy[6]], "1000")
trace1000_RT_Pos = make_trace_line(x, [sD_pos3or4_RT[6], sD_pos5or6_RT[6], sD_pos9or10_RT[6], sD_pos11or12_RT[6],
                                   sS_pos3or4_RT[6], sS_pos5or6_RT[6], sS_pos9or10_RT[6], sS_pos11or12_RT[6] ], "1000")
trace1008_A_Pos  = make_trace_bar(x, [sD_pos3or4_accuracy[7], sD_pos5or6_accuracy[7], sD_pos9or10_accuracy[7], sD_pos11or12_accuracy[7],
                                   sS_pos3or4_accuracy[7], sS_pos5or6_accuracy[7], sS_pos9or10_accuracy[7], sS_pos11or12_accuracy[7]], "1008")
trace1008_RT_Pos = make_trace_line(x, [sD_pos3or4_RT[7], sD_pos5or6_RT[7], sD_pos9or10_RT[7], sD_pos11or12_RT[7],
                                   sS_pos3or4_RT[7], sS_pos5or6_RT[7], sS_pos9or10_RT[7], sS_pos11or12_RT[7] ], "1008")


#make dprime trace
trace865_dprime_Freq   = make_trace_bar(x3, [dprime[0], dPrimeObj.TPR[0], dPrimeObj.FPR[0], dPrimeObj.TNR[0], dPrimeObj.FNR[0]], "865")
trace873_dprime_Freq   = make_trace_bar(x3, [dprime[1], dPrimeObj.TPR[1], dPrimeObj.FPR[1], dPrimeObj.TNR[1], dPrimeObj.FNR[1]], "873")
trace888_dprime_Freq   = make_trace_bar(x3, [dprime[2], dPrimeObj.TPR[2], dPrimeObj.FPR[2], dPrimeObj.TNR[2], dPrimeObj.FNR[2]], "888")
trace946_dprime_Freq   = make_trace_bar(x3, [dprime[3], dPrimeObj.TPR[3], dPrimeObj.FPR[3], dPrimeObj.TNR[3], dPrimeObj.FNR[3]], "946")
trace983_dprime_Freq   = make_trace_bar(x3, [dprime[4], dPrimeObj.TPR[4], dPrimeObj.FPR[4], dPrimeObj.TNR[4], dPrimeObj.FNR[4]], "983")
trace998_dprime_Freq   = make_trace_bar(x3, [dprime[5], dPrimeObj.TPR[5], dPrimeObj.FPR[5], dPrimeObj.TNR[5], dPrimeObj.FNR[3]], "998")
trace1000_dprime_Freq  = make_trace_bar(x3, [dprime[6], dPrimeObj.TPR[6], dPrimeObj.FPR[6], dPrimeObj.TNR[6], dPrimeObj.FNR[6]], "1000")
trace1008_dprime_Freq  = make_trace_bar(x3, [dprime[7], dPrimeObj.TPR[7], dPrimeObj.FPR[7], dPrimeObj.TNR[7], dPrimeObj.FNR[7]], "1008")

# Generate Figure object with 2 axes on 2 rows, print axis grid to stdout
figFreq_ACC = tls.make_subplots(rows=1, cols=1, shared_xaxes=True)

figPos_ACC  = tls.make_subplots(rows=1, cols=1, shared_xaxes=True)

figFreq_RT = tls.make_subplots(rows=1, cols=1, shared_xaxes=True)

figPos_RT  = tls.make_subplots(rows=1, cols=1, shared_xaxes=True)

figDPrime = tls.make_subplots(rows=1, cols=1, shared_xaxes=True)

#set figure layout to hold mutlitple bars
figFreq_ACC['layout'].update(barmode='group', bargroupgap=0, bargap=0.25,
    title = "Accuracy by Frequency on Single Stimuli Frequency Discrimination Task")

figPos_ACC['layout'].update(barmode='group', bargroupgap=0, bargap=0.25,
    title = "Accuracy by Position on Single Stimuli Frequency Discrimination Task")

figDPrime['layout'].update(barmode='group', bargroupgap=0, bargap=0.25,
    title = "Dprime Across Subjects on Single Stimuli Frequency Discrimination Task")

figFreq_RT['layout'].update(barmode='group', bargroupgap=0, bargap=0.25,
    title = "RT by Frequency on Single Stimuli Frequency Discrimination Task")

figPos_RT['layout'].update(barmode='group', bargroupgap=0, bargap=0.25,
    title = "RT by Position on Single Stimuli Frequency Discrimination Task")

figFreq_ACC['data'] = [trace865_A_Freq, trace873_A_Freq, trace888_A_Freq, trace946_A_Freq, trace983_A_Freq, trace998_A_Freq, trace1000_A_Freq, trace1008_A_Freq]
figFreq_RT['data']  = [trace865_RT_Freq, trace873_RT_Freq, trace888_RT_Freq, trace946_RT_Freq, trace983_RT_Freq, trace998_RT_Freq, trace1000_RT_Freq, trace1008_RT_Freq]
figDPrime['data']   = [trace865_dprime_Freq, trace873_dprime_Freq, trace888_dprime_Freq, trace946_dprime_Freq, trace983_dprime_Freq, trace998_dprime_Freq, trace1000_dprime_Freq, trace1008_dprime_Freq]
figPos_ACC['data']  = [trace865_A_Pos, trace873_A_Pos, trace888_A_Pos, trace946_A_Pos, trace983_A_Pos, trace998_A_Pos, trace1000_A_Pos, trace1008_A_Pos]
figPos_RT['data']   = [trace865_RT_Pos, trace873_RT_Pos, trace888_RT_Pos, trace946_RT_Pos, trace983_RT_Pos, trace998_RT_Pos, trace1000_RT_Pos, trace1008_RT_Pos]
#get the url of your figure to embed in html later
# first_plot_url = py.plot(fig, filename= subjectName + "AccByMorph" + session, auto_open=False,)
# tls.get_embed(first_plot_url)
# second_plot_url = py.plot(fig2, filename= subjectName + "RTbyMorph" + session, auto_open=False,)
# tls.get_embed(second_plot_url)
# third_plot_url = py.plot(fig3, filename= subjectName + "AccByCatgeory" + session, auto_open=False,)
# tls.get_embed(third_plot_url)

#bread crumbs to make sure entered the correct information
print("Your graph will be saved in this directory: " + fileDirectory + "\n")

# #embed figure data in html
# html_string = '''
# <html>
#     <head>
#         <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
#         <style>body{ margin:0 100; background:whitesmoke; }</style>
#     </head>
#     <body>
#         <!-- *** FirstPlot *** --->
#         <iframe width="1000" height="550" frameborder="0" seamless="seamless" scrolling="no" \
# src="'''+ first_plot_url + '''.embed?width=800&height=550"></iframe>
#         <!-- *** Second Plot *** --->
#         <iframe width="1000" height="550" frameborder="0" seamless="seamless" scrolling="no" \
# src="'''+ second_plot_url + '''.embed?width=800&height=550"></iframe>
#         <!-- *** ThirdPlot *** --->
#         <iframe width="1000" height="550" frameborder="0" seamless="seamless" scrolling="no" \
# src="'''+ third_plot_url + '''.embed?width=800&height=550"></iframe>
# </html>'''
#
# #save figure data in location specific previously
# f = open(fileDirectory + filename + '.html','w')
# f.write(html_string)

# save images as png in case prefer compared to html
py.image.save_as(figFreq_ACC, fileDirectory + "frequencyDiscrim_Freq_ACC_Group.jpeg")
py.image.save_as(figFreq_RT, fileDirectory + "frequencyDiscrim_Freq_RT_Group.jpeg")
py.image.save_as(figDPrime, fileDirectory + "frequencyDiscrim_Dprime_Group.jpeg")
py.image.save_as(figPos_ACC, fileDirectory + "frequencyDiscrim_Pos_ACC_Group.jpeg")
py.image.save_as(figPos_RT, fileDirectory + "frequencyDiscrim_Pos_RT_Group.jpeg")
#close all open files
# f.close()

print("Done!")
