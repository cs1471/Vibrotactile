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
filename = ('20160131_1455-MR983_block6')
fileDirectory = '/Users/courtney/GoogleDrive/Riesenhuber/05_2015_scripts/Vibrotactile/01_CategoryTraining/data/983/'
session = '3'

#load matfile
data = sio.loadmat(fileDirectory + filename, struct_as_record=True)

#make list of frequencies tested
frequencyList = makeFrequency()

#pull relevant data from structures
RT = data['trialOutput']['RT']
sResp = data['trialOutput']['sResp']
correctResponse = data['trialOutput']['correctResponse']
accuracy = data['trialOutput']['accuracy']
level = data['trialOutput']['level']
stimuli = data['trialOutput']['stimuli']
nTrials = data['exptdesign']['numTrialsPerSession'][0,0][0]
nBlocks = data['exptdesign']['numSessions'][0,0][0]
subjectNumber = data['exptdesign']['number'][0,0][0]
subjectName = data['exptdesign']['subjectName'][0,0][0]


#############################################################################
#Calculations by category type
#############################################################################

#calculate accuracy by category type
b_categoryA = []
b_categoryB = []
i = counter = 0
for i in range(sResp.size):
    categoryA = []
    categoryB = []
    for counter in range(sResp[0,i].size):
        stimulus = round(stimuli[0,i][0,counter])
        if accuracy[0,i][0,counter]==1:
            if stimulus in frequencyList and stimulus < 47:
                categoryA.append(1)
            else:
                categoryB.append(1)
        else:
            if stimulus in frequencyList and stimulus < 47:
                categoryA.append(0)
            else:
                categoryB.append(0)
    b_categoryA.append(categoryA)
    b_categoryB.append(categoryB)

#calculate accuracy by block for category A
i = 0
mAcc_categoryA = []
for i in range(len(b_categoryA)):
    mAcc_categoryA.append(stat.mean(b_categoryA[i]))

#calculate accuracy by block for category B
i = 0
mAcc_categoryB = []
for i in range(len(b_categoryB)):
    mAcc_categoryB.append(stat.mean(b_categoryB[i]))

#calculate reaction time by category type
b_categoryA_RT = []
b_categoryB_RT = []
iTrial = iBLock = 0
for iBlock in range(sResp.size):
    categoryA_RT = []
    categoryB_RT = []
    for iTrial in range(len(RT[0,iBlock][0])):
        stimulus = round(stimuli[0,iBlock][0,iTrial])
        if stimulus in frequencyList and stimulus < 47:
            categoryA_RT.append(RT[0,iBlock][0,iTrial])
        else:
            categoryB_RT.append(RT[0,iBlock][0,iTrial])
    b_categoryA_RT.append(categoryA_RT)
    b_categoryB_RT.append(categoryB_RT)

#calculate RT by block for category A
iBlock = 0
mRT_categoryA = []
for iBlock, time in enumerate(b_categoryA_RT):
        mRT_categoryA.append(stat.mean(time))

#calculate RT by block for category B
iBlock = 0
mRT_categoryB = []
for iBlock, time in enumerate(b_categoryB_RT):
    mRT_categoryB.append(stat.mean(time))

#############################################################################
#Calculations by morph
#############################################################################

