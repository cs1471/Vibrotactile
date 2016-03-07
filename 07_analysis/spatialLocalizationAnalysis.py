#packages to import
import numpy as np
import scipy.io as sio
import plotly.plotly as py
import statistics as stat
import math as m
import plotly.graph_objs as go
import plotly.tools as tls
from frequencyGenerator import FrequencyGenerator as FG
import os
import glob

tls.set_credentials_file(username='cs1471', api_key='9xknhmjhas')

#################################################################################
#make list of frequencies tested
freqL = FG()
freqL.setFrequencyList()

#################################MAIN##########################################
# filename = input('Enter a filename: \n')
# fileDirectory = input('Enter the directory where you want your figure saved: /n')
# session = input('Enter the session number: \n')

#Use when debugging or manually editing
filename = ('20160217_1154-MR976_block7.144')
fileDirectory = '/Users/courtney/GoogleDrive/Riesenhuber/05_2015_scripts/Vibrotactile/03_spatialLocalization/data/976/'


#load matfile
data = sio.loadmat(fileDirectory + filename, struct_as_record=True)

#pull relevant data from structures
iBlock = 0
#pull relevant data from structures
RT            = data[iBlock]['trialOutput']['RT']
accuracy      = data[iBlock]['trialOutput']['accuracy']
stimuli       = data[iBlock]['trialOutput']['stimuli']
subjectNumber = data[iBlock]['exptdesign']['number'][0,0][0]

if int(data['trialOutput']['preOrPostTrain'][0,0][0]) == 1:
    session = "Pre"
else:
    session = "post"

#############################################################################
#Calculations by position
#############################################################################

#calculate the accuracy by position
iBlock = iTrial = 0
bD_wristPos_accuracy = []
bD_elbowPos_accuracy = []
bD_crossMidline_accuracy = []
bS_wristPos_accuracy = []
bS_elbowPos_accuracy = []
bS_midline_accuracy = []
bD_wristPos_RT = []
bD_elbowPos_RT = []
bD_crossMidline_RT = []
bS_wristPos_RT = []
bS_elbowPos_RT = []
bS_midline_RT = []
for iBlock in range(sResp.size):
    D_wristPos_accuracy = []
    D_elbowPos_accuracy = []
    D_crossMidline_accuracy = []
    S_wristPos_accuracy = []
    S_elbowPos_accuracy = []
    S_midline_accuracy = []
    D_wristPos_RT = []
    D_elbowPos_RT = []
    D_crossMidline_RT = []
    S_wristPos_RT = []
    S_elbowPos_RT = []
    S_midline_RT = []
    for iTrial in range(sResp[0,iBlock].size):
        pos1 = int(stimuli[0,iBlock][1,iTrial])
        pos2 = int(stimuli[0,iBlock][3,iTrial])
        # pos1 = int(stimuli[0,iBlock][0,iTrial])
        # pos2 = int(stimuli[0,iBlock][2,iTrial])
        if pos1 != pos2:
            if (pos1 == 1 or pos1 == 2 or pos1 == 3 or pos1 == 4 or pos1 == 5 or pos1 == 6)\
                    and (pos2 == 1 or pos2 == 2 or pos2 == 3 or pos2 == 4 or pos2 == 5 or pos2 == 6):
                D_wristPos_accuracy.append(accuracy[0,iBlock][0,iTrial])
                D_wristPos_RT.append(RT[0,iBlock][0,iTrial])
            elif (pos1 == 9 or pos1 == 10 or pos1 == 11 or pos1 == 12 or pos1 == 13 or pos1 == 14)\
                    and (pos2 == 9 or pos2 == 10 or pos2 == 11 or pos2 == 12 or pos2 == 13 or pos2 == 14):
                D_elbowPos_accuracy.append(accuracy[0,iBlock][0,iTrial])
                D_elbowPos_RT.append(RT[0,iBlock][0,iTrial])
            else:
                D_crossMidline_accuracy.append(accuracy[0,iBlock][0,iTrial])
                D_crossMidline_RT.append(RT[0,iBlock][0,iTrial])
        else:
            if pos1 == 1 or pos1 == 2 or pos1 == 3 or pos1 == 4:
                S_wristPos_accuracy.append(accuracy[0,iBlock][0,iTrial])
                S_wristPos_RT.append(RT[0,iBlock][0,iTrial])
            elif pos1 == 5 or pos1 == 6 or pos1 == 9 or pos1 == 10:
                S_midline_accuracy.append(accuracy[0,iBlock][0,iTrial])
                S_midline_RT.append(RT[0,iBlock][0,iTrial])
            else:
                S_elbowPos_accuracy.append(accuracy[0,iBlock][0,iTrial])
                S_elbowPos_RT.append(RT[0,iBlock][0,iTrial])

    bD_wristPos_accuracy.append(stat.mean(D_wristPos_accuracy))
    bD_elbowPos_accuracy.append(stat.mean(D_elbowPos_accuracy))
    bD_crossMidline_accuracy.append(stat.mean(D_crossMidline_accuracy))
    bS_wristPos_accuracy.append(stat.mean(S_wristPos_accuracy))
    bS_elbowPos_accuracy.append(stat.mean(S_elbowPos_accuracy))
    bS_midline_accuracy.append(stat.mean(S_midline_accuracy))
    bD_wristPos_RT.append(stat.mean(D_wristPos_RT))
    bD_elbowPos_RT.append(stat.mean(D_elbowPos_RT))
    bD_crossMidline_RT.append(stat.mean(D_crossMidline_RT))
    bS_wristPos_RT.append(stat.mean(S_wristPos_RT))
    bS_elbowPos_RT.append(stat.mean(S_elbowPos_RT))
    bS_midline_RT.append(stat.mean(S_midline_RT))

