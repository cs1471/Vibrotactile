import statistics as stat

class Position_catBound():
    def __init__(self):
        self.RT = []
        self.ACC = []

    def zeroChanDiff_top(self, pos1, pos2):
        if ((pos1 == 5 or pos1 == 6) and (pos2 == 3 or pos2 == 4))\
            or ((pos1 == 3 or pos1 == 4) and (pos2 == 5 or pos2 == 6)):
            return True
        else:
            return False

    def zeroChanDiff_bottom(self, pos1, pos2):
        if ((pos1 == 9 or pos1 == 10) and (pos2 == 11 or pos2 == 12))\
            or ((pos1 == 11 or pos1 == 12) and (pos2 == 9 or pos2 ==10)):
            return True
        else:
            return False

    def oneChanDiff_top(self, pos1, pos2):
        if ((pos1 == 5 or pos1 == 6) and (pos2 == 1 or pos2 == 2)) \
            or ((pos1 == 1 or pos1 == 2) and (pos2 == 5 or pos2 == 6)):
            return True
        else:
            return False

    def oneChanDiff_bottom(self, pos1, pos2):
        if ((pos1 == 9 or pos1 == 10) and (pos2 == 13 or pos2 == 14))\
            or ((pos1 == 13 or pos1 == 14) and (pos2 == 9 or pos2 == 10)):
            return True
        else:
            return False

    def twoChanDiff_top(self, pos1, pos2):
        if ((pos1 == 5 or pos1 == 6) and (pos2 == 11 or pos2 ==12))\
                or ((pos1 == 11 or pos1 ==12) and (pos2 == 5 or pos2 ==6)):
            return True
        else:
            return False

    def twoChanDiff_bottom(self, pos1, pos2):
        if ((pos1 == 9 or pos1 == 10) and (pos2 == 3 or pos2 == 4))\
                or ((pos1 == 3 or pos1 == 4) and (pos2 == 9 or pos2 == 10)):
            return True
        else:
            return False

    def parseData(self, rawData, stimuli, DataID, parseBy ):
        if parseBy == 'Block':
            if DataID == 'ACC':
                self.ACC = self._parseData_block(rawData, stimuli)
            elif DataID == 'RT':
                self.RT = self._parseData_block(rawData, stimuli)
        elif parseBy == 'Subject':
            if DataID == 'ACC':
                self.ACC = self._parseData(rawData, stimuli)
            elif DataID == 'RT':
                self.RT = self._parseData(rawData, stimuli)


    def _parseData(self, accuracy, stimuli):
        data = []
        for iSubject in range(len(accuracy)):
            D_pos5v1 = []
            D_pos5v3 = []
            D_pos5v9 = []
            D_pos5v11 = []
            D_pos9v3 = []
            D_pos9v5 = []
            D_pos9v11 = []
            D_pos9v13 = []
            for iBlock in range(accuracy[iSubject].size):
                for iTrial in range(accuracy[iSubject][0,iBlock].size):
                    if iSubject == 0 or iSubject == 1 or iSubject == 2:
                        pos1 = int(stimuli[iSubject][0,iBlock][0,iTrial])
                        pos2 = int(stimuli[iSubject][0,iBlock][2,iTrial])
                    else:
                        pos1 = int(stimuli[iSubject][0,iBlock][1,iTrial])
                        pos2 = int(stimuli[iSubject][0,iBlock][3,iTrial])
                    if self.oneChanDiff_top(pos1, pos2):
                        D_pos5v1.append(accuracy[iSubject][0,iBlock][0,iTrial])
                    elif self.zeroChanDiff_top(pos1, pos2):
                        D_pos5v3.append(accuracy[iSubject][0,iBlock][0,iTrial])
                    elif ((pos1 == 5 or pos1 == 6) and (pos2 == 9 or pos2 == 10)):
                        D_pos5v9.append(accuracy[iSubject][0,iBlock][0,iTrial])
                    elif self.twoChanDiff_top(pos1, pos2):
                        D_pos5v11.append(accuracy[iSubject][0,iBlock][0,iTrial])
                    elif self.twoChanDiff_bottom(pos1, pos2):
                        D_pos9v3.append(accuracy[iSubject][0,iBlock][0,iTrial])
                    elif ((pos1 == 9 or pos1 == 10) and (pos2 == 5 or pos2 == 6)):
                        D_pos9v5.append(accuracy[iSubject][0,iBlock][0,iTrial])
                    elif self.zeroChanDiff_bottom(pos1, pos2):
                        D_pos9v11.append(accuracy[iSubject][0,iBlock][0,iTrial])
                    elif self.oneChanDiff_bottom(pos1, pos2):
                        D_pos9v13.append(accuracy[iSubject][0,iBlock][0,iTrial])

            data.append([stat.mean(D_pos5v1), stat.mean(D_pos5v3), stat.mean(D_pos5v9), stat.mean(D_pos5v11),
                             stat.mean(D_pos9v3), stat.mean(D_pos9v5), stat.mean(D_pos9v11), stat.mean(D_pos9v13)])
        return data

    def _parseData_block(self, accuracy, stimuli):
        data = []
        for iBlock in range(accuracy.size):
            D_pos5v1 = []
            D_pos5v3 = []
            D_pos5v9 = []
            D_pos5v11 = []
            D_pos9v3 = []
            D_pos9v5 = []
            D_pos9v11 = []
            D_pos9v13 = []
            for iTrial in range(accuracy[0,iBlock].size):
                # if iSubject == 0 or iSubject == 1 or iSubject == 2:
                #     pos1 = int(stimuli[0,iBlock][0,iTrial])
                #     pos2 = int(stimuli[0,iBlock][2,iTrial])
                # else:
                pos1 = int(stimuli[0,iBlock][1,iTrial])
                pos2 = int(stimuli[0,iBlock][3,iTrial])
                if self.oneChanDiff_top(pos1, pos2):
                    D_pos5v1.append(accuracy[0,iBlock][0,iTrial])
                elif self.zeroChanDiff_top(pos1, pos2):
                    D_pos5v3.append(accuracy[0,iBlock][0,iTrial])
                elif ((pos1 == 5 or pos1 == 6) and (pos2 == 9 or pos2 == 10)):
                    D_pos5v9.append(accuracy[0,iBlock][0,iTrial])
                elif self.twoChanDiff_top(pos1, pos2):
                    D_pos5v11.append(accuracy[0,iBlock][0,iTrial])
                elif self.twoChanDiff_bottom(pos1, pos2):
                    D_pos9v3.append(accuracy[0,iBlock][0,iTrial])
                elif ((pos1 == 9 or pos1 == 10) and (pos2 == 5 or pos2 == 6)):
                    D_pos9v5.append(accuracy[0,iBlock][0,iTrial])
                elif self.zeroChanDiff_bottom(pos1, pos2):
                    D_pos9v11.append(accuracy[0,iBlock][0,iTrial])
                elif self.oneChanDiff_bottom(pos1, pos2):
                    D_pos9v13.append(accuracy[0,iBlock][0,iTrial])

            data.append([stat.mean(D_pos5v1), stat.mean(D_pos5v3), stat.mean(D_pos5v9), stat.mean(D_pos5v11),
                             stat.mean(D_pos9v3), stat.mean(D_pos9v5), stat.mean(D_pos9v11), stat.mean(D_pos9v13)])

            return data

    def calcAccRT(self, accuracy, RT, stimuli, parseBy):
        self.parseData(accuracy, stimuli, 'ACC', parseBy)
        self.parseData(RT, stimuli, 'RT', parseBy)