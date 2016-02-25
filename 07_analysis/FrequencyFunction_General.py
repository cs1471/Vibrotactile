import statistics as stat
from frequencyGenerator import FrequencyGenerator

class Frequency_general():
    def __init__(self):
        self.RT = [[]]
        self.ACC = [[]]
        self.FL = FrequencyGenerator()

    def m3b(self, f1, f2):
        if (f1 == self.FL.frequencyList[7] and f2 == self.FL.frequencyList[13])\
                or (f1 == self.FL.frequencyList[13] and f2 == self.FL.frequencyList[7]):
            return True
        else:
            return False

    def m3w5(self, f1, f2):
        if (f1 == self.FL.frequencyList[19] and f2 == self.FL.frequencyList[13])\
                or (f1 == self.FL.frequencyList[13] and f2 == self.FL.frequencyList[19]):
            return True
        else:
            return False

    def m3w95(self, f1, f2):
        if (f1 == self.FL.frequencyList[1] and f2 == self.FL.frequencyList[7])\
                or (f1 == self.FL.frequencyList[7] and f2 == self.FL.frequencyList[1]):
            return True
        else:
            return False

    def m6_5(self, f1, f2):
        if (f1 == self.FL.frequencyList[7] and f2 == self.FL.frequencyList[19])\
                or (f1 == self.FL.frequencyList[19] and f2 == self.FL.frequencyList[7]):
            return True
        else:
            return False

    def m6_95(self, f1, f2):
        if (f1 == self.FL.frequencyList[1] and f2 == self.FL.frequencyList[13])\
                or (f1 == self.FL.frequencyList[13] and f2 == self.FL.frequencyList[1]):
            return True
        else:
            return False

    def calcAccRT(self, ACC, RT, stimuli):
        self.ACC = self._calcAccRT('ACC', ACC, stimuli)
        self.RT = self._calcAccRT('RT', RT, stimuli)

    def _calcAccRT(self, dataStringID, dataToParse, stimuli):
        if dataStringID == 'ACC':
            return self.parser(dataToParse, stimuli)
        elif dataStringID == 'RT':
            return self.parser(dataToParse, stimuli)
        else:
            print("Sorry the data requested to parse is not recognized")

    def parser(self, dataRaw, stimuli):
        data = []
        for iSubject in range(len(dataRaw)):
            same = []
            m3w5 = []
            m3w95 = []
            m3b = []
            m6_5 = []
            m6_95 = []
            for iBlock in range(dataRaw[iSubject].size):
                for iTrial in range(dataRaw[iSubject][0,iBlock].size):
                    stim1 = int(round(stimuli[iSubject][0,iBlock][0,iTrial]))
                    stim2 = int(round(stimuli[iSubject][0,iBlock][2,iTrial]))

                    if stim1 == stim2:
                        same.append(dataRaw[iSubject][0,iBlock][0,iTrial])
                    elif self.m6_5(stim1, stim2) == True:
                        m6_5.append(dataRaw[iSubject][0,iBlock][0,iTrial])
                    elif self.m6_95(stim1, stim2) == True:
                        m6_95.append(dataRaw[iSubject][0,iBlock][0,iTrial])
                    elif self.m3w5(stim1, stim2) == True:
                        m3w5.append(dataRaw[iSubject][0,iBlock][0,iTrial])
                    elif self.m3w95(stim1, stim2) == True:
                        m3w95.append(dataRaw[iSubject][0,iBlock][0,iTrial])
                    elif self.m3b(stim1, stim2) == True:
                        m3b.append(dataRaw[iSubject][0,iBlock][0,iTrial])

            data.append([sum(same)/len(same), stat.mean(m3w5), stat.mean(m3w95), stat.mean(m3b), stat.mean(m6_5), stat.mean(m6_95)])

        return data