#############################################################################
#Calculations for stimuli around Boundary
#############################################################################

#calculate the accuracy by position
iBlock = iTrial = 0
bD_pos5v1_ACC = []
bD_pos5v3_ACC = []
bD_pos5v9_ACC = []
bD_pos5v11_ACC = []
bD_pos9v3_ACC = []
bD_pos9v5_ACC = []
bD_pos9v11_ACC = []
bD_pos9v13_ACC = []
bD_pos5v1_RT = []
bD_pos5v3_RT = []
bD_pos5v9_RT = []
bD_pos5v11_RT = []
bD_pos9v3_RT = []
bD_pos9v5_RT = []
bD_pos9v11_RT = []
bD_pos9v13_RT = []

for iBlock in range(sResp.size):
    D_pos5v1_ACC = []
    D_pos5v3_ACC = []
    D_pos5v9_ACC = []
    D_pos5v11_ACC = []
    D_pos9v3_ACC = []
    D_pos9v5_ACC = []
    D_pos9v11_ACC = []
    D_pos9v13_ACC = []
    D_pos5v1_RT = []
    D_pos5v3_RT = []
    D_pos5v9_RT = []
    D_pos5v11_RT = []
    D_pos9v3_RT = []
    D_pos9v5_RT = []
    D_pos9v11_RT = []
    D_pos9v13_RT = []
    for iTrial in range(sResp[0,iBlock].size):
        pos1 = int(stimuli[0,iBlock][1,iTrial])
        pos2 = int(stimuli[0,iBlock][3,iTrial])
        # pos1 = int(stimuli[0,iBlock][0,iTrial])
        # pos2 = int(stimuli[0,iBlock][2,iTrial])
        if ((pos1 == 5 or pos1 == 6) and (pos2 == 1 or pos2 == 2)) \
                or ((pos1 == 1 or pos1 == 2) and (pos2 == 5 or pos2 == 6)):
            D_pos5v1_ACC.append(accuracy[0,iBlock][0,iTrial])
            D_pos5v1_RT.append(RT[0,iBlock][0,iTrial])
        elif ((pos1 == 5 or pos1 == 6) and (pos2 == 3 or pos2 == 4))\
                    or ((pos1 == 3 or pos1 == 4) and (pos2 == 5 or pos2 == 6)):
            D_pos5v3_ACC.append(accuracy[0,iBlock][0,iTrial])
            D_pos5v3_RT.append(RT[0,iBlock][0,iTrial])
        elif ((pos1 == 5 or pos1 == 6) and (pos2 == 9 or pos2 == 10)):
            D_pos5v9_ACC.append(accuracy[0,iBlock][0,iTrial])
            D_pos5v9_RT.append(RT[0,iBlock][0,iTrial])
        elif ((pos1 == 5 or pos1 == 6) and (pos2 == 11 or pos2 ==12))\
                or ((pos1 == 11 or pos1 ==12) and (pos2 == 5 or pos2 ==6)):
            D_pos5v11_ACC.append(accuracy[0,iBlock][0,iTrial])
            D_pos5v11_RT.append(RT[0,iBlock][0,iTrial])
        elif ((pos1 == 9 or pos1 == 10) and (pos2 == 3 or pos2 == 4))\
               or ((pos1 == 3 or pos1 == 4) and (pos2 == 9 or pos2 == 10)):
            D_pos9v3_ACC.append(accuracy[0,iBlock][0,iTrial])
            D_pos9v3_RT.append(RT[0,iBlock][0,iTrial])
        elif ((pos1 == 9 or pos1 == 10) and (pos2 == 5 or pos2 == 6)):
            D_pos9v5_ACC.append(accuracy[0,iBlock][0,iTrial])
            D_pos9v5_RT.append(RT[0,iBlock][0,iTrial])
        elif ((pos1 == 9 or pos1 == 10) and (pos2 == 11 or pos2 == 12))\
                or ((pos1 == 11 or pos1 == 12) and (pos2 == 9 or pos2 ==10)):
            D_pos9v11_ACC.append(accuracy[0,iBlock][0,iTrial])
            D_pos9v11_RT.append(RT[0,iBlock][0,iTrial])
        elif ((pos1 == 9 or pos1 == 10) and (pos2 == 13 or pos2 == 14))\
                or ((pos1 == 13 or pos1 == 14) and (pos2 == 9 or pos2 == 10)):
            D_pos9v13_ACC.append(accuracy[0,iBlock][0,iTrial])
            D_pos9v13_RT.append(RT[0,iBlock][0,iTrial])

    bD_pos5v1_ACC.append(stat.mean(D_pos5v1_ACC))
    bD_pos5v1_RT.append(stat.mean(D_pos5v1_RT))
    bD_pos5v3_ACC.append(stat.mean(D_pos5v3_ACC))
    bD_pos5v3_RT.append(stat.mean(D_pos5v3_RT))
    bD_pos5v9_ACC.append(stat.mean(D_pos5v9_ACC))
    bD_pos5v9_RT.append(stat.mean(D_pos5v9_RT))
    bD_pos5v11_ACC.append(stat.mean(D_pos5v11_ACC))
    bD_pos5v11_RT.append(stat.mean(D_pos5v11_RT))
    bD_pos9v3_ACC.append(stat.mean(D_pos9v3_ACC))
    bD_pos9v3_RT.append(stat.mean(D_pos9v3_RT))
    bD_pos9v5_ACC.append(stat.mean(D_pos9v5_ACC))
    bD_pos9v5_RT.append(stat.mean(D_pos9v5_RT))
    bD_pos9v11_ACC.append(stat.mean(D_pos9v11_ACC))
    bD_pos9v11_RT.append(stat.mean(D_pos9v11_RT))
    bD_pos9v13_ACC.append(stat.mean(D_pos9v13_ACC))
    bD_pos9v13_RT.append(stat.mean(D_pos9v13_RT))

