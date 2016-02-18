#packages to import
import numpy as np
import scipy.io as sio
import plotly.plotly as py
import statistics as stat
import plotly.graph_objs as go
import plotly.tools as tls
from dPrime import Dprime
from frequencyGenerator import FrequencyGenerator as FG
from Position import Position


tls.set_credentials_file(username='cs1471', api_key='9xknhmjhas')

# filename = input('Enter a filename: \n')
# fileDirectory = input('Enter the directory where you want your figure saved: /n')
# session = input('Enter the session number: \n')

#Use when debugging or manually editing
filename = ['MR873_block7.144', 'MR946_block7.144', '20151118_1817-983_block7', '20151202_1354-998_block7', '20151118_1239-1000_block7', 'MR1008_block7.144']
fileDirectory = '/Users/courtney/GoogleDrive/Riesenhuber/05_2015_scripts/Vibrotactile/03_spatialLocalization/data/'


#load matfile
data873  = sio.loadmat(fileDirectory + '873/' + filename[0], struct_as_record=True)
data946  = sio.loadmat(fileDirectory + '946/' + filename[1], struct_as_record=True)
data983  = sio.loadmat(fileDirectory + '983/' + filename[2], struct_as_record=True)
data998  = sio.loadmat(fileDirectory + '998/' + filename[3], struct_as_record=True)
data1000 = sio.loadmat(fileDirectory + '1000/' + filename[4], struct_as_record=True)
data1008 = sio.loadmat(fileDirectory + '1008/' + filename[5], struct_as_record=True)


#make list of frequencies tested
freqL = FG()
freqL.setFrequencyList()

#pull relevant data from structures
RT = [data873['trialOutput']['RT'], data946['trialOutput']['RT'], data983['trialOutput']['RT'],
      data998['trialOutput']['RT'], data1000['trialOutput']['RT'], data1008['trialOutput']['RT']]
accuracy = [data873['trialOutput']['accuracy'], data946['trialOutput']['accuracy'], data983['trialOutput']['accuracy'],
            data998['trialOutput']['accuracy'], data1000['trialOutput']['accuracy'], data1008['trialOutput']['accuracy']]
stimuli = [data873['trialOutput']['stimuli'], data946['trialOutput']['stimuli'], data983['trialOutput']['stimuli'],
           data998['trialOutput']['stimuli'], data1000['trialOutput']['stimuli'], data1008['trialOutput']['stimuli']]
subjectNumber = [data873['exptdesign']['number'][0,0][0], data946['exptdesign']['number'][0,0][0], data983['exptdesign']['number'][0,0][0],
                 data998['exptdesign']['number'][0,0][0], data1000['exptdesign']['number'][0,0][0], data1008['exptdesign']['number'][0,0][0]]

#############################################################################
#Calculations by position
#############################################################################

positionObj = Position()
positionObj.parseData(accuracy, RT, stimuli)

#############################################################################
#Calculations by position
#############################################################################

dprimeObj = Dprime()
dprimeObj.dPrimeCalc()

#############################################################################
#Calculating mean acc and RT overall
#############################################################################
#calculate the mean overall accuracy by block
sO_accuracy = []
iBlock = iSubject = 0
for iSubject in range(len(accuracy)):
    O_accuracy = []
    for iBlock in range(accuracy[iSubject].size):
        O_accuracy.append(np.mean(accuracy[iSubject][0,iBlock]))
sO_accuracy.append(stat.mean(O_accuracy))

#calculate the mean RT overall by block
sO_reactionTime = []
iBlock = iSubject = 0
for iSubject in range(len(RT)):
    O_reactionTime = []
    for iBlock in range(RT[iSubject].size):
        O_reactionTime.append(np.mean(RT[iSubject][0,iBlock]))
sO_reactionTime.append(stat.mean(O_reactionTime))

