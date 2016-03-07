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
filename = ('20160210_1549-MR976_block7')
fileDirectory = '/Users/courtney/GoogleDrive/Riesenhuber/05_2015_scripts/Vibrotactile/06_frequencyDiscrimination/data/976/'


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

if int(data['exptdesign']['preOrPostTrain'][0,0][0]) == 1:
    session = "Pre"
else:
    session = "post"

#############################################################################
#Calculations by Acc category type
#############################################################################

#calculate accuracy by frequency
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

FL = [frequencyList[1], frequencyList[7], frequencyList[13], frequencyList[19]]

iTrial = iBlock = 0
for iBlock in range(sResp.size):
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
    for iTrial in range(sResp[0,iBlock].size):
        stim1 = int(round(stimuli[0,iBlock][0,iTrial]))
        stim2 = int(round(stimuli[0,iBlock][2,iTrial]))

        if stim1 == stim2:
            sameAcc.append(accuracy[0,iBlock][0,iTrial])
            sameRT.append(RT[0,iBlock][0,iTrial])
        elif (stim1 == FL[3] and stim2 == FL[1]) or (stim1 == FL[3] and stim2 == FL[1]):
            m6_5Acc.append(accuracy[0,iBlock][0,iTrial])
            m6_5RT.append(RT[0,iBlock][0,iTrial])
        elif (stim1 == FL[2] and stim2 == FL[0]) or (stim1 == FL[0] and stim2 == FL[2]):
            m6_95Acc.append(accuracy[0,iBlock][0,iTrial])
            m6_95RT.append(RT[0,iBlock][0,iTrial])
        elif (stim1 == FL[3] and stim2 == FL[2]) or (stim1 == FL[2] and stim2 == FL[3]):
            m3w5Acc.append(accuracy[0,iBlock][0,iTrial])
            m3w5RT.append(RT[0,iBlock][0,iTrial])
        elif (stim1 == FL[0] and stim2 == FL[1]) or (stim1 == FL[1] and stim2 == FL[0]):
            m3w95Acc.append(accuracy[0,iBlock][0,iTrial])
            m3w95RT.append(RT[0,iBlock][0,iTrial])
        elif (stim1 == FL[1] and stim2 == FL[2]) or (stim1 == FL[2] and stim2 == FL[1]):
            m3bAcc.append(accuracy[0,iBlock][0,iTrial])
            m3bRT.append(RT[0,iBlock][0,iTrial])

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

#############################################################################
#Calculations by position
#############################################################################

#calculate the reaction time by position
iBlock = iTrial = 0
bD_pos3or4_RT = []
bD_pos5or6_RT = []
bD_pos9or10_RT = []
bD_pos11or12_RT = []
bS_pos3or4_RT = []
bS_pos5or6_RT = []
bS_pos9or10_RT = []
bS_pos11or12_RT = []

for iBlock in range(sResp.size):
    D_pos3or4_RT = []
    D_pos5or6_RT = []
    D_pos9or10_RT = []
    D_pos11or12_RT = []
    S_pos3or4_RT = []
    S_pos5or6_RT = []
    S_pos9or10_RT = []
    S_pos11or12_RT = []
    for iTrial in range(sResp[0,iBlock].size):
        pos1 = int(stimuli[0,iBlock][1,iTrial])
        pos2 = int(stimuli[0,iBlock][3,iTrial])
        stim1 = stimuli[0,iBlock][0,iTrial]
        stim2 = stimuli[0,iBlock][2,iTrial]
        if stim1 != stim2:
            if (pos1 == 3 or pos1 == 4):
                D_pos3or4_RT.append(RT[0,iBlock][0,iTrial])
            elif (pos1 == 5 or pos1 == 6):
                D_pos5or6_RT.append(RT[0,iBlock][0,iTrial])
            elif (pos1 == 9 or pos1 == 10):
                D_pos9or10_RT.append(RT[0,iBlock][0,iTrial])
            # elif pos1 == 1 or pos1 == 2:
            #     D_pos5or6_RT.append(RT[0,iBlock][0,iTrial])
            # elif pos1 == 13 or pos1 == 14:
            #     D_pos9or10_RT.append(RT[0,iBlock][0,iTrial])
            elif (pos1 == 11 or pos1 == 12):
                D_pos11or12_RT.append(RT[0,iBlock][0,iTrial])
            else:
                print("Your script is broked and stimuli are not meeting criteria for position of different stimuli")
                print(stim1, stim2)
                print(pos1, pos2)
        else:
            if (pos1 == 3 or pos1 == 4):
                S_pos3or4_RT.append(RT[0,iBlock][0,iTrial])
            elif (pos1 == 5 or pos1 == 6):
                S_pos5or6_RT.append(RT[0,iBlock][0,iTrial])
            elif (pos1 == 9 or pos1 == 10):
                S_pos9or10_RT.append(RT[0,iBlock][0,iTrial])
            # elif (pos1 == 1 or pos1 == 2):
            #      S_pos5or6_RT.append(RT[0,iBlock][0,iTrial])
            # elif (pos1 == 13 or pos1 == 14):
            #     S_pos9or10_RT.append(RT[0,iBlock][0,iTrial])
            elif (pos1 == 11 or pos1 == 12):
                S_pos11or12_RT.append(RT[0,iBlock][0,iTrial])
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

#calculate the accuracy by position
iBlock = iTrial = 0
bD_pos3or4_accuracy = []
bD_pos5or6_accuracy = []
bD_pos9or10_accuracy = []
bD_pos11or12_accuracy = []
bS_pos3or4_accuracy = []
bS_pos5or6_accuracy = []
bS_pos9or10_accuracy = []
bS_pos11or12_accuracy = []