#############################################################################
#Calculating mean acc and RT overall
#############################################################################
#calculate the mean overall accuracy by block
O_accuracy = []
iBlock = 0
for iBlock in range(accuracy.size):
    O_accuracy.append(np.mean(accuracy[0,iBlock]))

#calculate the mean RT overall by block
O_reactionTime = []
iBlock = 0
for iBlock in range(RT.size):
    O_reactionTime.append(np.mean(RT[0,iBlock]))

#x-axis label
# x = []
# i=0
# for i in range(nBlocks):
#             x.append("Block: " + str(i+1)),
x = ["Different", "Same"]
x2 = ["(5,1) vs (9,13)", "(5,3) vs (9,11)", "(5,9) vs (9,5)", "(5,11) vs (9,3)"]
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


#make trace containing acc and RT by position for Different Condition
trace1 = make_trace_bar( x, [stat.mean(bD_wristPos_accuracy), stat.mean(bS_wristPos_accuracy)], "Wrist Accuracy" )
trace2 = make_trace_bar( x, [stat.mean(bD_crossMidline_accuracy), stat.mean(bS_midline_accuracy)], "Across Mid Accuracy" )
trace3 = make_trace_bar( x, [stat.mean(bD_elbowPos_accuracy), stat.mean(S_elbowPos_accuracy)], "Elbow Accuracy" )
trace4 = make_trace_line( x, [stat.mean(bD_wristPos_RT), stat.mean(bS_wristPos_RT)], "Wrist RT" )
trace5 = make_trace_line( x, [stat.mean(bD_crossMidline_RT), stat.mean(bS_midline_RT)], "Across Mid RT" )
trace6 = make_trace_line( x, [stat.mean(bD_elbowPos_RT), stat.mean(bS_elbowPos_RT)], "Elbow RT" )

