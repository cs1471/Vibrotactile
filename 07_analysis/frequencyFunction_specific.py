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
        for iBlock in range(rawData.size):
            for iTrial in range(rawData[0,iBlock].size):
                stimulus = round(self.stimuli[0,iBlock][0,iTrial])
                if stimulus == self.FL.frequencyList[0] or stimulus == self.FL.frequencyList[20]:
                    f1.append(rawData[0,iBlock][0,iTrial])
                elif stimulus == self.FL.frequencyList[1] or stimulus == self.FL.frequencyList[19]:
                    f2.append(rawData[0,iBlock][0,iTrial])
                elif stimulus == self.FL.frequencyList[2] or stimulus == self.FL.frequencyList[18]:
                    f3.append(rawData[0,iBlock][0,iTrial])
                elif stimulus == self.FL.frequencyList[3] or stimulus == self.FL.frequencyList[17]:
                    f4.append(rawData[0,iBlock][0,iTrial])
                elif stimulus == self.FL.frequencyList[4] or stimulus == self.FL.frequencyList[16]:
                    f5.append(rawData[0,iBlock][0,iTrial])
                elif stimulus == self.FL.frequencyList[5] or stimulus == self.FL.frequencyList[15]:
                    f6.append(rawData[0,iBlock][0,iTrial])
                elif stimulus == self.FL.frequencyList[6] or stimulus == self.FL.frequencyList[14]:
                    f7.append(rawData[0,iBlock][0,iTrial])
                elif stimulus == self.FL.frequencyList[7] or stimulus == self.FL.frequencyList[13]:
                    f8.append(rawData[0,iBlock][0,iTrial])
                elif stimulus == self.FL.frequencyList[8] or stimulus == self.FL.frequencyList[12]:
                    f9.append(rawData[0,iBlock][0,iTrial])

        mF = [stat.mean(f1), stat.mean(f2), stat.mean(f3), stat.mean(f4), stat.mean(f5),
              stat.mean(f6), stat.mean(f7), stat.mean(f8), stat.mean(f9)]

        return mF