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
from frequencyGenerator import FrequencyGenerator as FG

tls.set_credentials_file(username='cs1471', api_key='9xknhmjhas')

# fileDirectory = input('Enter the directory where you want your figure saved: /n')

#Use when debugging or manually editing
fileDirectory = '/Users/courtney/GoogleDrive/Riesenhuber/05_2015_scripts/Vibrotactile/06_frequencyDiscrimination/data/groupData/'

os.chdir(fileDirectory)

data = []
for file in glob.glob("*.mat"):
    data.append(sio.loadmat(file, struct_as_record=True))

#make list of frequencies tested
FG = FG()
FG.setFrequencyList()
FL = [FG.frequencyList[1], FG.frequencyList[7], FG.frequencyList[13], FG.frequencyList[19]]

iSubject = 0
#pull relevant data from structures
RT            = [data[iSubject]['trialOutput']['RT'] for iSubject in range(len(data))]
accuracy      = [data[iSubject]['trialOutput']['accuracy'] for iSubject in range(len(data))]
stimuli       = [data[iSubject]['trialOutput']['stimuli'] for iSubject in range(len(data))]
subjectNumber = [data[iSubject]['exptdesign']['number'][0,0][0] for iSubject in range(len(data))]

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

iTrial = iBlock = iSession = 0
for iSession in range(len(accuracy)):
    b_sameAcc = []
    b_m3w5Acc = []
    b_m3w95Acc = []
    b_m3bAcc = []
    b_m6_95Acc = []
    b_m6_5Acc = []
    b_sameRT = []
    b_m3w5RT = []
    b_m3w95RT = []
    b_m3bRT = []
    b_m6_95RT = []
    b_m6_5RT = []
    for iBlock in range(accuracy[iSession].size):
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
        for iTrial in range(accuracy[iSession][0,iBlock].size):
            stim1 = int(round(stimuli[iSession][0,iBlock][0,iTrial]))
            stim2 = int(round(stimuli[iSession][0,iBlock][2,iTrial]))

            if stim1 == stim2:
                sameAcc.append(accuracy[iSession][0,iBlock][0,iTrial])
                sameRT.append(RT[iSession][0,iBlock][0,iTrial])
            elif (stim1 == FL[3] and stim2 == FL[1]) or (stim1 == FL[3] and stim2 == FL[1]):
                m6_5Acc.append(accuracy[iSession][0,iBlock][0,iTrial])
                m6_5RT.append(RT[iSession][0,iBlock][0,iTrial])
            elif (stim1 == FL[2] and stim2 == FL[0]) or (stim1 == FL[0] and stim2 == FL[2]):
                m6_95Acc.append(accuracy[iSession][0,iBlock][0,iTrial])
                m6_95RT.append(RT[iSession][0,iBlock][0,iTrial])
            elif (stim1 == FL[3] and stim2 == FL[2]) or (stim1 == FL[2] and stim2 == FL[3]):
                m3w5Acc.append(accuracy[iSession][0,iBlock][0,iTrial])
                m3w5RT.append(RT[iSession][0,iBlock][0,iTrial])
            elif (stim1 == FL[0] and stim2 == FL[1]) or (stim1 == FL[1] and stim2 == FL[0]):
                m3w95Acc.append(accuracy[iSession][0,iBlock][0,iTrial])
                m3w95RT.append(RT[iSession][0,iBlock][0,iTrial])
            elif (stim1 == FL[1] and stim2 == FL[2]) or (stim1 == FL[2] and stim2 == FL[1]):
                m3bAcc.append(accuracy[iSession][0,iBlock][0,iTrial])
                m3bRT.append(RT[iSession][0,iBlock][0,iTrial])

        b_sameAcc.append(stat.mean(sameAcc))
        b_m3w5Acc.append(stat.mean(m3w5Acc))
        b_m3w95Acc.append(stat.mean(m3w95Acc))
        b_m3bAcc.append(stat.mean(m3bAcc))
        b_m6_5Acc.append(stat.mean(m6_5Acc))
        b_m6_95Acc.append(stat.mean(m6_95Acc))
        b_sameRT.append(stat.mean(sameRT))
        b_m3w5RT.append(stat.mean(m3w5RT))
        b_m3w95RT.append(stat.mean(m3w95RT))
        b_m3bRT.append(stat.mean(m3bRT))
        b_m6_95RT.append(stat.mean(m6_95RT))
        b_m6_5RT.append(stat.mean(m6_5RT))
    s_sameAcc.append(stat.mean(b_sameAcc))
    s_m3w5Acc.append(stat.mean(b_m3w5Acc))
    s_m3w95Acc.append(stat.mean(b_m3w95Acc))
    s_m3bAcc.append(stat.mean(b_m3bAcc))
    s_m6_5Acc.append(stat.mean(b_m6_5Acc))
    s_m6_95Acc.append(stat.mean(b_m6_95Acc))
    s_sameRT.append(stat.mean(b_sameRT))
    s_m3w5RT.append(stat.mean(b_m3w5RT))
    s_m3w95RT.append(stat.mean(b_m3w95RT))
    s_m3bRT.append(stat.mean(b_m3bRT))
    s_m6_95RT.append(stat.mean(b_m6_95RT))
    s_m6_5RT.append(stat.mean(b_m6_5RT))