for iBlock in range(sResp.size):
    D_pos3or4_accuracy = []
    D_pos5or6_accuracy = []
    D_pos9or10_accuracy = []
    D_pos11or12_accuracy = []
    S_pos3or4_accuracy = []
    S_pos5or6_accuracy = []
    S_pos9or10_accuracy = []
    S_pos11or12_accuracy = []
    for iTrial in range(sResp[0,iBlock].size):
        pos1 = int(stimuli[0,iBlock][1,iTrial])
        pos2 = int(stimuli[0,iBlock][3,iTrial])
        stim1 = stimuli[0,iBlock][0,iTrial]
        stim2 = stimuli[0,iBlock][2,iTrial]
        if stim1 != stim2:
            if (pos1 == 3 or pos1 == 4):
                D_pos3or4_accuracy.append(accuracy[0,iBlock][0,iTrial])
            elif (pos1 == 5 or pos1 == 6):
                D_pos5or6_accuracy.append(accuracy[0,iBlock][0,iTrial])
            elif (pos1 == 9 or pos1 == 10):
                D_pos9or10_accuracy.append(accuracy[0,iBlock][0,iTrial])
            # elif pos1 == 1 or pos1 == 2:
            #     D_pos5or6_accuracy.append(accuracy[0,iBlock][0,iTrial])
            # elif pos1 == 13 or pos1 == 14:
            #     D_pos9or10_accuracy.append(accuracy[0,iBlock][0,iTrial])
            elif (pos1 == 11 or pos1 == 12):
                D_pos11or12_accuracy.append(accuracy[0,iBlock][0,iTrial])
            else:
                print("Your script is broken and stimuli are not meeting criteria for position of different stimuli")
                print(stim1, stim2)
                print(pos1, pos2)
        else:
            if (pos1 == 3 or pos1 == 4):
                S_pos3or4_accuracy.append(accuracy[0,iBlock][0,iTrial])
            elif (pos1 == 5 or pos1 == 6):
                S_pos5or6_accuracy.append(accuracy[0,iBlock][0,iTrial])
            elif (pos1 == 9 or pos1 == 10):
                S_pos9or10_accuracy.append(accuracy[0,iBlock][0,iTrial])
            # elif pos1 == 1 or pos1 == 2:
            #     S_pos5or6_accuracy.append(accuracy[0,iBlock][0,iTrial])
            # elif pos1 == 13 or pos1 == 14:
            #     S_pos9or10_accuracy.append(accuracy[0,iBlock][0,iTrial])
            elif (pos1 == 11 or pos1 == 12):
                S_pos11or12_accuracy.append(accuracy[0,iBlock][0,iTrial])
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


#make trace containing acc and RT by position for Different Condition
trace1 = make_trace_bar(x, [stat.mean(bD_pos3or4_accuracy),stat.mean(bS_pos3or4_accuracy)],"Position 3 or 4 Acc" )
trace2 = make_trace_bar(x, [stat.mean(bD_pos5or6_accuracy),stat.mean(bS_pos5or6_accuracy)], "Position 5 or 6 Acc")
trace3 = make_trace_bar(x, [stat.mean(bD_pos9or10_accuracy),stat.mean(bS_pos9or10_accuracy)],"Position 9 or 10 Acc" )
trace4 = make_trace_bar(x, [stat.mean(bD_pos11or12_accuracy),stat.mean(bS_pos11or12_accuracy)], "Position 11 or 12 Acc")
trace5 = make_trace_line(x, [stat.mean(bD_pos3or4_RT),stat.mean(bS_pos3or4_RT)],"Position 3 or 4 RT")
trace6 = make_trace_line(x, [stat.mean(bD_pos5or6_RT), stat.mean(bS_pos5or6_RT)], "Position 5 or 6 RT")
trace7 = make_trace_line(x, [stat.mean(bD_pos9or10_RT),stat.mean(bS_pos9or10_RT)],"Position 9 or 10 RT")
trace8 = make_trace_line(x, [stat.mean(bD_pos11or12_RT), stat.mean(bS_pos11or12_RT)], "Position 11 or 12 RT")

#make trace containing acc by frequency for Same and different Condition
trace9  = make_trace_bar(x2, [stat.mean(b_sameAcc), stat.mean(b_m3bAcc), stat.mean(b_m3w5Acc),
                              stat.mean(b_m3w95Acc), stat.mean(b_m6_5Acc), stat.mean(b_m6_95Acc)], ["Acc"])
trace10 = make_trace_line(x2, [stat.mean(b_sameRT), stat.mean(b_m3bRT), stat.mean(b_m3w5RT),
                              stat.mean(b_m3w95RT), stat.mean(b_m6_5RT), stat.mean(b_m6_95RT)], ["RT"])
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
    title = subjectNumber + " Accuracy by Position across conditions " + session
)

fig2['layout'].update(
    barmode='group',
    bargroupgap=0,
    bargap=0.25,
    title = subjectNumber + " Accuracy by Frequency across conditions " + session
)

fig['data']  = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8]
fig2['data'] = [trace9, trace10]

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
py.image.save_as(fig, fileDirectory + filename + "frequencyDiscrim_pos" + session + ".jpeg")
py.image.save_as(fig2, fileDirectory + filename + "frequencyDiscrim_freq" + session + ".jpeg")
#close all open files
# f.close()

print("Done!")
