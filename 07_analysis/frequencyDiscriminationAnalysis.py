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
filename = ('20151120_1522-998_block5')
fileDirectory = '/Users/courtneysprouse/GoogleDrive/Riesenhuber/05_2015_scripts/Vibrotactile/06_frequencyDiscrimination/data/998/'


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
#Calculations by Acc category type
#############################################################################

#calculate accuracy by frequency
b_m0Acc = []
b_m3wAcc = []
b_m3bAcc = []
b_m6Acc = []
b_m10Acc = []

FL = [frequencyList[1], frequencyList[7], frequencyList[13], frequencyList[19]]

iTrial = iBlock = 0
for iBlock in range(sResp.size):
    m0Acc = []
    m3wAcc = []
    m3bAcc = []
    m6Acc = []
    m10Acc = []
    for iTrial in range(sResp[0,iBlock].size):
        stim1 = int(round(stimuli[0,iBlock][0,iTrial]))
        stim2 = int(round(stimuli[0,iBlock][2,iTrial]))

        if stim1 == stim2:
            m0Acc.append(accuracy[0,iBlock][0,iTrial])
        elif (stim1 == FL[0] and stim2 == FL[3]) or (stim1 == FL[3] and stim2 == FL[0]):
            m10Acc.append(accuracy[0,iBlock][0,iTrial])
        elif (stim1 == FL[0] and stim2 == FL[2]) or (stim1 == FL[2] and stim2 == FL[0]) or\
                (stim1 == FL[3] and stim2 == FL[1]) or (stim1 == FL[1] and stim2 == FL[3]):
            m6Acc.append(accuracy[0,iBlock][0,iTrial])
        elif (stim1 == FL[0] and stim2 == FL[1]) or (stim1 == FL[1] and stim2 == FL[0]) or\
                (stim1 == FL[3] and stim2 == FL[2]) or (stim1 == FL[2] and stim2 == FL[3]):
            m3wAcc.append(accuracy[0,iBlock][0,iTrial])
        elif (stim1 == FL[1] and stim2 == FL[2]) or (stim1 == FL[2] and stim2 == FL[1]):
            m3bAcc.append(accuracy[0,iBlock][0,iTrial])

    b_m0Acc.append(m0Acc)
    b_m3wAcc.append(m3wAcc)
    b_m3bAcc.append(m3bAcc)
    b_m6Acc.append(m6Acc)
    b_m10Acc.append(m10Acc)

#calculate accuracy for m0 condition
i = 0
mAcc_m0 = []
for i in range(len(b_m0Acc)):
    mAcc_m0.append(stat.mean(b_m0Acc[i]))

#calculate accuracy by m3w condition
i = 0
mAcc_m3w = []
for i in range(len(b_m3wAcc)):
    mAcc_m3w.append(stat.mean(b_m3wAcc[i]))

#calculate accuracy by m3b condition
i = 0
mAcc_m3b = []
for i in range(len(b_m3bAcc)):
    mAcc_m3b.append(stat.mean(b_m3bAcc[i]))

#calculate accuracy by m6 condition
i = 0
mAcc_m6 = []
for i in range(len(b_m6Acc)):
    mAcc_m6.append(stat.mean(b_m6Acc[i]))

#calculate accuracy by m10 condition
i = 0
mAcc_m10 = []
for i in range(len(b_m10Acc)):
    mAcc_m10.append(stat.mean(b_m10Acc[i]))

############################################################################
#Calculations by Acc category RT
#############################################################################
#calculate accuracy by frequency
b_m0RT = []
b_m3wRT = []
b_m3bRT = []
b_m6RT = []
b_m10RT = []

