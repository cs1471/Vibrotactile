from scipy import stats

class Dprime:
    def __init__(self):
        self.TPR = []
        self.FPR = []
        self.TNR = []
        self.FNR = []
        self.totalTP = []
        self.totalFP = []
        self.totalTN = []
        self.totalFN = []

    def parseData(self, accuracy, stimuli):
        for iSession in range(len(accuracy)):
            truePositive = []
            falsePositive = []
            trueNegative = []
            falseNegative = []
            for iBlock in range(accuracy[iSession].size):
                for iTrial in range(accuracy[iSession][0,iBlock].size):
                    stim1 = int(round(stimuli[iSession][0,iBlock][0,iTrial]))
                    stim2 = int(round(stimuli[iSession][0,iBlock][2,iTrial]))
                    if stim1 != stim2:
                        if accuracy[iSession][0,iBlock][0,iTrial] == 1:
                            truePositive.append(1)
                        elif accuracy[iSession][0,iBlock][0,iTrial] != 1:
                            falsePositive.append(1)
                        else:
                            print("Sorry something seems to be wrong with your parse data function in your dprime class")
                            print("Here are the different stimuli that are bot being parsed")
                            print(stim1, stim2)
                    elif stim1 == stim2:
                        if accuracy[iSession][0,iBlock][0,iTrial] == 1:
                            trueNegative.append(1)
                        elif accuracy[iSession][0,iBlock][0,iTrial] != 1:
                            falseNegative.append(1)
                        else:
                            print("Sorry something seems to be wrong with your parse data function in your dprime class")
                            print("Here are the same stimuli that are bot being parsed")
                            print(stim1, stim2)
            self.TPR.append(sum(truePositive)/sum(truePositive + falsePositive))
            self.FPR.append(sum(falsePositive)/sum(truePositive + falsePositive))
            self.TNR.append(sum(trueNegative)/sum(trueNegative + falseNegative))
            self.FNR.append(sum(falseNegative)/sum(trueNegative + falseNegative))
            self.totalTP.append(sum(truePositive))
            self.totalFP.append(sum(falsePositive))
            self.totalTN.append(sum(trueNegative))
            self.totalFN.append(sum(falseNegative))

    def zscore(self):
        zscore = [stats.zscore(self.TPR), stats.zscore(self.FPR),
                  stats.zscore(self.TNR), stats.zscore(self.FNR)]

        return zscore

    def dPrimeCalc(self):
        dprime = []
        for index, value in enumerate(self.zscore(self.TPR)):
            dprime.append(value - self.zscore(self.FNR)[index])
        return dprime