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
        if (f1 == self.FL.frequencyList[19] and f2 == self.FL.frequencyList[13])\
                or (f1 == self.FL.frequencyList[13] and f2 == self.FL.frequencyList[19]):
            return True
        else:
            return False



    def parseAcc(self, accuracy, stimuli):
        for iSubject in range(len(accuracy)):
            for iBlock in range(accuracy[iSubject].size):
                sameAcc = []
                m3w5Acc = []
                m3w95Acc = []
                m3bAcc = []
                m6_5Acc = []
                m6_95Acc = []
                for iTrial in range(accuracy[iSubject][0,iBlock].size):
                    stim1 = int(round(stimuli[iSubject][0,iBlock][0,iTrial]))
                    stim2 = int(round(stimuli[iSubject][0,iBlock][2,iTrial]))

                    if stim1 == stim2:
                        sameAcc.append(accuracy[iSubject][0,iBlock][0,iTrial])
                    elif self.m6_5(stim1, stim2) == True:
                        m6_5Acc.append(accuracy[iSubject][0,iBlock][0,iTrial])
                    elif self.m6_95(stim1, stim2) == True:
                        m6_95Acc.append(accuracy[iSubject][0,iBlock][0,iTrial])
                    elif self.m3w5(stim1, stim2) == True:
                        m3w5Acc.append(accuracy[iSubject][0,iBlock][0,iTrial])
                    elif self.m3w95(stim1, stim2) == True:
                        m3w95Acc.append(accuracy[iSubject][0,iBlock][0,iTrial])
                    elif self.m3b(stim1, stim2) == True:
                        m3bAcc.append(accuracy[iSubject][0,iBlock][0,iTrial])

            self.ACC.append(stat.mean(sameAcc))
            self.ACC.append(stat.mean(m3w5Acc))
            self.ACC.append(stat.mean(m3w95Acc))
            self.ACC.append(stat.mean(m3bAcc))
            self.ACC.append(stat.mean(m6_5Acc))
            self.ACC.append(stat.mean(m6_95Acc))

    def parseRT (self, RT, stimuli):
        for iSubject in range(len(RT)):
            for iBlock in range(RT[iSubject].size):
                sameRT = []
                m3w5RT = []
                m3w95RT = []
                m3bRT = []
                m6_5RT = []
                m6_95RT = []
                for iTrial in range(RT[iSubject][0,iBlock].size):
                    stim1 = int(round(stimuli[iSubject][0,iBlock][0,iTrial]))
                    stim2 = int(round(stimuli[iSubject][0,iBlock][2,iTrial]))

                    if stim1 == stim2:
                        sameRT.append(RT[iSubject][0,iBlock][0,iTrial])
                    elif self.m6_5(stim1, stim2) == True:
                        m6_5RT.append(RT[iSubject][0,iBlock][0,iTrial])
                    elif self.m6_95(stim1, stim2) == True:
                        m6_95RT.append(RT[iSubject][0,iBlock][0,iTrial])
                    elif self.m3w5(stim1, stim2) == True:
                        m3w5RT.append(RT[iSubject][0,iBlock][0,iTrial])
                    elif self.m3w95(stim1, stim2) == True:
                        m3w95RT.append(RT[iSubject][0,iBlock][0,iTrial])
                    elif self.m3b(stim1, stim2) == True:
                        m3bRT.append(RT[iSubject][0,iBlock][0,iTrial])

            self.RT.append(stat.mean(sameRT))
            self.RT.append(stat.mean(m3w5RT))
            self.RT.append(stat.mean(m3w95RT))
            self.RT.append(stat.mean(m3bRT))
            self.RT.append(stat.mean(m6_5RT))
            self.RT.append(stat.mean(m6_95RT))


    def calcAccRT(self, accuracy, RT, stimuli):
        self.parseAcc(accuracy, stimuli)
        self.parseRT(RT, stimuli)