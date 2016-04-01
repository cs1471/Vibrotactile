from frequencyGenerator import FrequencyGenerator
import statistics as stat

class category():
    def __init__(self, stimuli):
        self.stim = stimuli
        self.FL = FrequencyGenerator()

    def catProtoMorph95(self, stim):
        if stim == self.FL.frequencyList[0] or stim == self.FL.frequencyList[1] or stim == self.FL.frequencyList[2]:
            return True
        else:
            return False

    def catProtoMorph5(self, stim):
        if stim == self.FL.frequencyList[20] or stim == self.FL.frequencyList[19] or stim == self.FL.frequencyList[18]:
            return True
        else:
            return False

    def middleMorph95(self, stim):
        if stim == self.FL.frequencyList[3] or stim == self.FL.frequencyList[4] or stim == self.FL.frequencyList[5]:
            return True
        else:
            return False

    def middleMorph5(self, stim):
        if stim == self.FL.frequencyList[17] or stim == self.FL.frequencyList[16] or stim == self.FL.frequencyList[15]:
            return True
        else:
            return False

    def catBoundMorph95(self, stim):
        if stim == self.FL.frequencyList[6] or stim == self.FL.frequencyList[7] or stim == self.FL.frequencyList[8]:
            return True
        else:
            return False

    def catBoundMorph5(self, stim):
        if stim == self.FL.frequencyList[14] or stim == self.FL.frequencyList[13] or stim == self.FL.frequencyList[12]:
            return True
        else:
            return False


    def parser(self, rawData):
        #calculate the accuracy by morph
        data = []
        for iBlock in range(rawData.size):
            b_catProto = []
            b_middleM = []
            b_catBound = []
            for iTrial in range(rawData[0,iBlock].size):
                stimulus = round(self.stim[0,iBlock][0,iTrial])
                if self.catProtoMorph95(stimulus) == True:
                    b_catProto.append(rawData[0,iBlock][0,iTrial])
                elif  self.catProtoMorph5(stimulus) == True:
                    b_catProto.append(rawData[0,iBlock][0,iTrial])
                elif self.middleMorph95(stimulus):
                    b_middleM.append(rawData[0,iBlock][0,iTrial])
                elif self.middleMorph5(stimulus):
                    b_middleM.append(rawData[0,iBlock][0,iTrial])
                elif self.catBoundMorph95(stimulus):
                    b_catBound.append(rawData[0,iBlock][0,iTrial])
                elif self.catBoundMorph5(stimulus):
                    b_catBound.append(rawData[0,iBlock][0,iTrial])
                else:
                    print("There is something wrong with your morph parsing function and stimuli are not be classified")
                    print("The following were stimuli were not parsed: ")
                    print(stimulus)
            if b_catProto != []:
                data.append(sum(b_catProto)/len(b_catProto))
            else:
                data.append(0)

            if b_middleM != []:
                data.append(stat.mean(b_middleM))
            else:
                data.append(0)

            if b_catBound != []:
                data.append(stat.mean(b_catBound))
            else:
                data.append(0)
        return data

    def wrapper(self, ACC, RT):
        RT = self.parser(RT)
        ACC = self.parser(ACC)
        return RT, ACC
