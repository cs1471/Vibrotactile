import statistics as stat

class Position_general():
    def __init__(self):
        self.RT = [[]]
        self.ACC = [[]]

    def wristPos_Different(self, pos1, pos2):
        if (pos1 == 1 or pos1 == 2 or pos1 == 3 or pos1 == 4 or pos1 == 5 or pos1 == 6)\
            and (pos2 == 1 or pos2 == 2 or pos2 == 3 or pos2 == 4 or pos2 == 5 or pos2 == 6):
            return True
        else:
            return False

    def wristPos_Same(self, pos1, pos2):
         if pos1 == 1 or pos1 == 2 or pos1 == 3 or pos1 == 4:
             return True
         else:
             return False

    def elbowPos_Different(self, pos1, pos2):
        if (pos1 == 9 or pos1 == 10 or pos1 == 11 or pos1 == 12 or pos1 == 13 or pos1 == 14)\
            and (pos2 == 9 or pos2 == 10 or pos2 == 11 or pos2 == 12 or pos2 == 13 or pos2 == 14):
            return True
        else:
            return False

    def elbowPos_Same(self, pos1, pos2):
        if  pos1 == 11 or pos1 == 12 or pos1 == 13 or pos1 == 14:
            return True
        else:
            return False

    def parseRT (self, RT, stimuli):
        for iSubject in range(len(RT)):
            D_wristPos_RT = []
            D_elbowPos_RT = []
            D_crossMidline_RT = []
            S_wristPos_RT = []
            S_elbowPos_RT = []
            S_midline_RT = []
            for iBlock in range(RT[iSubject].size):
                for iTrial in range(RT[iSubject][0,iBlock].size):
                    if iSubject == 0 or iSubject == 1 or iSubject == 2:
                        pos1 = int(stimuli[iSubject][0,iBlock][0,iTrial])
                        pos2 = int(stimuli[iSubject][0,iBlock][2,iTrial])
                    else:
                        pos1 = int(stimuli[iSubject][0,iBlock][1,iTrial])
                        pos2 = int(stimuli[iSubject][0,iBlock][3,iTrial])
                    if pos1 != pos2:
                        if self.wristPos_Different(pos1, pos2) == True:
                            D_wristPos_RT.append(RT[iSubject][0,iBlock][0,iTrial])
                        elif self.elbowPos_Different(pos1, pos2) == True:
                            D_elbowPos_RT.append(RT[iSubject][0,iBlock][0,iTrial])
                        else:
                            D_crossMidline_RT.append(RT[iSubject][0,iBlock][0,iTrial])
                    else:
                        if self.wristPos_Same(pos1, pos2) == True:
                            S_wristPos_RT.append(RT[iSubject][0,iBlock][0,iTrial])
                        elif self.elbowPos_Same(pos1, pos2) == True:
                            S_elbowPos_RT.append(RT[iSubject][0,iBlock][0,iTrial])
                        else:
                            S_midline_RT.append(RT[iSubject][0,iBlock][0,iTrial])

            self.RT.append([stat.mean(D_wristPos_RT), stat.mean(D_crossMidline_RT), stat.mean(D_elbowPos_RT),
                            stat.mean(S_wristPos_RT), stat.mean(S_midline_RT), stat.mean(S_elbowPos_RT)])

    def parseAcc(self, accuracy, stimuli):
        for iSubject in range(len(accuracy)):
            D_wristPos_ACC = []
            D_elbowPos_ACC = []
            D_crossMidline_ACC = []
            S_wristPos_ACC = []
            S_elbowPos_ACC = []
            S_midline_ACC = []
            for iBlock in range(accuracy[iSubject].size):
                for iTrial in range(accuracy[iSubject][0,iBlock].size):
                    if iSubject == 0 or iSubject == 1 or iSubject == 2:
                        pos1 = int(stimuli[iSubject][0,iBlock][0,iTrial])
                        pos2 = int(stimuli[iSubject][0,iBlock][2,iTrial])
                    else:
                        pos1 = int(stimuli[iSubject][0,iBlock][1,iTrial])
                        pos2 = int(stimuli[iSubject][0,iBlock][3,iTrial])
                    if pos1 != pos2:
                        if self.wristPos_Different(pos1, pos2) == True:
                            D_wristPos_ACC.append(accuracy[iSubject][0,iBlock][0,iTrial])
                        elif self.elbowPos_Different(pos1, pos2) == True:
                            D_elbowPos_ACC.append(accuracy[iSubject][0,iBlock][0,iTrial])
                        else:
                            D_crossMidline_ACC.append(accuracy[iSubject][0,iBlock][0,iTrial])
                    else:
                        if self.wristPos_Same(pos1, pos2) == True:
                            S_wristPos_ACC.append(accuracy[iSubject][0,iBlock][0,iTrial])
                        elif self.elbowPos_Same(pos1, pos2) == True:
                            S_elbowPos_ACC.append(accuracy[iSubject][0,iBlock][0,iTrial])
                        else:
                            S_midline_ACC.append(accuracy[iSubject][0,iBlock][0,iTrial])

            self.ACC.append([stat.mean(D_wristPos_ACC), stat.mean(D_crossMidline_ACC), stat.mean(D_elbowPos_ACC),
                                    stat.mean(S_wristPos_ACC), stat.mean(S_midline_ACC), stat.mean(S_elbowPos_ACC)])

    def calcAccRT(self, accuracy, RT, stimuli):
        self.parseAcc(accuracy, stimuli)
        self.parseRT(RT, stimuli)