#############################################################################
#Calculations by position
#############################################################################

#calculate the reaction time by position
iBlock = iTrial = iSession = 0
sD_pos3or4_RT = []
sD_pos5or6_RT = []
sD_pos9or10_RT = []
sD_pos11or12_RT = []
sS_pos3or4_RT = []
sS_pos5or6_RT = []
sS_pos9or10_RT = []
sS_pos11or12_RT = []
for iSession in range(len(accuracy)):
    bD_pos3or4_RT = []
    bD_pos5or6_RT = []
    bD_pos9or10_RT = []
    bD_pos11or12_RT = []
    bS_pos3or4_RT = []
    bS_pos5or6_RT = []
    bS_pos9or10_RT = []
    bS_pos11or12_RT = []
    for iBlock in range(accuracy[iSession].size):
        D_pos3or4_RT = []
        D_pos5or6_RT = []
        D_pos9or10_RT = []
        D_pos11or12_RT = []
        S_pos3or4_RT = []
        S_pos5or6_RT = []
        S_pos9or10_RT = []
        S_pos11or12_RT = []
        for iTrial in range(accuracy[iSession][0,iBlock].size):
            pos1 = int(stimuli[iSession][0,iBlock][1,iTrial])
            pos2 = int(stimuli[iSession][0,iBlock][3,iTrial])
            stim1 = stimuli[iSession][0,iBlock][0,iTrial]
            stim2 = stimuli[iSession][0,iBlock][2,iTrial]
            if stim1 != stim2:
                if (pos1 == 3 or pos1 == 4):
                    D_pos3or4_RT.append(RT[iSession][0,iBlock][0,iTrial])
                elif (pos1 == 5 or pos1 == 6 or pos1 == 1 or pos1 == 2):
                    D_pos5or6_RT.append(RT[iSession][0,iBlock][0,iTrial])
                elif (pos1 == 9 or pos1 == 10 or pos1 == 13 or pos1 == 14):
                    D_pos9or10_RT.append(RT[iSession][0,iBlock][0,iTrial])
                # elif pos1 == 1 or pos1 == 2:
                #     D_pos5or6_RT.append(RT[0,iBlock][0,iTrial])
                # elif pos1 == 13 or pos1 == 14:
                #     D_pos9or10_RT.append(RT[0,iBlock][0,iTrial])
                elif (pos1 == 11 or pos1 == 12):
                    D_pos11or12_RT.append(RT[iSession][0,iBlock][0,iTrial])
                else:
                    print("Your script is broken and stimuli are not meeting criteria for position of different stimuli")
                    print(stim1, stim2)
                    print(pos1, pos2)
            else:
                if (pos1 == 3 or pos1 == 4):
                    S_pos3or4_RT.append(RT[iSession][0,iBlock][0,iTrial])
                elif (pos1 == 5 or pos1 == 6 or pos1 == 1 or pos1 == 2):
                    S_pos5or6_RT.append(RT[iSession][0,iBlock][0,iTrial])
                elif (pos1 == 9 or pos1 == 10 or pos1 == 13 or pos1 == 14):
                    S_pos9or10_RT.append(RT[iSession][0,iBlock][0,iTrial])
                # elif (pos1 == 1 or pos1 == 2):
                #      S_pos5or6_RT.append(RT[0,iBlock][0,iTrial])
                # elif (pos1 == 13 or pos1 == 14):
                #     S_pos9or10_RT.append(RT[0,iBlock][0,iTrial])
                elif (pos1 == 11 or pos1 == 12):
                    S_pos11or12_RT.append(RT[iSession][0,iBlock][0,iTrial])
                else:
                    print("Your script is broked and stimuli are not meeting criteria for position of same stimuli")
                    print(stim1, stim2)
                    print(pos1, pos2)

        bD_pos3or4_RT.append(stat.mean(D_pos3or4_RT))
        bD_pos5or6_RT.append(stat.mean(D_pos5or6_RT))
        bD_pos9or10_RT.append(stat.mean(D_pos9or10_RT))
        bD_pos11or12_RT.append(stat.mean(D_pos11or12_RT))
        bS_pos3or4_RT.append(stat.mean(S_pos3or4_RT))
        bS_pos5or6_RT.append(stat.mean(S_pos5or6_RT))
        bS_pos9or10_RT.append(stat.mean(S_pos9or10_RT))
        bS_pos11or12_RT.append(stat.mean(S_pos11or12_RT))
    sD_pos3or4_RT.append(stat.mean(bD_pos3or4_RT))
    sD_pos5or6_RT.append(stat.mean(bD_pos5or6_RT))
    sD_pos9or10_RT.append(stat.mean(bD_pos9or10_RT))
    sD_pos11or12_RT.append(stat.mean(bD_pos11or12_RT))
    sS_pos3or4_RT.append(stat.mean(bS_pos3or4_RT))
    sS_pos5or6_RT.append(stat.mean(bS_pos5or6_RT))
    sS_pos9or10_RT.append(stat.mean(bS_pos9or10_RT))
    sS_pos11or12_RT.append(stat.mean(bS_pos11or12_RT))