x = ["Different", "Same"]
x2 = ["(5,1)", "(9,13)", "(5,3)", "(9,11)", "(5,9)", "(9,5)", "(5,11)", "(9,3)"]
x3 = ["D_Wrist Accuracy", "D_Midline Accuracy", "D_Elbow Accuracy", "S_Wrist Accuracy", "S_Midline Accuracy", "S_Elbow Accuracy"]
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
trace873_Pos_ACC  = make_trace_bar( x3, [positionObj.PG.ACC[0[0]], sD_crossMidline_accuracy[0], sD_elbowPos_accuracy[0],
                                         sS_wristPos_accuracy[0], sS_midline_accuracy[0], sS_elbowPos_accuracy[0]], "873" )
trace946_Pos_ACC  = make_trace_bar( x3, [sD_wristPos_accuracy[1], sD_crossMidline_accuracy[1], sD_elbowPos_accuracy[1],
                                         sS_wristPos_accuracy[1], sS_midline_accuracy[1], sS_elbowPos_accuracy[1]], "946" )
trace983_Pos_ACC  = make_trace_bar( x3, [sD_wristPos_accuracy[2], sD_crossMidline_accuracy[2], sD_elbowPos_accuracy[2],
                                         sS_wristPos_accuracy[2], sS_midline_accuracy[2], sS_elbowPos_accuracy[2]], "983" )
trace998_Pos_ACC  = make_trace_bar( x3, [sD_wristPos_accuracy[3], sD_crossMidline_accuracy[3], sD_elbowPos_accuracy[3],
                                         sS_wristPos_accuracy[3], sS_midline_accuracy[3], sS_elbowPos_accuracy[3]], "998" )
trace1000_Pos_ACC = make_trace_bar( x3, [sD_wristPos_accuracy[4], sD_crossMidline_accuracy[4], sD_elbowPos_accuracy[4],
                                         sS_wristPos_accuracy[4], sS_midline_accuracy[4], sS_elbowPos_accuracy[4]], "1000" )
trace1008_Pos_ACC = make_trace_bar( x3, [sD_wristPos_accuracy[5], sD_crossMidline_accuracy[5], sD_elbowPos_accuracy[5],
                                         sS_wristPos_accuracy[5], sS_midline_accuracy[5], sS_elbowPos_accuracy[5]], "1008" )

trace873_Pos_RT   = make_trace_line( x3, [sD_wristPos_RT[0], sD_crossMidline_RT[0], sD_elbowPos_RT[0],
                                         sS_wristPos_RT[0], sS_midline_RT[0], sS_elbowPos_RT[0]], "873")
trace946_Pos_RT   = make_trace_line( x3, [sD_wristPos_RT[1], sD_crossMidline_RT[1], sD_elbowPos_RT[1],
                                         sS_wristPos_RT[1], sS_midline_RT[1], sS_elbowPos_RT[1]], "946")
trace983_Pos_RT   = make_trace_line( x3, [sD_wristPos_RT[2], sD_crossMidline_RT[2], sD_elbowPos_RT[2],
                                         sS_wristPos_RT[2], sS_midline_RT[2], sS_elbowPos_RT[2]], "946")
trace998_Pos_RT   = make_trace_line( x3, [sD_wristPos_RT[3], sD_crossMidline_RT[3], sD_elbowPos_RT[3],
                                         sS_wristPos_RT[3], sS_midline_RT[3], sS_elbowPos_RT[3]], "946")
trace1000_Pos_RT  = make_trace_line( x3, [sD_wristPos_RT[4], sD_crossMidline_RT[4], sD_elbowPos_RT[4],
                                         sS_wristPos_RT[4], sS_midline_RT[4], sS_elbowPos_RT[4]], "946")
trace1008_Pos_RT  = make_trace_line( x3, [sD_wristPos_RT[5], sD_crossMidline_RT[5], sD_elbowPos_RT[5],
                                         sS_wristPos_RT[5], sS_midline_RT[5], sS_elbowPos_RT[5]], "946")
