from frequencyGenerator import FrequencyGenerator
import statistics as stat
#############################################################################
#Calculations by frequency pair
#############################################################################

class FrequencySpecific():
    def __init__(self, stimuli = None):
        self.ACC = []
        self.RT = []
        self.FL = FrequencyGenerator()
        self.stimuli = stimuli

    def frequencyPair_parse(self, rawData):
        f1 = []
        f2 = []
        f3 = []
        f4 = []
        f5 = []
        f6 = []
        f7 = []
        f8 = []
        f9 = []
        f13 = []
        f14 = []
        f15 = []
        f16 = []
        f17 = []
        f18 = []
        f19 = []
        f20 = []
        f21 = []

        countF1 = countF2 = countF3 = countF4 = countF5 = countF6 = countF7 = countF8 = countF9 = 0
        countF13 = countF14 = countF15 = countF16 = countF17 = countF18 = countF19 = countF20 = countF21 = 0
        for iBlock in range(rawData.size):
            for iTrial in range(rawData[0,iBlock].size):
                stimulus = round(self.stimuli[0,iBlock][0,iTrial])
                if stimulus == self.FL.frequencyList[0]:
                    f1.append(rawData[0,iBlock][0,iTrial])
                    countF1 += 1
                elif stimulus == self.FL.frequencyList[20]:
                    f21.append(rawData[0,iBlock][0,iTrial])
                    countF21 += 1
                elif stimulus == self.FL.frequencyList[1]:
                    f2.append(rawData[0,iBlock][0,iTrial])
                    countF2 += 1
                elif stimulus == self.FL.frequencyList[19]:
                    f20.append(rawData[0,iBlock][0,iTrial])
                    countF20 += 1
                elif stimulus == self.FL.frequencyList[2]:
                    f3.append(rawData[0,iBlock][0,iTrial])
                    countF3 += 1
                elif stimulus == self.FL.frequencyList[18]:
                    f19.append(rawData[0,iBlock][0,iTrial])
                    countF19 += 1
                elif stimulus == self.FL.frequencyList[3]:
                    f4.append(rawData[0,iBlock][0,iTrial])
                    countF4 += 1
                elif stimulus == self.FL.frequencyList[17]:
                    f18.append(rawData[0,iBlock][0,iTrial])
                    countF18 += 1
                elif stimulus == self.FL.frequencyList[4]:
                    f5.append(rawData[0,iBlock][0,iTrial])
                    countF5 += 1
                elif stimulus == self.FL.frequencyList[16]:
                    f17.append(rawData[0,iBlock][0,iTrial])
                    countF17 += 1
                elif stimulus == self.FL.frequencyList[5]:
                    f6.append(rawData[0,iBlock][0,iTrial])
                    countF6 += 1
                elif stimulus == self.FL.frequencyList[15]:
                    f16.append(rawData[0,iBlock][0,iTrial])
                    countF16 += 1
                elif stimulus == self.FL.frequencyList[6]:
                    f7.append(rawData[0,iBlock][0,iTrial])
                    countF7 += 1
                elif stimulus == self.FL.frequencyList[14]:
                    f15.append(rawData[0,iBlock][0,iTrial])
                    countF15 += 1
                elif stimulus == self.FL.frequencyList[7]:
                    f8.append(rawData[0,iBlock][0,iTrial])
                    countF8 += 1
                elif stimulus == self.FL.frequencyList[13]:
                    f14.append(rawData[0,iBlock][0,iTrial])
                    countF14 += 1
                elif stimulus == self.FL.frequencyList[8]:
                    f9.append(rawData[0,iBlock][0,iTrial])
                    countF9 += 1
                elif stimulus == self.FL.frequencyList[12]:
                    f13.append(rawData[0,iBlock][0,iTrial])
                    countF13 += 1

        temp = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f13, f14, f15, f16, f17, f18, f19, f20, f21]
        countTotal = [str(countF1), str(countF2), str(countF3), str(countF4),
                      str(countF5), str(countF6), str(countF7), str(countF8),
                      str(countF9), str(countF13), str(countF14), str(countF15),
                      str(countF16), str(countF17), str(countF18), str(countF19),
                      str(countF20), str(countF21)]

        self.checkForZero(temp)

        mF = [stat.mean(f1), stat.mean(f2), stat.mean(f3), stat.mean(f4), stat.mean(f5),
              stat.mean(f6), stat.mean(f7), stat.mean(f8), stat.mean(f9), stat.mean(f13),
              stat.mean(f14), stat.mean(f15), stat.mean(f16), stat.mean(f17), stat.mean(f18),
              stat.mean(f19), stat.mean(f20), stat.mean(f21)]

        return mF, countTotal

    def checkForZero(self, list):
        for subList in list:
            if subList == []:
                subList.append(0)
                subList.append(0)