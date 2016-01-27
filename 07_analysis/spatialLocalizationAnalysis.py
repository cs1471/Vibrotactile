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
#Calculations by position
#############################################################################

#calculate the reaction time by position
iBlock = iTrial = 0
bD_wristPos_RT = []
bD_elbowPos_RT = []
bD_crossMidline_RT = []
bS_wristPos_RT = []
bS_elbowPos_RT = []
bS_midline_RT = []
for iBlock in range(sResp.size):
    D_wristPos_RT = []
    D_elbowPos_RT = []
    D_crossMidline_RT = []
    S_wristPos_RT = []
    S_elbowPos_RT = []
    S_midline_RT = []
    for iTrial in range(sResp[0,iBlock].size):
        pos1 = int(stimuli[0,iBlock][0,iTrial])
        pos2 = int(stimuli[0,iBlock][2,iTrial])
        if pos1 != pos2:
            if (pos1 == 1 or pos1 == 2 or pos1 == 3 or pos1 == 4 or pos1 == 5 or pos1 == 6)\
                    and (pos2 == 1 or pos2 == 2 or pos2 == 3 or pos2 == 4 or pos2 == 5 or pos2 == 6):
                D_wristPos_RT.append(RT[0,iBlock][0,iTrial])
            elif (pos1 == 9 or pos1 == 10 or pos1 == 11 or pos1 == 12 or pos1 == 13 or pos1 == 14)\
                    and (pos2 == 9 or pos2 == 10 or pos2 == 11 or pos2 == 12 or pos2 == 13 or pos2 == 14):
                 D_elbowPos_RT.append(RT[0,iBlock][0,iTrial])
            else:
                D_crossMidline_RT.append(RT[0,iBlock][0,iTrial])
        else:
            if pos1 == 1 or pos1 == 2 or pos1 == 3 or pos1 == 4:
                S_wristPos_RT.append(RT[0,iBlock][0,iTrial])
            elif pos1 == 5 or pos1 == 5 or pos1 == 9 or pos1 == 10:
                S_midline_RT.append(RT[0,iBlock][0,iTrial])
            else:
                S_elbowPos_RT.append(RT[0,iBlock][0,iTrial])

    bD_wristPos_RT.append(D_wristPos_RT)
    bD_elbowPos_RT.append(D_elbowPos_RT)
    bD_crossMidline_RT.append(D_crossMidline_RT)
    bS_wristPos_RT.append(S_wristPos_RT)
    bS_elbowPos_RT.append(S_elbowPos_RT)
    bS_midline_RT.append(S_midline_RT)

#calculate the mean RT by morph
D_wristPos_meanRT = []
iBlock = 0
for iBlock, rtDWP in enumerate(bD_wristPos_RT):
    if rtDWP != []:
        D_wristPos_meanRT.append(stat.mean(rtDWP))
    else:
        D_wristPos_meanRT.append(0)

#calculate the mean RT by morph
D_crossMidline_meanRT = []
iBlock = 0
for iBlock, rtDCM in enumerate(bD_crossMidline_RT):
    if rtDCM != []:
        D_crossMidline_meanRT.append(stat.mean(rtDCM))
    else:
        D_crossMidline_meanRT.append(0)

#calculate the mean RT by morph
D_elbowPos_meanRT = []
iBlock = 0
for iBlock, rtDEP in enumerate(bD_elbowPos_RT):
    if rtDEP != []:
        D_elbowPos_meanRT.append(stat.mean(rtDEP))
    else:
        D_elbowPos_meanRT.append(0)

#calculate the mean RT by morph
S_wristPos_meanRT = []
iBlock = 0
for iBlock, rtSWP in enumerate(bS_wristPos_RT):
    if rtSWP != []:
        S_wristPos_meanRT.append(stat.mean(rtSWP))
    else:
        S_wristPos_meanRT.append(0)

#calculate the mean RT by morph
S_midline_meanRT = []
iBlock = 0
for iBlock, rtSM in enumerate(bS_midline_RT):
    if rtSM != []:
        S_midline_meanRT.append(stat.mean(rtSM))
    else:
        S_midline_meanRT.append(0)

#calculate the mean RT by morph
S_elbowPos_meanRT = []
iBlock = 0
for iBlock, rtSEP in enumerate(bS_elbowPos_RT):
    if rtSEP != []:
        S_elbowPos_meanRT.append(stat.mean(rtSEP))
    else:
        S_elbowPos_meanRT.append(0)

#calculate the accuracy by position
iBlock = iTrial = 0
bD_wristPos_accuracy = []
bD_elbowPos_accuracy = []
bD_crossMidline_accuracy = []
bS_wristPos_accuracy = []
bS_elbowPos_accuracy = []
bS_midline_accuracy = []
for iBlock in range(sResp.size):
    D_wristPos_accuracy = []
    D_elbowPos_accuracy = []
    D_crossMidline_accuracy = []
    S_wristPos_accuracy = []
    S_elbowPos_accuracy = []
    S_midline_accuracy = []
    for iTrial in range(sResp[0,iBlock].size):
        pos1 = int(stimuli[0,iBlock][0,iTrial])
        pos2 = int(stimuli[0,iBlock][2,iTrial])
        if pos1 != pos2:
            if (pos1 == 1 or pos1 == 2 or pos1 == 3 or pos1 == 4 or pos1 == 5 or pos1 == 6)\
                    and (pos2 == 1 or pos2 == 2 or pos2 == 3 or pos2 == 4 or pos2 == 5 or pos2 == 6):
                D_wristPos_accuracy.append(accuracy[0,iBlock][0,iTrial])
            elif (pos1 == 9 or pos1 == 10 or pos1 == 11 or pos1 == 12 or pos1 == 13 or pos1 == 14)\
                    and (pos2 == 9 or pos2 == 10 or pos2 == 11 or pos2 == 12 or pos2 == 13 or pos2 == 14):
                D_elbowPos_accuracy.append(accuracy[0,iBlock][0,iTrial])
            else:
                D_crossMidline_accuracy.append(accuracy[0,iBlock][0,iTrial])
        else:
            if pos1 == 1 or pos1 == 2 or pos1 == 3 or pos1 == 4:
                S_wristPos_accuracy.append(accuracy[0,iBlock][0,iTrial])
            elif pos1 == 5 or pos1 == 6 or pos1 == 9 or pos1 == 10:
                S_midline_accuracy.append(accuracy[0,iBlock][0,iTrial])
            else:
                S_elbowPos_accuracy.append(accuracy[0,iBlock][0,iTrial])

    bD_wristPos_accuracy.append(D_wristPos_accuracy)
    bD_elbowPos_accuracy.append(D_elbowPos_accuracy)
    bD_crossMidline_accuracy.append(D_crossMidline_accuracy)
    bS_wristPos_accuracy.append(S_wristPos_accuracy)
    bS_elbowPos_accuracy.append(S_elbowPos_accuracy)
    bS_midline_accuracy.append(S_midline_accuracy)

