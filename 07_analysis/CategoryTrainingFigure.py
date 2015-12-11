import numpy as np
import scipy.io as sio
from matplotlib import pyplot as plt
import statistics as stat
from math import log2

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

# for i in range(RT.size):
print(m_middleM_accuracy[1][1])

n_groups = 3
accuracy_mean = ((sum(catProto_accuracy)/len(catProto_accuracy)), (sum(middleM_accuracy)/len(middleM_accuracy)), (sum(catBound_accuracy)/len(catBound_accuracy)))
SEM = (np.std(catProto_accuracy), np.std(middleM_accuracy), np.std(catBound_accuracy))
fig = plt.subplot()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 1

plt.bar(index, accuracy_mean, alpha=opacity, width = bar_width, color='b')

plt.xlabel('Stimuli')
plt.ylabel('Accuracy')
plt.title(subjectName + ' Accuracy by Difficulty of Morphs')
plt.xticks(index+(bar_width), ('Category Prototype Morphs', 'Middle Morphs', 'Category Boundary Morphs'))
plt.tight_layout()
plt.grid(b=None, which='major', axis='y')
saveName = '/Users/courtney/GoogleDrive/Riesenhuber/05_2015_scripts/Vibrotactile/01_CategoryTraining/data/' + subjectName +'/' + subjectName+'_CategoryTrainingAccuracy.jpg'

print('Saving under...'+ saveName)
plt.savefig(saveName)
print('done!')
plt.plot(accuracy[0],'r--',  accuracy[1],'g--', accuracy[2],'b--')
plt.legend((line1, line2, line3), ('Category Prototype Morphs', 'Middle Morphs', 'Category Boundary Morphs'))
plt.show()