#calculate the accuracy by position
iBlock = iTrial = iSession = 0
sD_pos3or4_accuracy = []
sD_pos5or6_accuracy = []
sD_pos9or10_accuracy = []
sD_pos11or12_accuracy = []
sS_pos3or4_accuracy = []
sS_pos5or6_accuracy = []
sS_pos9or10_accuracy = []
sS_pos11or12_accuracy = []
for iSession in range(len(accuracy)):
    bD_pos3or4_accuracy = []
    bD_pos5or6_accuracy = []
    bD_pos9or10_accuracy = []
    bD_pos11or12_accuracy = []
    bS_pos3or4_accuracy = []
    bS_pos5or6_accuracy = []
    bS_pos9or10_accuracy = []
    bS_pos11or12_accuracy = []
    for iBlock in range(accuracy[iSession].size):
        D_pos3or4_accuracy = []
        D_pos5or6_accuracy = []
        D_pos9or10_accuracy = []
        D_pos11or12_accuracy = []
        S_pos3or4_accuracy = []
        S_pos5or6_accuracy = []
        S_pos9or10_accuracy = []
        S_pos11or12_accuracy = []
        for iTrial in range(accuracy[iSession][0,iBlock].size):
            pos1 = int(stimuli[iSession][0,iBlock][1,iTrial])
            pos2 = int(stimuli[iSession][0,iBlock][3,iTrial])
            stim1 = stimuli[iSession][0,iBlock][0,iTrial]
            stim2 = stimuli[iSession][0,iBlock][2,iTrial]
            if stim1 != stim2:
                if (pos1 == 3 or pos1 == 4):
                    D_pos3or4_accuracy.append(accuracy[iSession][0,iBlock][0,iTrial])
                elif (pos1 == 5 or pos1 == 6 or pos1 == 1 or pos1 == 2):
                    D_pos5or6_accuracy.append(accuracy[iSession][0,iBlock][0,iTrial])
                elif (pos1 == 9 or pos1 == 10 or pos1 == 13 or pos1 == 14):
                    D_pos9or10_accuracy.append(accuracy[iSession][0,iBlock][0,iTrial])
                # elif pos1 == 1 or pos1 == 2:
                #     D_pos5or6_accuracy.append(accuracy[0,iBlock][0,iTrial])
                # elif pos1 == 13 or pos1 == 14:
                #     D_pos9or10_accuracy.append(accuracy[0,iBlock][0,iTrial])
                elif (pos1 == 11 or pos1 == 12):
                    D_pos11or12_accuracy.append(accuracy[iSession][0,iBlock][0,iTrial])
                else:
                    print("Your script is broken and stimuli are not meeting criteria for position of different stimuli")
                    print(stim1, stim2)
                    print(pos1, pos2)
            else:
                if (pos1 == 3 or pos1 == 4):
                    S_pos3or4_accuracy.append(accuracy[iSession][0,iBlock][0,iTrial])
                elif (pos1 == 5 or pos1 == 6 or pos1 == 1 or pos1 == 2):
                    S_pos5or6_accuracy.append(accuracy[iSession][0,iBlock][0,iTrial])
                elif (pos1 == 9 or pos1 == 10 or pos1 == 13 or pos1 == 14):
                    S_pos9or10_accuracy.append(accuracy[iSession][0,iBlock][0,iTrial])
                # elif pos1 == 1 or pos1 == 2:
                #     S_pos5or6_accuracy.append(accuracy[0,iBlock][0,iTrial])
                # elif pos1 == 13 or pos1 == 14:
                #     S_pos9or10_accuracy.append(accuracy[0,iBlock][0,iTrial])
                elif (pos1 == 11 or pos1 == 12):
                    S_pos11or12_accuracy.append(accuracy[iSession][0,iBlock][0,iTrial])
                else:
                    print("Your script is broken and stimuli are not meeting criteria for position of same stimuli")
                    print(stim1, stim2)
                    print(pos1, pos2)

        bD_pos3or4_accuracy.append(stat.mean(D_pos3or4_accuracy))
        bD_pos5or6_accuracy.append(stat.mean(D_pos5or6_accuracy))
        bD_pos9or10_accuracy.append(stat.mean(D_pos9or10_accuracy))
        bD_pos11or12_accuracy.append(stat.mean(D_pos11or12_accuracy))
        bS_pos3or4_accuracy.append(stat.mean(S_pos3or4_accuracy))
        bS_pos5or6_accuracy.append(stat.mean(S_pos5or6_accuracy))
        bS_pos9or10_accuracy.append(stat.mean(S_pos9or10_accuracy))
        bS_pos11or12_accuracy.append(stat.mean(S_pos11or12_accuracy))
    sD_pos3or4_accuracy.append(stat.mean(bD_pos3or4_accuracy))
    sD_pos5or6_accuracy.append(stat.mean(bD_pos5or6_accuracy))
    sD_pos9or10_accuracy.append(stat.mean(bD_pos9or10_accuracy))
    sD_pos11or12_accuracy.append(stat.mean(bD_pos11or12_accuracy))
    sS_pos3or4_accuracy.append(stat.mean(bS_pos3or4_accuracy))
    sS_pos5or6_accuracy.append(stat.mean(bS_pos5or6_accuracy))
    sS_pos9or10_accuracy.append(stat.mean(bS_pos9or10_accuracy))
    sS_pos11or12_accuracy.append(stat.mean(bS_pos11or12_accuracy))