#calculate the accuracy by morph
iBlock = iTrial = 0
b_catProto_accuracy = []
b_middleM_accuracy = []
b_catBound_accuracy = []
for iBlock in range(sResp.size):
    catProto_accuracy = []
    middleM_accuracy = []
    catBound_accuracy = []
    for iTrial in range(sResp[0,iBlock].size):
        stimulus = round(stimuli[0,iBlock][0,iTrial])
        if accuracy[0,iBlock][0,iTrial]==1:
            if stimulus == frequencyList[0] or stimulus == frequencyList[1] or stimulus == frequencyList[2]:
                catProto_accuracy.append(1)
            elif stimulus == frequencyList[19] or stimulus == frequencyList[18] or stimulus == frequencyList[17]:
                catProto_accuracy.append(1)
            elif stimulus == frequencyList[3] or stimulus == frequencyList[4] or stimulus == frequencyList[5]:
                middleM_accuracy.append(1)
            elif stimulus == frequencyList[16] or stimulus == frequencyList[15] or stimulus == frequencyList[14]:
                middleM_accuracy.append(1)
            elif stimulus == frequencyList[6] or stimulus == frequencyList[7] or stimulus == frequencyList[8]:
                catBound_accuracy.append(1)
            elif stimulus == frequencyList[13] or stimulus == frequencyList[12] or stimulus == frequencyList[11]:
                catBound_accuracy.append(1)
        else:
            if stimulus == frequencyList[0] or stimulus == frequencyList[1] or stimulus == frequencyList[2]:
                catProto_accuracy.append(0)
            elif stimulus == frequencyList[19] or stimulus == frequencyList[18] or stimulus == frequencyList[17]:
                catProto_accuracy.append(0)
            elif stimulus == frequencyList[3] or stimulus == frequencyList[4] or stimulus == frequencyList[5]:
                middleM_accuracy.append(0)
            elif stimulus == frequencyList[16] or stimulus == frequencyList[15] or stimulus == frequencyList[14]:
                middleM_accuracy.append(0)
            elif stimulus == frequencyList[6] or stimulus == frequencyList[7] or stimulus == frequencyList[8]:
                catBound_accuracy.append(0)
            elif stimulus == frequencyList[13] or stimulus == frequencyList[12] or stimulus == frequencyList[11]:
                catBound_accuracy.append(0)
    b_catProto_accuracy.append(catProto_accuracy)
    b_catBound_accuracy.append(catBound_accuracy)
    b_middleM_accuracy.append(middleM_accuracy)

#calculate the mean accuracy by morph
cp_meanAcc = []
iBlock = 0
for iBlock, accCP in enumerate(b_catProto_accuracy):
    if accCP != []:
        cp_meanAcc.append(stat.mean(accCP))
    else:
        cp_meanAcc.append(0)

#calculate the mean accuracy by morph
mm_meanAcc = []
iBlock = 0
for iBlock, accMM in enumerate(b_middleM_accuracy):
    if accMM != []:
        mm_meanAcc.append(stat.mean(accMM))
    else:
        mm_meanAcc.append(0)

#calculate the mean accuracy by morph
cb_meanAcc = []
iBlock = 0
for iBlock, accCB in enumerate(b_catBound_accuracy):
    if accCB != []:
        cb_meanAcc.append(stat.mean(accCB))
    else:
        cb_meanAcc.append(0)

#calculate the reaction time by morph
iBlock = iTrial = 0
b_catProto_RT = []
b_middleM_RT = []
b_catBound_RT = []
for iBlock in range(sResp.size):
    catProto_RT = []
    middleM_RT = []
    catBound_RT = []
    for iTrial in range(len(RT[0,iBlock][0])):
        stimulus = round(stimuli[0,iBlock][0,iTrial])
        if stimulus == frequencyList[0] or stimulus == frequencyList[1] or stimulus == frequencyList[2]:
            catProto_RT.append(RT[0,iBlock][0,iTrial])
        elif stimulus == frequencyList[19] or stimulus == frequencyList[18] or stimulus == frequencyList[17]:
            catProto_RT.append(RT[0,iBlock][0,iTrial])
        elif stimulus == frequencyList[3] or stimulus == frequencyList[4] or stimulus == frequencyList[5]:
            middleM_RT.append(RT[0,iBlock][0,iTrial])
        elif stimulus == frequencyList[16] or stimulus == frequencyList[15] or stimulus == frequencyList[14]:
            middleM_RT.append(RT[0,iBlock][0,iTrial])
        elif stimulus == frequencyList[6] or stimulus == frequencyList[7] or stimulus == frequencyList[8]:
            catBound_RT.append(RT[0,iBlock][0,iTrial])
        elif stimulus == frequencyList[13] or stimulus == frequencyList[12] or stimulus == frequencyList[11]:
            catBound_RT.append(RT[0,iBlock][0,iTrial])
    b_catProto_RT.append(catProto_RT)
    b_catBound_RT.append(catBound_RT)
    b_middleM_RT.append(middleM_RT)

#calculate the mean RT by morph
cp_meanRT=[]
iBlock = 0
for iBlock,timeCP in enumerate(b_catProto_RT):
    if timeCP != []:
        cp_meanRT.append(stat.mean(timeCP))
    else:
        cp_meanRT.append(0)

#calculate the mean RT by morph
mm_meanRT=[]
iBlock = 0
for iBlock,timeMM in enumerate(b_middleM_RT):
    if timeMM != []:
        mm_meanRT.append(stat.mean(timeMM))
    else:
        mm_meanRT.append(0)

