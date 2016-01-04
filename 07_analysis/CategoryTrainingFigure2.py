import statistics as stat
from math import log2
import plotly as plt
import numpy as np
import scipy.io as sio

page_template = """
<html>
  <script src="https://www.google.com/jsapi" type="text/javascript"></script>
  <script>
    google.load('visualization', '1', {packages:['table']});

    google.setOnLoadCallback(drawTable);
    function drawTable() {
      %(jscode)s
      var jscode_table = new google.visualization.Table(document.getElementById('table_div_jscode'));
      jscode_table.draw(jscode_data, {showRowNumber: true});

      var json_table = new google.visualization.Table(document.getElementById('table_div_json'));
      var json_data = new google.visualization.DataTable(%(json)s, 0.6);
      json_table.draw(json_data, {showRowNumber: true});
    }
  </script>
  <body>
    <H1>Table created using ToJSCode</H1>
    <div id="table_div_jscode"></div>
    <H1>Table created using ToJSon</H1>
    <div id="table_div_json"></div>
  </body>
</html>
"""

def my_range(start, end, step):
    while start <= end:
        yield start
        start += step
# filename = input('Enter a filename: ')
# dprimeCalc = input('Do you want to calculate dprime (y/n): \n')
filename = '/Users/courtney/GoogleDrive/Riesenhuber/05_2015_scripts/Vibrotactile/01_CategoryTraining/data/1000/20151208_1505-MR1000_block6.mat'
dprimeCalc = 'n'
data = sio.loadmat(filename, struct_as_record=True)

frequencyList=[]
for i in my_range(0, 2, 0.1):
    frequencyList.append(i)

for index,obj in enumerate(frequencyList):
    obj += log2(25)
    frequencyList[index] = round(2**obj)

#pull relevant data from structures
responseStartTime = data['trialOutput']['responseStartTime']
responseFinishedTime = data['trialOutput']['responseFinishedTime']
RT = data['trialOutput']['RT']
sResp = data['trialOutput']['sResp']
correctResponse = data['trialOutput']['correctResponse']
accuracy = data['trialOutput']['accuracy']
level = data['trialOutput']['level']
stimuli = data['trialOutput']['stimuli']
nTrials=data['exptdesign']['numTrialsPerSession'][0,0][0]
nBlocks=data['exptdesign']['numSessions'][0,0][0]
subjectName = data['exptdesign']['number'][0,0][0]

if dprimeCalc == 'y':
    hit = generalMiss = false_alarm = correct_rejection = correctResponseDiff = correctResponseSame = miss = 0
    for i in range(sResp.size):
        for counter in range(sResp[0,i].size):
            if sResp[0,i][0,counter]==2 and correctResponse[0,i][0,counter]==2:
                hit += 1
                correctResponseDiff += 1
            elif sResp[0,i][0,counter]==1 and correctResponse[0,i][0,counter]==1:
                correct_rejection += 1
                correctResponseSame += 1
            elif sResp[0,i][0,counter]==2 and correctResponse[0,i][0,counter]==1:
                false_alarm += 1
            elif sResp[0,i][0,counter]==1 and correctResponse[0,i][0,counter]==2:
                miss += 1
            else:
                generalMiss += 1

    dprime = (sum(hit))/len(hit) - (sum(false_alarm))/len(false_alarm)/(stat.stdev(hit)-stat.stdev(false_alarm))

i=counter=0
catProto_accuracy = []
middleM_accuracy = []
catBound_accuracy = []
m_catProto_accuracy = []
m_middleM_accuracy = []
m_catBound_accuracy = []
for i in range(sResp.size):
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

n_groups = 3
accuracy_mean = ((sum(catProto_accuracy)/len(catProto_accuracy)), (sum(middleM_accuracy)/len(middleM_accuracy)), (sum(catBound_accuracy)/len(catBound_accuracy)))
SEM = (np.std(catProto_accuracy), np.std(middleM_accuracy), np.std(catBound_accuracy))

#creating data to load into js data table
description = {"difficulty": ("string", "Difficulty"),
               "accuracy": ("number", "Accuracy")}

data = [ {"difficulty": "Category Prototype Accuracy", "accuracy": (accuracy_mean[0])},
         {"difficulty": "Middle Morph Accuracy", "accuracy": (accuracy_mean[1])},
         {"difficulty": "Category Boundary Accuracy", "accuracy": (accuracy_mean[2])}]

#loading into the data table
data_table = gviz.Table(description)
data_table.LoadData(data)

#creat a javascript code string
jscode = data_table.ToJSCode("jscode_data",
                             columns_order=("difficulty","accuracy"),
                             order_by="difficulty")

#create a json string
json = data_table.ToJSon(columns_order = ("difficulty", "accuracy"),
                         order_by = "difficulty")

#put the jscode and json string into the template
print("Content-type:text/html" + page_template % vars())

