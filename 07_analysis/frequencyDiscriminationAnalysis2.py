#packages to import
import numpy as np
import scipy.io as sio
import plotly.plotly as py
import statistics as stat
import plotly.graph_objs as go
import plotly.tools as tls
from FrequencyFunction_General import Frequency_general
from PositionFunction_General import Position_general

tls.set_credentials_file(username='cs1471', api_key='9xknhmjhas')

# filename = input('Enter a filename: \n')
# fileDirectory = input('Enter the directory where you want your figure saved: /n')
# session = input('Enter the session number: \n')

#Use when debugging or manually editing
filename = ('20160307_1534-MR979_block7')
fileDirectory = '/Users/courtney/GoogleDrive/Riesenhuber/05_2015_scripts/Vibrotactile/06_frequencyDiscrimination/data/979/'

#load matfile
data = sio.loadmat(fileDirectory + filename, struct_as_record=True)

#pull relevant data from structures
RT            = [data[iBlock]['trialOutput']['RT'] for iBlock in range(len(data))]
ACC           = [data[iBlock]['trialOutput']['accuracy'] for iBlock in range(len(data))]
stimuli       = [data[iBlock]['trialOutput']['stimuli'] for iBlock in range(len(data))]
subjectNumber = [data[iBlock]['exptdesign']['number'][0,0][0] for iBlock in range(len(data))]
nBlocks       = [data[iBlock]['exptdesign']['numBlocks'][0,0][0] for iBlock in range(len(data))]

if int(data['exptdesign']['preOrPostTrain'][0,0][0]) == 1:
    session = "Pre"
else:
    session = "post"

#############################################################################
#Calculations by Acc by frequency
#############################################################################

FreqObj = Frequency_general()
FreqObj.calcAccRT(ACC, RT, stimuli, 'Block')


#############################################################################
#Calculations by Acc by position
#############################################################################

PosObj = Position_general()
PosObj.calcAccRT(ACC, RT, stimuli, 'freq', 'Block')

#############################################################################
#Calculating mean acc and RT overall
#############################################################################
#calculate the mean overall accuracy by block
O_accuracy = []
iBlock = 0
for iBlock in range(ACC.size):
    O_accuracy.append(np.mean(ACC[0,iBlock]))

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
x2 = ["Same", "62.50 v 40.00", "90.91 v 62.50", "40.00 v 27.03", "90.91 v 40.00", "62.50 v 27.03"]

#############################################################################
#Generating figures
#############################################################################

# (1.1) Define a trace-generating function (returns a Bar object)
def make_trace_bar(x, y, name):
    return go.Bar( x = x, y = y, name  = name, xaxis = 'x1', yaxis = 'y1')

# (1.1) Define a trace-generating function (returns a line object)
def make_trace_line(x, y, name):
    return go.Scatter(x = x, y = y, name = name, xaxis = 'x1', yaxis = 'y1')

#make trace containing acc and RT by position for Different Condition

trace_FG_ACC = []
trace_FG_RT = []

trace_PG_ACC_3or4   = make_trace_bar(x, [stat.mean(PosObj.ACC[0]),stat.mean(PosObj.ACC[4])], "Position 3 or 4 Acc" )
trace_PG_ACC_5or6   = make_trace_bar(x, [stat.mean(PosObj.ACC[1]),stat.mean(PosObj.ACC[5])],"Position 5 or 6 Acc" )
trace_PG_ACC_9or10  = make_trace_bar(x, [stat.mean(PosObj.ACC[2]),stat.mean(PosObj.ACC[6])],"Position 9 or 10 Acc" )
trace_PG_ACC_11or12 = make_trace_bar(x, [stat.mean(PosObj.ACC[3]),stat.mean(PosObj.ACC[7])],"Position 11 or 12 Acc" )
trace_PG_RT_3or4    = make_trace_line(x, [stat.mean(PosObj.RT[0]),stat.mean(PosObj.RT[4])],"Position 3 or 4 RT" )
trace_PG_RT_5or6    = make_trace_line(x, [stat.mean(PosObj.RT[1]),stat.mean(PosObj.RT[5])],"Position 5 or 6 RT" )
trace_PG_RT_9or10   = make_trace_line(x, [stat.mean(PosObj.RT[2]),stat.mean(PosObj.RT[6])],"Position 9 or 10 RT" )
trace_PG_RT_11or12  = make_trace_line(x, [stat.mean(PosObj.RT[3]),stat.mean(PosObj.RT[7])],"Position 11 or 12 RT" )

#make trace containing acc by frequency for Same and different Condition
for index in FreqObj.ACC:
    trace_FG_ACC.append(make_trace_bar(x2, [stat.mean(index)], "Acc"))
    trace_FG_RT.append(make_trace_line(x2, [stat.mean(index)], "RT"))

# Generate Figure object with 2 axes on 2 rows, print axis grid to stdout
fig_frequency = tls.make_subplots( rows=1, cols=1, shared_xaxes=True )
fig_position = tls.make_subplots( rows=1, cols=1, shared_xaxes=True )

#set figure layout to hold mutlitple bars
fig_frequency['layout'].update( barmode='group', bargroupgap=0, bargap=0.25,
                                title = subjectNumber + " Accuracy by Frequency across conditions " + session )

fig_position['layout'].update( barmode='group', bargroupgap=0, bargap=0.25,
                       title = subjectNumber + " Accuracy by Position across conditions " + session )

fig_frequency['data']  = [trace_FG_ACC, trace_FG_RT ]
fig_position['data'] = [trace_PG_ACC_3or4, trace_PG_ACC_5or6, trace_PG_ACC_9or10, trace_PG_ACC_11or12,
                          trace_PG_RT_3or4, trace_PG_RT_5or6, trace_PG_RT_9or10, trace_PG_RT_11or12 ]

#bread crumbs to make sure entered the correct information
print("Your graph will be saved in this directory: " + fileDirectory + "\n")
print("Your graph will be saved under: " + filename + "\n")
print("The session number you have indicated is: " + session + "\n")

# save images as png in case prefer compared to html
py.image.save_as(fig_frequency, fileDirectory + filename + "frequencyDiscrim_freq" + session + ".jpeg")
py.image.save_as(fig_position, fileDirectory + filename + "frequencyDiscrim_pos" + session + ".jpeg")

print("Done!")
