#packages to import
import scipy.io as sio
import plotly.plotly as py
import statistics as stat
import plotly.graph_objs as go
import plotly.tools as tls
import glob
import os
from frequencyGenerator import FrequencyGenerator as FG
from dPrime import Dprime
from FrequencyFunction_General import Frequency_general
from PositionFunction_General import Position_general

tls.set_credentials_file(username='cs1471', api_key='9xknhmjhas')

# filename = input('Enter a filename: \n')
# fileDirectory = input('Enter the directory where you want your figure saved: /n')
# session = input('Enter the session number: \n')

#Use when debugging or manually editing
fileDirectory = '/Users/courtney/GoogleDrive/Riesenhuber/05_2015_scripts/Vibrotactile/06_frequencyDiscrimination/data/groupData'

os.chdir(fileDirectory)

data = []
for file in glob.glob("*.mat"):
    data.append(sio.loadmat(file, struct_as_record=True))

#pull relevant data from structures
iSubject = 0
#pull relevant data from structures
RT            = [data[iSubject]['trialOutput']['RT'] for iSubject in range(len(data))]
accuracy      = [data[iSubject]['trialOutput']['accuracy'] for iSubject in range(len(data))]
stimuli       = [data[iSubject]['trialOutput']['stimuli'] for iSubject in range(len(data))]
subjectNumber = [data[iSubject]['exptdesign']['number'][0,0][0] for iSubject in range(len(data))]

#############################################################################
#Calculations by Acc category type
#############################################################################

FreqObj = Frequency_general()
FreqObj.calcAccRT(accuracy, RT, stimuli)

#############################################################################
#Calculations by position
#############################################################################
PosObj = Position_general()
PosObj.calcAccRT(accuracy, RT, stimuli, 'freq')

#############################################################################
#Calculating dPrime
#############################################################################
dPrimeObj = Dprime()
dprime = dPrimeObj.dPrimeCalc(accuracy, stimuli)


x = ["Diff Pos3", "Diff Pos5", "Diff Pos9", "Diff Pos11", "Same Pos3", "Same Pos5", "Same Pos9", "Same Pos11"]
x2 = ["Same", "62.50 v 40.00", "90.91 v 62.50", "40.00 v 27.03", "90.91 v 40.00", "62.50 v 27.03"]
x3 = ['Dprime', 'True Positive Rate', 'False Positive Rate', 'True Negative Rate', 'False Negative Rate']

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
trace_PG_ACC = []
trace_PG_RT = []
trace_FG_ACC = []
trace_FG_RT = []
trace_dprime = []
for index, iSubject in enumerate(subjectNumber):
    trace_PG_ACC.append(make_trace_bar(x, PosObj.PG.ACC[(index+1)], iSubject))
    trace_PG_RT.append(make_trace_line(x, PosObj.PG.RT[(index+1)], iSubject))
    trace_FG_ACC.append(make_trace_bar(x2, FreqObj.ACC[(index+1)], iSubject))
    trace_FG_RT.append(make_trace_line(x2, FreqObj.RT[(index+1)], iSubject))
    trace_dprime.append(make_trace_bar(x3, [dprime[index], dPrimeObj.TPR[index], dPrimeObj.FPR[index], dPrimeObj.TNR[index], dPrimeObj.FNR[index]], iSubject))

# Generate Figure object with 2 axes on 2 rows, print axis grid to stdout
figFreq_ACC = tls.make_subplots(rows=1, cols=1, shared_xaxes=True)
figPos_ACC  = tls.make_subplots(rows=1, cols=1, shared_xaxes=True)
figFreq_RT = tls.make_subplots(rows=1, cols=1, shared_xaxes=True)
figPos_RT  = tls.make_subplots(rows=1, cols=1, shared_xaxes=True)
figDPrime = tls.make_subplots(rows=1, cols=1, shared_xaxes=True)

#set figure layout to hold mutlitple bars
figFreq_ACC['layout'].update(barmode='group', bargroupgap=0, bargap=0.25,
    title = "Accuracy by Frequency on Single Stimuli Frequency Discrimination Task")

figPos_ACC['layout'].update(barmode='group', bargroupgap=0, bargap=0.25,
    title = "Accuracy by Position on Single Stimuli Frequency Discrimination Task")

figDPrime['layout'].update(barmode='group', bargroupgap=0, bargap=0.25,
    title = "Dprime Across Subjects on Single Stimuli Frequency Discrimination Task")

figFreq_RT['layout'].update(barmode='group', bargroupgap=0, bargap=0.25,
    title = "RT by Frequency on Single Stimuli Frequency Discrimination Task")

figPos_RT['layout'].update(barmode='group', bargroupgap=0, bargap=0.25,
    title = "RT by Position on Single Stimuli Frequency Discrimination Task")

figFreq_ACC['data'] = [trace_FG_ACC]
figFreq_RT['data']  = [trace_FG_RT]
figDPrime['data']   = [trace_dprime]
figPos_ACC['data']  = [trace_PG_ACC]
figPos_RT['data']   = [trace_PG_RT]
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
py.image.save_as(figDPrime, fileDirectory + "frequencyDiscrim_Dprime_Group.jpeg")
py.image.save_as(figPos_ACC, fileDirectory + "frequencyDiscrim_Pos_ACC_Group.jpeg")
py.image.save_as(figPos_RT, fileDirectory + "frequencyDiscrim_Pos_RT_Group.jpeg")
#close all open files
# f.close()

print("Done!")