x = ["Diff Pos3", "Diff Pos5", "Diff Pos9", "Diff Pos11", "Same Pos3", "Same Pos5", "Same Pos9", "Same Pos11"]
x2 = ["Same", "62.50 v 40.00", "90.91 v 62.50", "40.00 v 27.03", "90.91 v 40.00", "62.50 v 27.03"]

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

# Generate Figure object with 2 axes on 2 rows, print axis grid to stdout
figFreq_ACC = tls.make_subplots(rows=1, cols=1, shared_xaxes=True)

figPos_ACC  = tls.make_subplots(rows=1, cols=1, shared_xaxes=True)

figFreq_RT = tls.make_subplots(rows=1, cols=1, shared_xaxes=True)

figPos_RT  = tls.make_subplots(rows=1, cols=1, shared_xaxes=True)

#set figure layout to hold mutlitple bars
figFreq_ACC['layout'].update(barmode='group', bargroupgap=0, bargap=0.25,
    title = "Accuracy by Frequency across conditions")

figPos_ACC['layout'].update(barmode='group', bargroupgap=0, bargap=0.25,
    title = "Accuracy by Position across conditions")

figFreq_RT['layout'].update(barmode='group', bargroupgap=0, bargap=0.25,
    title = "RT by Frequency across conditions")

figPos_RT['layout'].update(barmode='group', bargroupgap=0, bargap=0.25,
    title = "RT by Position across conditions")

figFreq_ACC['data'] = [trace865_A_Freq, trace873_A_Freq, trace888_A_Freq, trace946_A_Freq, trace983_A_Freq, trace998_A_Freq, trace1000_A_Freq, trace1008_A_Freq]
figFreq_RT['data']  = [trace865_RT_Freq, trace873_RT_Freq, trace888_RT_Freq, trace946_RT_Freq, trace983_RT_Freq, trace998_RT_Freq, trace1000_RT_Freq, trace1008_RT_Freq]
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
py.image.save_as(figPos_ACC, fileDirectory + "frequencyDiscrim_Pos_ACC_Group.jpeg")
py.image.save_as(figPos_RT, fileDirectory + "frequencyDiscrim_Pos_RT_Group.jpeg")
#close all open files
# f.close()

print("Done!")