#calculate the mean RT by morph
cb_meanRT = []
iBlock = 0
for iBlock, timeCB in enumerate(b_catBound_RT):
    if timeCB != []:
        cb_meanRT.append(stat.mean(timeCB))
    else:
        cb_meanRT.append(0)

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
for i in range(nBlocks):
            x.append("Block: " + str(i+1) + ", Level: " + str(level[0,i][0,0])),

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


#make trace containing acc and RT for morph
trace1 = make_trace_bar(cp_meanAcc,  "Category Prototype Acc")
trace2 = make_trace_bar(mm_meanAcc, "Middle Morph Acc")
trace3 = make_trace_bar(cb_meanAcc, "Category Boundary Acc")
trace4 = make_trace_line(cp_meanRT, "Category Prototype RT", 'n')
trace5 = make_trace_line(mm_meanRT, "Middle Morph RT", 'n')
trace6 = make_trace_line(cb_meanRT, "Category Boundary RT", 'n')

#make trace containing overall acc and rt
trace7 = make_trace_line(O_accuracy, "Overall Accuracy", 'y')
trace8 = make_trace_line(O_reactionTime, "Overall RT", 'y')

#make trace containing acc and RT for category type
trace9 = make_trace_bar(mAcc_categoryA, 'Category A Acc (LF prox to wrist)')
trace10 = make_trace_bar(mAcc_categoryB, 'Category B Acc (HF prox to wrist)')
trace11 = make_trace_line(mRT_categoryA, 'Category A RT (LF prox to wrist)', 'n')
trace12 = make_trace_line(mRT_categoryB, 'Category B RT (HF prox to wrist)', 'n')

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
    title = subjectNumber + "Accuracy and RT By Morph_Session" + session
)

fig2['layout'].update(
    barmode='group',
    bargroupgap=0,
    bargap=0.25,
    title = subjectNumber + "Accuracy and RT By Category_Session" + session
)


fig['data']  = [trace1, trace2, trace3, trace7, trace4, trace5, trace6, trace8]
fig2['data'] = [trace9, trace10, trace7, trace11, trace12, trace8]

#get the url of your figure to embed in html later
# first_plot_url = py.plot(fig, filename= subjectName + "AccByMorph" + session, auto_open=False,)
# tls.get_embed(first_plot_url)
# second_plot_url = py.plot(fig2, filename= subjectName + "RTbyMorph" + session, auto_open=False,)
# tls.get_embed(second_plot_url)

#bread crumbs to make sure entered the correct information
print("Your graph will be saved in this directory: " + fileDirectory + "\n")
print("Your graph will be saved under: " + filename + "\n")
print("The session number you have indicated is: " + session + "\n")


#embed figure data in html
# html_string = '''
# <html>
#     <head>
#         <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
#         <style>body{ margin:0 100; background:whitesmoke; }</style>
#     </head>
#     <body>
#         <!-- *** Accuracy by Morph *** --->
#         <iframe width="1000" height="550" frameborder="0" seamless="seamless" scrolling="no" \
# src="'''+ first_plot_url + '''.embed?width=800&height=550"></iframe>
#         <!-- *** Accuracy by Morph *** --->
#         <iframe width="1000" height="550" frameborder="0" seamless="seamless" scrolling="no" \
# src="'''+ second_plot_url + '''.embed?width=800&height=550"></iframe>
#         <!-- *** Accuracy by Morph *** --->
#         <iframe width="1000" height="550" frameborder="0" seamless="seamless" scrolling="no" \
# src="'''+ third_plot_url + '''.embed?width=800&height=550"></iframe>
#         <!-- *** Accuracy by Morph *** --->
#         <iframe width="1000" height="550" frameborder="0" seamless="seamless" scrolling="no" \
# src="'''+ fourth_plot_url + '''.embed?width=800&height=550"></iframe>
#     </body>
# </html>'''
#
# #save figure data in location specific previously
# f = open(fileDirectory + filename + '.html','w')
# f.write(html_string)

#save images as png in case prefer compared to html
py.image.save_as(fig, fileDirectory + filename + "_CategTrainingMorphAccSession" + session + ".jpeg")
py.image.save_as(fig2, fileDirectory + filename + "_CategTrainingSession" + session + ".jpeg")

#close all open files
# f.close()

print("Done!")