#make trace parsing out positions 5 and 9
trace7 = make_trace_bar(x2, [stat.mean(bD_pos5v1_ACC), stat.mean(bD_pos5v3_ACC), stat.mean(bD_pos5v9_ACC), stat.mean(bD_pos5v11_ACC)], "Pos 5 Comparisons Acc")
trace8 = make_trace_bar(x2, [stat.mean(bD_pos9v13_ACC), stat.mean(bD_pos9v11_ACC), stat.mean(bD_pos9v5_ACC), stat.mean(bD_pos9v3_ACC)], "Pos 9 Comparisons Acc")
trace9 = make_trace_line(x2, [stat.mean(bD_pos5v1_RT), stat.mean(bD_pos5v3_RT), stat.mean(bD_pos5v9_RT), stat.mean(bD_pos5v11_RT)], "Pos 5 Comparisons RT")
trace10 = make_trace_line(x2, [stat.mean(bD_pos9v13_RT), stat.mean(bD_pos9v11_RT), stat.mean(bD_pos9v5_RT), stat.mean(bD_pos9v3_RT)], "Pos 5 Comparisons RT")

# matFileName = fileDirectory + filename
# dataFile = sio.savemat(matFileName, {'x':x, 'y':y, 'cp_mean': cp_mean, 'mm_mean': mm_mean, 'cb_mean': cb_mean)
# dataFile.write(x,y,cp_mean, mm_mean, cb_mean,)
# dataFile.close()


# Generate Figure object with 2 axes on 2 rows, print axis grid to stdout
fig = tls.make_subplots( rows=1, cols=1, shared_xaxes=True,)
fig2 = tls.make_subplots( rows=1, cols=1, shared_xaxes=True,)

#set figure layout to hold mutlitple bars
fig['layout'].update(barmode='group', bargroupgap=0, bargap=0.25,
    title = subjectNumber + " Accuracy and RT by Position Same v Different " + session)

fig2['layout'].update(barmode='group', bargroupgap=0, bargap=0.25,
    title = subjectNumber + " Accuracy and RT at Position 5 and 9 " + session)

fig['data']  = [trace1, trace2, trace3, trace4, trace5, trace6]
fig2['data'] = [trace7, trace8, trace9, trace10]

#get the url of your figure to embed in html later
first_plot_url = py.plot(fig, filename= subjectName + "AccByMorph" + session, auto_open=False,)
tls.get_embed(first_plot_url)

#bread crumbs to make sure entered the correct information
print("Your graph will be saved in this directory: " + fileDirectory + "\n")
print("Your graph will be saved under: " + filename + "\n")
print("The session number you have indicated is: " + session + "\n")


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
# </html>'''
#
# #save figure data in location specific previously
# f = open(fileDirectory + filename + '.html','w')
# f.write(html_string)

# save images as png in case prefer compared to html
py.image.save_as(fig, fileDirectory + filename + "spatialLoc" + session + ".png")
py.image.save_as(fig2, fileDirectory + filename + "spatialLoc5v9" + session + ".png")
#close all open files
# f.close()

print("Done!")