#make trace parsing out positions 5 and 9
trace873_Pos5v9_ACC   = make_trace_bar(x2, [sD_pos5v1_ACC[0], sD_pos5v3_ACC[0], sD_pos5v9_ACC[0], sD_pos5v11_ACC[0],
                                          sD_pos9v13_ACC[0], sD_pos9v11_ACC[0], sD_pos9v5_ACC[0], sD_pos9v3_ACC[0]], "873")
trace946_Pos5v9_ACC   = make_trace_bar(x2, [sD_pos5v1_ACC[1], sD_pos5v3_ACC[1], sD_pos5v9_ACC[1], sD_pos5v11_ACC[1],
                                          sD_pos9v13_ACC[1], sD_pos9v11_ACC[1], sD_pos9v5_ACC[1], sD_pos9v3_ACC[1]], "946")
trace983_Pos5v9_ACC   = make_trace_bar(x2, [sD_pos5v1_ACC[2], sD_pos5v3_ACC[2], sD_pos5v9_ACC[2], sD_pos5v11_ACC[2],
                                          sD_pos9v13_ACC[2], sD_pos9v11_ACC[2], sD_pos9v5_ACC[2], sD_pos9v3_ACC[2]], "983")
trace998_Pos5v9_ACC   = make_trace_bar(x2, [sD_pos5v1_ACC[3], sD_pos5v3_ACC[3], sD_pos5v9_ACC[3], sD_pos5v11_ACC[3],
                                          sD_pos9v13_ACC[3], sD_pos9v11_ACC[3], sD_pos9v5_ACC[3], sD_pos9v3_ACC[3]], "998")
trace1000_Pos5v9_ACC  = make_trace_bar(x2, [sD_pos5v1_ACC[4], sD_pos5v3_ACC[4], sD_pos5v9_ACC[4], sD_pos5v11_ACC[4],
                                          sD_pos9v13_ACC[4], sD_pos9v11_ACC[4], sD_pos9v5_ACC[4], sD_pos9v3_ACC[4]], "1000")
trace1008_Pos5v9_ACC  = make_trace_bar(x2, [sD_pos5v1_ACC[5], sD_pos5v3_ACC[5], sD_pos5v9_ACC[5], sD_pos5v11_ACC[5],
                                          sD_pos9v13_ACC[5], sD_pos9v11_ACC[5], sD_pos9v5_ACC[5], sD_pos9v3_ACC[5]], "1008")

trace873_Pos5v9_RT   = make_trace_line(x2, [sD_pos5v1_RT[0], sD_pos5v3_RT[0], sD_pos5v9_RT[0], sD_pos5v11_RT[0],
                                          sD_pos9v13_RT[0], sD_pos9v11_RT[0], sD_pos9v5_RT[0], sD_pos9v3_RT[0]], "873")
trace946_Pos5v9_RT   = make_trace_line(x2, [sD_pos5v1_RT[1], sD_pos5v3_RT[1], sD_pos5v9_RT[1], sD_pos5v11_RT[1],
                                          sD_pos9v13_RT[1], sD_pos9v11_RT[1], sD_pos9v5_RT[1], sD_pos9v3_RT[1]], "946")
trace983_Pos5v9_RT   = make_trace_line(x2, [sD_pos5v1_RT[2], sD_pos5v3_RT[2], sD_pos5v9_RT[2], sD_pos5v11_RT[2],
                                          sD_pos9v13_RT[2], sD_pos9v11_RT[2], sD_pos9v5_RT[2], sD_pos9v3_RT[2]], "983")
trace998_Pos5v9_RT   = make_trace_line(x2, [sD_pos5v1_RT[3], sD_pos5v3_RT[3], sD_pos5v9_RT[3], sD_pos5v11_RT[3],
                                          sD_pos9v13_RT[3], sD_pos9v11_RT[3], sD_pos9v5_RT[3], sD_pos9v3_RT[3]], "998")
