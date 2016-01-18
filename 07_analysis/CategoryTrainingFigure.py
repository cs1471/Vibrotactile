#Trying to make a notebook not sure if I am succedding
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
import plotly.plotly as py
import statistics as stat
import math as m
import plotly.graph_objs as go
import plotly.tools as tls

#################################################################################
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

def makeFrequency():
    frequencyList = [i for i in my_range(0, 2, 0.1)]

    for index,obj in enumerate(frequencyList):
        obj += m.log2(25)
        frequencyList[index] = round(2**obj)
    return frequencyList

#################################MAIN##########################################
# filename = input('Enter a filename: \n')
# fileDirectory = input('Enter the directory where you want your figure saved: /n')

filename = ('20151209_1728-MR1000_block6')
fileDirectory = '/Users/courtney/GoogleDrive/Riesenhuber/05_2015_scripts/Vibrotactile/01_CategoryTraining/data/1000/'
multipleSession = 'y'
session = '1'
dprimeCalc = 'y'

#load matfile
data = sio.loadmat(fileDirectory + filename, struct_as_record=True)

#make list of frequencies tested
frequencyList = makeFrequency()

#pull relevant data from structures
responseStartTime = data['trialOutput']['responseStartTime']
responseFinishedTime = data['trialOutput']['responseFinishedTime']
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

i = 0
mAcc_categoryA = []

for i in range(len(b_categoryA)):
    mAcc_categoryA.append(stat.mean(b_categoryA[i]))

i = 0
mAcc_categoryB = []
for i in range(len(b_categoryB)):
    mAcc_categoryB.append(stat.mean(b_categoryB[i]))

#calculate the accuracy by difficulty
i=j=counter=0
m_catProto_accuracy = []
m_middleM_accuracy = []
m_catBound_accuracy = []

for i in range(sResp.size):
    catProto_accuracy = []
    middleM_accuracy = []
    catBound_accuracy = []
    for counter in range(sResp[0,i].size):
        stimulus = round(stimuli[0,i][0,counter])
        if accuracy[0,i][0,counter]==1:
            if stimulus == frequencyList[0] or stimulus == frequencyList[1] or stimulus == frequencyList[2]:
                catProto_accuracy.insert(counter,1)
            elif stimulus == frequencyList[19] or stimulus == frequencyList[18] or stimulus == frequencyList[17]:
                catProto_accuracy.insert(counter,1)
            elif stimulus == frequencyList[3] or stimulus == frequencyList[4] or stimulus == frequencyList[5]:
                middleM_accuracy.insert(counter,1)
            elif stimulus == frequencyList[16] or stimulus == frequencyList[15] or stimulus == frequencyList[14]:
                middleM_accuracy.insert(counter,1)
            elif stimulus == frequencyList[6] or stimulus == frequencyList[7] or stimulus == frequencyList[8]:
                catBound_accuracy.insert(counter,1)
            elif stimulus == frequencyList[13] or stimulus == frequencyList[12] or stimulus == frequencyList[11]:
                catBound_accuracy.insert(counter,1)
        else:
            if stimulus == frequencyList[0] or stimulus == frequencyList[1] or stimulus == frequencyList[2]:
                catProto_accuracy.insert(counter,0)
            elif stimulus == frequencyList[19] or stimulus == frequencyList[18] or stimulus == frequencyList[17]:
                catProto_accuracy.insert(counter,0)
            elif stimulus == frequencyList[3] or stimulus == frequencyList[4] or stimulus == frequencyList[5]:
                middleM_accuracy.insert(counter,0)
            elif stimulus == frequencyList[16] or stimulus == frequencyList[15] or stimulus == frequencyList[14]:
                middleM_accuracy.insert(counter,0)
            elif stimulus == frequencyList[6] or stimulus == frequencyList[7] or stimulus == frequencyList[8]:
                catBound_accuracy.insert(counter,0)
            elif stimulus == frequencyList[13] or stimulus == frequencyList[12] or stimulus == frequencyList[11]:
                catBound_accuracy.insert(counter,0)
    m_catProto_accuracy.append(catProto_accuracy)
    m_catBound_accuracy.append(catBound_accuracy)
    m_middleM_accuracy.append(middleM_accuracy)

#calculate the mean accuracy by difficulty by block
cp_mean=[]
counter =0
for counter in range(len(m_catProto_accuracy)):
    if m_catProto_accuracy[counter] != []:
        cp_mean.append(sum(m_catProto_accuracy[counter])/len(m_catProto_accuracy[counter]))
    else:
        cp_mean.append(0)