iTrial = iBlock = 0
for iBlock in range(sResp.size):
    m0RT = []
    m3wRT = []
    m3bRT = []
    m6RT = []
    m10RT = []
    for iTrial in range(sResp[0,iBlock].size):
        stim1 = int(round(stimuli[0,iBlock][0,iTrial]))
        stim2 = int(round(stimuli[0,iBlock][2,iTrial]))

        if stim1 == stim2:
            m0RT.append(RT[0,iBlock][0,iTrial])
        elif (stim1 == FL[0] and stim2 == FL[3]) or (stim1 == FL[3] and stim2 == FL[0]):
            m10RT.append(RT[0,iBlock][0,iTrial])
        elif (stim1 == FL[0] and stim2 == FL[2]) or (stim1 == FL[2] and stim2 == FL[0]) or\
                (stim1 == FL[3] and stim2 == FL[1]) or (stim1 == FL[1] and stim2 == FL[3]):
            m6RT.append(RT[0,iBlock][0,iTrial])
        elif (stim1 == FL[0] and stim2 == FL[1]) or (stim1 == FL[1] and stim2 == FL[0]) or\
                (stim1 == FL[3] and stim2 == FL[2]) or (stim1 == FL[2] and stim2 == FL[3]):
            m3wRT.append(RT[0,iBlock][0,iTrial])
        elif (stim1 == FL[1] and stim2 == FL[2]) or (stim1 == FL[2] and stim2 == FL[1]):
            m3bRT.append(RT[0,iBlock][0,iTrial])

    b_m0RT.append(m0RT)
    b_m3wRT.append(m3wRT)
    b_m3bRT.append(m3bRT)
    b_m6RT.append(m6RT)
    b_m10RT.append(m10RT)

#calculate accuracy for m0 condition
i = 0
mRT_m0 = []
for i in range(len(b_m0RT)):
    mRT_m0.append(stat.mean(b_m0RT[i]))

#calculate accuracy by m3w condition
i = 0
mRT_m3w = []
for i in range(len(b_m3wRT)):
    mRT_m3w.append(stat.mean(b_m3wRT[i]))

#calculate accuracy by m3w condition
i = 0
mRT_m3b = []
for i in range(len(b_m3bRT)):
    mRT_m3b.append(stat.mean(b_m3bRT[i]))

#calculate accuracy by m3w condition
i = 0
mRT_m6 = []
for i in range(len(b_m6RT)):
    mRT_m6.append(stat.mean(b_m6RT[i]))

#calculate accuracy by m3w condition
i = 0
mRT_m10 = []
for i in range(len(b_m10RT)):
    mRT_m10.append(stat.mean(b_m10RT[i]))

#############################################################################
#Calculations by position
#############################################################################

#calculate the reaction time by position
iBlock = iTrial = 0
bD_wristPos_RT = []
bD_elbowPos_RT = []
bS_wristPos_RT = []
bS_elbowPos_RT = []

for iBlock in range(sResp.size):
    D_wristPos_RT = []
    D_elbowPos_RT = []
    S_wristPos_RT = []
    S_elbowPos_RT = []
    for iTrial in range(sResp[0,iBlock].size):
        pos1 = int(stimuli[0,iBlock][1,iTrial])
        pos2 = int(stimuli[0,iBlock][3,iTrial])
        stim1 = stimuli[0,iBlock][0,iTrial]
        stim2 = stimuli[0,iBlock][2,iTrial]
        if stim1 != stim2:
            if (pos1 == 1 or pos1 == 2 or pos1 == 3 or pos1 == 4):
                D_wristPos_RT.append(RT[0,iBlock][0,iTrial])
            else:
                 D_elbowPos_RT.append(RT[0,iBlock][0,iTrial])
        else:
            if pos1 == 1 or pos1 == 2 or pos1 == 3 or pos1 == 4:
                S_wristPos_RT.append(RT[0,iBlock][0,iTrial])
            else:
                S_elbowPos_RT.append(RT[0,iBlock][0,iTrial])

    bD_wristPos_RT.append(D_wristPos_RT)
    bD_elbowPos_RT.append(D_elbowPos_RT)
    bS_wristPos_RT.append(S_wristPos_RT)
    bS_elbowPos_RT.append(S_elbowPos_RT)

#calculate the mean RT by morph
D_wristPos_meanRT = []
iBlock = 0
for iBlock, rtDWP in enumerate(bD_wristPos_RT):
    if rtDWP != []:
        D_wristPos_meanRT.append(stat.mean(rtDWP))
    else:
        D_wristPos_meanRT.append(0)

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
bS_wristPos_accuracy = []
bS_elbowPos_accuracy = []

