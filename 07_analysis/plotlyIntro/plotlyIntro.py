import matplotlib.pyplot as plot
import numpy as np
import scipy.io as sio

data = sio.loadmat('/Volumes/maxlab/vibrotactile/04_Aim1/02_spatialLocalization/1000/20151118_1239-1000_block7.mat')
# variables = sio.whosmat('/Volumes/maxlab/vibrotactile/04_Aim1/02_spatialLocalization/1000/20151118_1239-1000_block7.mat')

trialOutput = data['trialOutput']
varNames = trialOutput.dtype

print(trialOutput)
print(trialOutput.size)
print(trialOutput.ndim)
print(trialOutput.shape)

trialOutputSplit = np.hsplit(trialOutput, trialOutput.size)
for row in trialOutputSplit:
    print(row)

# for i in trialOutput:
#     if trialOutput.varNames == reactionTime:
#         mean()

# for i in trialOutput:

print(trialOutput[0])

print(list(data.keys()))
print(list(data.values()))
iterator = iter(data)
for iterator in data:
    if iterator == 'trialOutput':
        trialOutput = data.values()
    if iterator == 'exptdesign':
        exptdesign = data.values()

# trialOutput = trialOutput[0]
# for counter in trialOutput:
#     print(counter)


# exptdesign = variables[0]
# trialOutput = variables[1]

# print(exptdesign(data))
# print(trialOutput)