mm_mean=[]
counter =0
for counter in range(len(m_middleM_accuracy)):
    if m_middleM_accuracy[counter] != []:
        mm_mean.append(sum(m_middleM_accuracy[counter])/len(m_middleM_accuracy[counter]))
    else:
        mm_mean.append(0)

cb_mean=[]
counter =0
for counter in range(len(m_catBound_accuracy)):
    if m_catBound_accuracy[counter] != []:
        cb_mean.append(sum(m_catBound_accuracy[counter])/len(m_catBound_accuracy[counter]))
    else:
        cb_mean.append(0)

#calculate the mean overall accuracy by block
y = []
for i in range(accuracy.size):
    y.append([np.mean([accuracy[0,i]])])

i=0
x=[]
for i in range(nBlocks):
            x.append("Block: " + str(i+1) + ", Level: " + str(level[0,i][0,0])),

# (1.1) Define a trace-generating function (returns a Bar object)
def make_trace_bar(y, name):
    return go.Bar(
        x = x,
        y=y,            # take in the y-coords
        name=name,      # label for hover
        xaxis='x1',                    # (!) both subplots on same x-axis
        yaxis='y1'
    )

def make_trace_line(y, name):
    return go.Scatter(
        x=x,
        y=y,            # take in the y-coords
        name=name,      # label for hover
        xaxis='x1',                    # (!) both subplots on same x-axis
        yaxis='y1'
    )


#make trace containing data you wanted plotted
trace1 = make_trace_bar(cp_mean, "Category Prototype Accuracy")
trace2 = make_trace_bar(mm_mean, "Middle Morph Accuracy")
trace3 = make_trace_bar(cb_mean, "Category Boundary Accuracy")
trace4 = make_trace_line(y, "Overall Accuracy")
trace5 = make_trace_bar(mAcc_categoryA, 'Category A Acc (LF prox to wrist)')
trace6 = make_trace_bar(mAcc_categoryB, 'Category B Acc (HF prox to wrist)')

# matFileName = fileDirectory + filename
# dataFile = sio.savemat(matFileName, {'x':x, 'y':y, 'cp_mean': cp_mean, 'mm_mean': mm_mean, 'cb_mean': cb_mean)
# dataFile.write(x,y,cp_mean, mm_mean, cb_mean,)
# dataFile.close()


# Generate Figure object with 2 axes on 2 rows, print axis grid to stdout
fig = tls.make_subplots(
    rows=1,
    cols=1,
    shared_xaxes=True
)

fig2 = tls.make_subplots(
    rows=1,
    cols=1,
    shared_xaxes=True
)

#concatenate data you want plotted
fig['data'] = go.Data([trace1, trace2, trace3, trace4])
fig2['data'] = go.Data([trace4, trace5, trace6])

#set figure layout to hold mutlitple bars
fig['layout'].update(
    barmode='group',
    bargroupgap=0,
    bargap=0.25
)

fig2['layout'].update(
    barmode='group',
    bargroupgap=0,
    bargap=0.25
)

#set title of figure data
fig['layout'].update(
    title = subjectName + " Accuracy by difficulty, Session: " + session
)
fig2['layout'].update(
    title = subjectName + " Accuracy by Category Type, Session: " + session
)

#get the url of your figure to embed in html later
first_plot_url = py.plot(fig, filename= subjectName + "subjectData" + session, auto_open=False,)
tls.get_embed(first_plot_url)
second_plot_url = py.plot(fig2, filename= subjectName + "subjectData2" + session, auto_open=False,)
tls.get_embed(second_plot_url)

print("Your graph will be saved in this directory: " + fileDirectory + "\n")
print("Your graph will be saved under: " + filename + "\n")
#embed figure data in html
html_string = '''
<html>
    <head>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
        <style>body{ margin:0 100; background:whitesmoke; }</style>
    </head>
    <body>
        <!-- *** Accuracy by Morph *** --->
        <iframe width="1000" height="550" frameborder="0" seamless="seamless" scrolling="no" \
src="'''+ first_plot_url + '''.embed?width=800&height=550"></iframe>
        <!-- *** Accuracy by Category *** --->
        <iframe width="1000" height="550" frameborder="0" seamless="seamless" scrolling="no" \
src="'''+ second_plot_url + '''.embed?width=800&height=550"></iframe>
    </body>
</html>'''

#save figure data in location specific previously
f = open(fileDirectory + filename + '.html','w')
f.write(html_string)

py.image.save_as(fig, fileDirectory + filename + "CategoryTrainingAccMorph.png")
py.image.save_as(fig2, fileDirectory + filename + "CategoryTrainingAccCategory.png")

#close all open files
f.close()

print("Done!")