trace1000_Pos5v9_RT  = make_trace_line(x2, [sD_pos5v1_RT[4], sD_pos5v3_RT[4], sD_pos5v9_RT[4], sD_pos5v11_RT[4],
                                          sD_pos9v13_RT[4], sD_pos9v11_RT[4], sD_pos9v5_RT[4], sD_pos9v3_RT[4]], "1000")
trace1008_Pos5v9_RT  = make_trace_line(x2, [sD_pos5v1_RT[5], sD_pos5v3_RT[5], sD_pos5v9_RT[5], sD_pos5v11_RT[5],
                                          sD_pos9v13_RT[5], sD_pos9v11_RT[5], sD_pos9v5_RT[5], sD_pos9v3_RT[5]], "1008")
# matFileName = fileDirectory + filename
# dataFile = sio.savemat(matFileName, {'x':x, 'y':y, 'cp_mean': cp_mean, 'mm_mean': mm_mean, 'cb_mean': cb_mean)
# dataFile.write(x,y,cp_mean, mm_mean, cb_mean,)
# dataFile.close()


# Generate Figure object with 2 axes on 2 rows, print axis grid to stdout
fig_Pos_ACC = tls.make_subplots( rows=1, cols=1, shared_xaxes=True,)
fig_Pos_RT  = tls.make_subplots( rows=1, cols=1, shared_xaxes=True,)
fig_Pos5v9_ACC = tls.make_subplots( rows=1, cols=1, shared_xaxes=True,)
fig_Pos5v9_RT = tls.make_subplots( rows=1, cols=1, shared_xaxes=True,)
#set figure layout to hold mutlitple bars
fig_Pos_ACC['layout'].update(barmode='group', bargroupgap=0, bargap=0.25,
    title = "Accuracy by Position Group Data")

fig_Pos_RT['layout'].update(barmode='group', bargroupgap=0, bargap=0.25,
    title = "RT by Position Group Data")

fig_Pos5v9_ACC['layout'].update(barmode='group', bargroupgap=0, bargap=0.25,
    title = "Accuracy Position 5 and 9 Group Data")
fig_Pos5v9_RT['layout'].update(barmode='group', bargroupgap=0, bargap=0.25,
    title = "RT Position 5 and 9 Group Data")

fig_Pos_ACC['data']    = [trace873_Pos_ACC, trace946_Pos_ACC, trace983_Pos_ACC, trace998_Pos_ACC, trace1000_Pos_ACC, trace1008_Pos_ACC]
fig_Pos_RT['data']     = [trace873_Pos_RT, trace946_Pos_RT, trace983_Pos_RT, trace998_Pos_RT, trace1000_Pos_RT, trace1008_Pos_RT]
fig_Pos5v9_ACC['data'] = [trace873_Pos5v9_ACC, trace946_Pos5v9_ACC, trace983_Pos5v9_ACC,trace998_Pos5v9_ACC, trace1000_Pos5v9_ACC, trace1008_Pos5v9_ACC]
fig_Pos5v9_RT['data']  = [trace873_Pos5v9_RT, trace946_Pos5v9_RT, trace983_Pos5v9_RT, trace998_Pos5v9_RT, trace1000_Pos5v9_RT, trace1008_Pos5v9_RT]

# #get the url of your figure to embed in html later
# first_plot_url = py.plot(fig, filename= subjectName + "AccByMorph" + session, auto_open=False,)
# tls.get_embed(first_plot_url)

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
# </html>'''
#
# #save figure data in location specific previously
# f = open(fileDirectory + filename + '.html','w')
# f.write(html_string)

# save images as png in case prefer compared to html
py.image.save_as(fig_Pos_ACC, fileDirectory + "spatialLoc_ACC_Group.jpeg")
py.image.save_as(fig_Pos_RT, fileDirectory + "spatialLoc_RT_Group.jpeg")
py.image.save_as(fig_Pos5v9_ACC, fileDirectory + "spatialLoc5v9_ACC_Group.jpeg")
py.image.save_as(fig_Pos5v9_RT, fileDirectory + "spatialLoc5v9_RT_Group.jpeg")
#close all open files
# f.close()

print("Done!")