for iBlock in range(sResp.size):
    D_wristPos_accuracy = []
    D_elbowPos_accuracy = []
    S_wristPos_accuracy = []
    S_elbowPos_accuracy = []
    for iTrial in range(sResp[0,iBlock].size):
        pos1 = int(stimuli[0,iBlock][1,iTrial])
        pos2 = int(stimuli[0,iBlock][3,iTrial])
        stim1 = stimuli[0,iBlock][0,iTrial]
        stim2 = stimuli[0,iBlock][2,iTrial]
        if stim1 != stim2:
            if (pos1 == 1 or pos1 == 2 or pos1 == 3 or pos1 == 4):
                D_wristPos_accuracy.append(accuracy[0,iBlock][0,iTrial])
            else:
                D_elbowPos_accuracy.append(accuracy[0,iBlock][0,iTrial])
        else:
            if (pos1 == 1 or pos1 == 2 or pos1 == 3 or pos1 == 4):
                S_wristPos_accuracy.append(accuracy[0,iBlock][0,iTrial])
            else:
                S_elbowPos_accuracy.append(accuracy[0,iBlock][0,iTrial])

    bD_wristPos_accuracy.append(D_wristPos_accuracy)
    bD_elbowPos_accuracy.append(D_elbowPos_accuracy)
    bS_wristPos_accuracy.append(S_wristPos_accuracy)
    bS_elbowPos_accuracy.append(S_elbowPos_accuracy)

#calculate the mean accuracy by morph
D_wristPos_meanAcc = []
iBlock = 0
for iBlock, accDWP in enumerate(bD_wristPos_accuracy):
    if accDWP != []:
        D_wristPos_meanAcc.append(stat.mean(accDWP))
    else:
        D_wristPos_meanAcc.append(0)

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
x2 = ["M0", "M3B", "M3W", "M6", "M10"]

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
trace1 = make_trace_bar(x, [stat.mean(D_wristPos_meanAcc),stat.mean(S_wristPos_meanAcc)],"Wrist Accuracy" )
trace2 = make_trace_bar(x, [stat.mean(D_elbowPos_meanAcc),stat.mean(S_elbowPos_meanAcc)], "Elbow Accuracy")
trace3 = make_trace_line(x, [stat.mean(D_wristPos_meanRT),stat.mean(S_wristPos_meanRT)],"Wrist RT")
trace4 = make_trace_line(x, [stat.mean(D_elbowPos_meanRT), stat.mean(S_elbowPos_meanRT)], "Elbow RT")

#make trace containing acc by frequency for Same and different Condition
trace5  = make_trace_bar(x2, [stat.mean(mAcc_m0), stat.mean(mAcc_m3b), stat.mean(mAcc_m3w),
                              stat.mean(mAcc_m6), stat.mean(mAcc_m10)], ["M0","M3B", "M3W", "M6", "M10"])
trace6 = make_trace_line(x2, [stat.mean(mRT_m0), stat.mean(mRT_m3b), stat.mean(mRT_m3w),
                             stat.mean(mRT_m6), stat.mean(mRT_m10)], ["M0","M3B", "M3W", "M6", "M10"])
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

fig2 = tls.make_subplots(
    rows=1,
    cols=1,
    shared_xaxes=True,
)

#set figure layout to hold mutlitple bars
fig['layout'].update(
    barmode='group',
    bargroupgap=0,
    bargap=0.25,
    title = subjectNumber + " Accuracy by Frequency across conditions " + session
)

fig2['layout'].update(
    barmode='group',
    bargroupgap=0,
    bargap=0.25,
    title = subjectNumber + " Accuracy by Position across conditions " + session
)

fig['data']  = [trace1, trace2, trace3, trace4]
fig2['data'] = [trace5, trace6]

#get the url of your figure to embed in html later
# first_plot_url = py.plot(fig, filename= subjectName + "AccByMorph" + session, auto_open=False,)
# tls.get_embed(first_plot_url)
# second_plot_url = py.plot(fig2, filename= subjectName + "RTbyMorph" + session, auto_open=False,)
# tls.get_embed(second_plot_url)
# third_plot_url = py.plot(fig3, filename= subjectName + "AccByCatgeory" + session, auto_open=False,)
# tls.get_embed(third_plot_url)

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
py.image.save_as(fig, fileDirectory + filename + "frequencyDiscrim_pos" + session + ".png")
py.image.save_as(fig2, fileDirectory + filename + "frequencyDiscrim_freq" + session + ".png")
#close all open files
# f.close()

print("Done!")
