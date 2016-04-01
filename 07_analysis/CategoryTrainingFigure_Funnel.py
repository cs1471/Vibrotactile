#packages to import
import numpy as np
import scipy.io as sio
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
from frequencyFunction_specific import FrequencySpecific
from category import category

tls.set_credentials_file(username='cs1471', api_key='9xknhmjhas')

#Use when debugging or manually editing
filename      = ('20160317_0940-MR1011_block3')
fileDirectory = '/Users/courtney/GoogleDrive/Riesenhuber/05_2015_scripts/Vibrotactile/01_CategoryTraining/data/1011/'
session       = '4'

#load matfile
data = sio.loadmat(fileDirectory + filename, struct_as_record=True)

#pull relevant data from structures
reactionTime    = data['trialOutput']['RT']
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

FS = FrequencySpecific(stimuli=stimuli)
mF, countTotal = FS.frequencyPair_parse(accuracy)

#############################################################################
#Calculations by morph
#############################################################################

catObj = category(stimuli= stimuli)
RT,ACC = catObj.wrapper(accuracy, reactionTime)

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
for iBlock in range(reactionTime.size):
    O_reactionTime.append(np.mean(reactionTime[0,iBlock]))

#x-axis label
x = []
i=0
for i in range(nBlocks):
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
        xaxis = 'x1',
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
x2 = ['[25,100]', '[27,91]', '[29,91]', '[31,83]', '[33,77]', '[36,71]', '[38,67]', '[40,62.5]', '[43,59]',
      '[59, 43]', '[62.5, 40]', '[67, 38]', '[71, 36]','[77, 33]', '[83, 31]', '[91, 29]', '[91, 27]','[100, 25]']

trace_ACC_FP = make_trace_bar(x2, mF, '')

#, ACC[9], ACC[12], ACC[15]
#, ACC[10], ACC[13], ACC[16]
#, ACC[11], ACC[14], ACC[17]
#, RT[9], RT[12], RT[15]
#, RT[10], RT[13], RT[16]
#, RT[11], RT[14], RT[17]
#make trace containing acc and RT for morph
trace1 = make_trace_bar(x, [ACC[0], ACC[3], ACC[6]],  "Category Prototype Acc")
trace2 = make_trace_bar(x, [ACC[1], ACC[4], ACC[7]], "Middle Morph Acc")
trace3 = make_trace_bar(x, [ACC[2], ACC[5], ACC[8]], "Category Boundary Acc")
trace4 = make_trace_line([RT[0], RT[3], RT[6]], "Category Prototype RT", 'n')
trace5 = make_trace_line([RT[1], RT[4], RT[7]], "Middle Morph RT", 'n')
trace6 = make_trace_line([RT[2], RT[5], RT[8]], "Category Boundary RT", 'n')

#make trace containing overall acc and rt
trace7 = make_trace_line(O_accuracy, "Overall Accuracy", 'y')
trace8 = make_trace_line(O_reactionTime, "Overall RT", 'y')

# Generate Figure object with 2 axes on 2 rows, print axis grid to stdout
fig  = tls.make_subplots(rows=1, cols=1, shared_xaxes=True)
fig_FP = tls.make_subplots(rows=1, cols=1, shared_xaxes=True)

#set figure layout to hold mutlitple bars
fig['layout'].update(barmode='group', bargroupgap=0, bargap=0.25,
    title = subjectName + " Accuracy and RT By Morph Session " + session, yaxis = dict(dtick = .1))

xZip = x2[:len(x2)]
yZip = countTotal

fig_FP['layout'].update(barmode='group', bargroupgap=0, bargap=0.25,
    title = subjectName + " Accuracy By Frequency Pair, Session " + session,  yaxis = dict(dtick = .1),
    annotations = [dict(x = xZip[i], y = mF[i], text=yZip[i], xanchor='center', yanchor='bottom', showarrow=False) for i in range(len(xZip))])

colorRA = ['black', 'blue', 'black', 'black', 'black', 'black', 'black' ,'blue', 'black',
           'black', 'blue', 'black', 'black', 'black', 'black', 'black' ,'blue', 'black']

fig['data']  = [trace1, trace2, trace3, trace7, trace4, trace5, trace6, trace8]
fig_FP['data'] = [go.Bar(x=x2, y=mF, marker = dict(color = colorRA))]
#bread crumbs to make sure entered the correct information
print("Your graph will be saved in this directory: " + fileDirectory + "\n")
print("Your graph will be saved under: " + filename + "\n")
print("The session number you have indicated is: " + session + "\n")

#save images as png in case prefer compared to html
py.image.save_as(fig, fileDirectory + filename + "_CategTrainingMorphAccSession" + session + ".jpeg")
py.image.save_as(fig_FP, fileDirectory + filename + "_FP_AccSession" + session + ".jpeg")

print("Done!")
