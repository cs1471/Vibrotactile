import statistics as stat

class Position_catBound():
    def __init__(self):
        self.RT = [[]]
        self.ACC = [[]]

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

    def parseACC(self, accuracy, stimuli):
        for iSubject in range(len(accuracy)):
            D_pos5v1_ACC = []
            D_pos5v3_ACC = []
            D_pos5v9_ACC = []
            D_pos5v11_ACC = []
            D_pos9v3_ACC = []
            D_pos9v5_ACC = []
            D_pos9v11_ACC = []
            D_pos9v13_ACC = []
            for iBlock in range(accuracy[iSubject].size):
                for iTrial in range(accuracy[iSubject][0,iBlock].size):
                    if iSubject == 0 or iSubject == 1 or iSubject == 2:
                        pos1 = int(stimuli[iSubject][0,iBlock][0,iTrial])
                        pos2 = int(stimuli[iSubject][0,iBlock][2,iTrial])
                    else:
                        pos1 = int(stimuli[iSubject][0,iBlock][1,iTrial])
                        pos2 = int(stimuli[iSubject][0,iBlock][3,iTrial])
                    if self.oneChanDiff_top(pos1, pos2):
                        D_pos5v1_ACC.append(accuracy[iSubject][0,iBlock][0,iTrial])
                    elif self.zeroChanDiff_top(pos1, pos2):
                        D_pos5v3_ACC.append(accuracy[iSubject][0,iBlock][0,iTrial])
                    elif ((pos1 == 5 or pos1 == 6) and (pos2 == 9 or pos2 == 10)):
                        D_pos5v9_ACC.append(accuracy[iSubject][0,iBlock][0,iTrial])
                    elif self.twoChanDiff_top(pos1, pos2):
                        D_pos5v11_ACC.append(accuracy[iSubject][0,iBlock][0,iTrial])
                    elif self.twoChanDiff_bottom(pos1, pos2):
                        D_pos9v3_ACC.append(accuracy[iSubject][0,iBlock][0,iTrial])
                    elif ((pos1 == 9 or pos1 == 10) and (pos2 == 5 or pos2 == 6)):
                        D_pos9v5_ACC.append(accuracy[iSubject][0,iBlock][0,iTrial])
                    elif self.zeroChanDiff_bottom(pos1, pos2):
                        D_pos9v11_ACC.append(accuracy[iSubject][0,iBlock][0,iTrial])
                    elif self.oneChanDiff_bottom(pos1, pos2):
                        D_pos9v13_ACC.append(accuracy[iSubject][0,iBlock][0,iTrial])

            self.ACC.append([stat.mean(D_pos5v1_ACC), stat.mean(D_pos5v3_ACC), stat.mean(D_pos5v9_ACC), stat.mean(D_pos5v11_ACC),
                             stat.mean(D_pos9v3_ACC), stat.mean(D_pos9v5_ACC), stat.mean(D_pos9v11_ACC), stat.mean(D_pos9v13_ACC)])

    def parseRT(self, RT, stimuli):
        for iSubject in range(len(RT)):
            D_pos5v1_RT = []
            D_pos5v3_RT = []
            D_pos5v9_RT = []
            D_pos5v11_RT = []
            D_pos9v3_RT = []
            D_pos9v5_RT = []
            D_pos9v11_RT = []
            D_pos9v13_RT = []
            for iBlock in range(RT[iSubject].size):
                for iTrial in range(RT[iSubject][0,iBlock].size):
                    if iSubject == 0 or iSubject == 1 or iSubject == 2:
                        pos1 = int(stimuli[iSubject][0,iBlock][0,iTrial])
                        pos2 = int(stimuli[iSubject][0,iBlock][2,iTrial])
                    else:
                        pos1 = int(stimuli[iSubject][0,iBlock][1,iTrial])
                        pos2 = int(stimuli[iSubject][0,iBlock][3,iTrial])

                    if self.oneChanDiff_top(pos1, pos2) == True:
                        D_pos5v1_RT.append(RT[iSubject][0,iBlock][0,iTrial])
                    elif self.zeroChanDiff_top(pos1, pos2) == True:
                        D_pos5v3_RT.append(RT[iSubject][0,iBlock][0,iTrial])
                    elif ((pos1 == 5 or pos1 == 6) and (pos2 == 9 or pos2 == 10)):
                        D_pos5v9_RT.append(RT[iSubject][0,iBlock][0,iTrial])
                    elif self.twoChanDiff_top(pos1, pos2) == True:
                        D_pos5v11_RT.append(RT[iSubject][0,iBlock][0,iTrial])
                    elif self.twoChanDiff_bottom(pos1, pos2) == True:
                        D_pos9v3_RT.append(RT[iSubject][0,iBlock][0,iTrial])
                    elif ((pos1 == 9 or pos1 == 10) and (pos2 == 5 or pos2 == 6)):
                        D_pos9v5_RT.append(RT[iSubject][0,iBlock][0,iTrial])
                    elif self.zeroChanDiff_bottom(pos1, pos2) == True:
                        D_pos9v11_RT.append(RT[iSubject][0,iBlock][0,iTrial])
                    elif self.oneChanDiff_bottom(pos1, pos2) == True:
                        D_pos9v13_RT.append(RT[iSubject][0,iBlock][0,iTrial])

            self.RT.append([stat.mean(D_pos5v1_RT), stat.mean(D_pos5v3_RT), stat.mean(D_pos5v9_RT), stat.mean(D_pos5v11_RT),
                            stat.mean(D_pos9v3_RT), stat.mean(D_pos9v5_RT), stat.mean(D_pos9v11_RT), stat.mean(D_pos9v13_RT)])

    def calcAccRT(self, accuracy, RT, stimuli):
        self.parseACC(accuracy, stimuli)
        self.parseRT(RT, stimuli)