#calculate the mean accuracy by morph
D_wristPos_meanAcc = []
iBlock = 0
for iBlock, accDWP in enumerate(bD_wristPos_accuracy):
    if accDWP != []:
        D_wristPos_meanAcc.append(stat.mean(accDWP))
    else:
        D_wristPos_meanAcc.append(0)

#calculate the mean accuracy by morph
D_crossMidline_meanAcc = []
iBlock = 0
for iBlock, accDCM in enumerate(bD_crossMidline_accuracy):
    if accDCM != []:
        D_crossMidline_meanAcc.append(stat.mean(accDCM))
    else:
        D_crossMidline_meanAcc.append(0)

#calculate the mean accuracy by morph
D_elbowPos_meanAcc = []
iBlock = 0
for iBlock, accDEP in enumerate(bD_elbowPos_accuracy):
    if accDEP != []:
        D_elbowPos_meanAcc.append(stat.mean(accDEP))
    else:
        D_elbowPos_meanAcc.append(0)

#calculate the mean accuracy by morph
S_wristPos_meanAcc = []
iBlock = 0
for iBlock, accSWP in enumerate(bS_wristPos_accuracy):
    if accSWP != []:
        S_wristPos_meanAcc.append(stat.mean(accSWP))
    else:
        S_wristPos_meanAcc.append(0)

#calculate the mean accuracy by morph
S_midline_meanAcc = []
iBlock = 0
for iBlock, accSM in enumerate(bS_midline_accuracy):
    if accSM != []:
        S_midline_meanAcc.append(stat.mean(accSM))
    else:
        S_midline_meanAcc.append(0)

#calculate the mean accuracy by morph
S_elbowPos_meanAcc = []
iBlock = 0
for iBlock, accSEP in enumerate(bS_elbowPos_accuracy):
    if accSEP != []:
        S_elbowPos_meanAcc.append(stat.mean(accSEP))
    else:
        S_elbowPos_meanAcc.append(0)

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

#############################################################################
#Generating figures
#############################################################################

# (1.1) Define a trace-generating function (returns a Bar object)
def make_trace_bar(y, name):
    return go.Bar(
        x     = x,
        y     = y,            # take in the y-coords
        name  = name,      # label for hover
        xaxis = 'x1',                    # (!) both subplots on same x-axis
        yaxis = 'y1'
    )

# (1.1) Define a trace-generating function (returns a line object)
def make_trace_line(y, name):
    return go.Scatter(
        x     = x,
        y     = y,            # take in the y-coords
        name  = name,      # label for hover
        xaxis = 'x1',                    # (!) both subplots on same x-axis
        yaxis = 'y1'
    )


#make trace containing acc and RT by position for Different Condition
trace1 = make_trace_bar([stat.mean(D_wristPos_meanAcc),stat.mean(S_wristPos_meanAcc)],"Wrist Accuracy" )
trace2 = make_trace_bar([stat.mean(D_crossMidline_meanAcc), stat.mean(S_midline_meanAcc)],"Across Mid Accuracy")
trace3 = make_trace_bar([stat.mean(D_elbowPos_meanAcc),stat.mean(S_elbowPos_meanAcc)], "Elbow Accuracy")
trace4 = make_trace_line([stat.mean(D_wristPos_meanRT),stat.mean(S_wristPos_meanRT)],"Wrist RT")
trace5 = make_trace_line([stat.mean(D_crossMidline_meanRT), stat.mean(S_midline_meanRT)], "Across Mid RT")
trace6 = make_trace_line([stat.mean(D_elbowPos_meanRT), stat.mean(S_elbowPos_meanRT)], "Elbow RT")



# matFileName = fileDirectory + filename
# dataFile = sio.savemat(matFileName, {'x':x, 'y':y, 'cp_mean': cp_mean, 'mm_mean': mm_mean, 'cb_mean': cb_mean)
# dataFile.write(x,y,cp_mean, mm_mean, cb_mean,)
# dataFile.close()


# Generate Figure object with 2 axes on 2 rows, print axis grid to stdout
fig = tls.make_subplots(
    rows=1,
    cols=1,
    shared_xaxes=True,
)

#set figure layout to hold mutlitple bars
fig['layout'].update(
    barmode='group',
    bargroupgap=0,
    bargap=0.25,
    title = subjectNumber + " Accuracy by Position Same v Different " + session
)

fig['data']  = [trace1, trace2, trace3, trace4, trace5, trace6]

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

#close all open files
# f.close()

print("Done!")
