% Automaticity
function trialOutput = diskAnimalsExperiment_inScanner20150630(name,exptdesign)

try
    % following codes should be used when you are getting key presses using
    % fast routines like kbcheck.
    KbName('UnifyKeyNames');
    Priority(1)

    %settings so that Psychtoolbox doesn't display annoying warnings--DON'T CHANGE
    oldLevel = Screen('Preference', 'VisualDebugLevel', 1);
    %     oldEnableFlag = Screen('Preference', 'SuppressAllWarnings', 1);
    %     warning offc
    HideCursor;

    WaitSecs(1); % make sure it is loaded into memory;
    
    % initialize the random number generator
%     randn('state',sum(100*clock));
% THIS IS NOW DONE IN THE WRAPPER FUNCTION WITH RNG('SHUFFLE')

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %		INITIALIZE EXPERIMENT
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % open a screen and display instructions
    % Choosing the display with the highest display number is
    % a best guess about where you want the stimulus displayed.
    screens = Screen('Screens');
    screenNumber = min(screens);
%     screenNumber = 1;
    % Open window with default settings:
    [w windowRect] = Screen('OpenWindow', screenNumber,[128 128 128]);
%     [w windowRect] = Screen('OpenWindow', screenNumber,[128 128 128], [0 0 800 800]); %for debugging
    white = WhiteIndex(w); % pixel value for white
    black = BlackIndex(w); % pixel value for black
    responseDotSize=20;
    
    %  calculate the slack allowed during a flip interval
    refresh = Screen('GetFlipInterval',w);
    slack = refresh/2;

    % Select specific text font, style and size, unless we're on Linux
    % where this combo is not available:
    if IsLinux==0
        Screen('TextFont',w, 'Courier New');
        Screen('TextSize',w, 14);
        Screen('TextStyle', w, 1+2);
    end;
    
    if exptdesign.netstationPresent
        % Connect to Netstation
        [status error] = NetStation('Connect', exptdesign.netstationIP);
        if status ==1 % there was an error!
            ME = MException('NETSTATION:CouldNotConnect', ['Could not connect to Netstation computer at IP ' exptdesign.netstationIP '.  Please check the IP and network connection and try again.\n  Error:' error]);
            throw(ME);
        end

        % Tell Netstation to synchronize recording
        [status error] = NetStation('Synchronize',exptdesign.netstationSyncLimit);
        if status ==1 % there was an error!
            ME = MException('NETSTATION:CouldNotSync', ['Could not sync with Netstation to allowable limit of ' exptdesign.syncLimit '.  Please check the IP and connection and try again.\n  Error:' error]);
            throw(ME);
        end
    end
    
    centSOA = exptdesign.centSOADurations;
    perifSOA = exptdesign.perifSOADurations;
    % FIXATION IMAGE
    fixationImage = imread(exptdesign.fixationImage);
    % BLANK IMAGE
    blankImage = imread(exptdesign.blankImage);   
    % CUE IMAGE
    cueImage = imread(exptdesign.cueImage, 'png', 'BackgroundColor', [0.5 0.5 0.5]);

    % MAKE TEXTURES
    fixationTexture = Screen('MakeTexture', w, double(fixationImage));
    blankTexture = Screen('MakeTexture', w, double(blankImage));
    cueTexture = Screen('MakeTexture', w, cueImage);

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %		INTRO EXPERIMENT
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    if exptdesign.responseBox
        %flush event cue
        evt=1;
        while ~isempty(evt)
            evt = CMUBox('GetEvent', exptdesign.boxHandle);
        end
        % Get the responses keyed in from subject
        drawAndCenterText(w,'Please press the button for animal.',0);
        evt = CMUBox('GetEvent', exptdesign.boxHandle, 1);
        responseMapping.animal=evt.state;
        drawAndCenterText(w,'Please press the button for no animal.',0);
        evt = CMUBox('GetEvent', exptdesign.boxHandle, 1);
        responseMapping.noAnimal=evt.state;
        drawAndCenterText(w,'Please press the button for red on left.',0);
        evt = CMUBox('GetEvent', exptdesign.boxHandle, 1);
        responseMapping.redLeft=evt.state;
        drawAndCenterText(w,'Please press the button for red on right.',0);
        evt = CMUBox('GetEvent', exptdesign.boxHandle, 1);
        responseMapping.redRight=evt.state;
        % Let the scanner signal the scan to start
        drawAndCenterText(w,'Please get ready.\n\nThe experiment will begin shortly.',0);
        % WARNING: TRRIGGER CORRESPONDS TO A PRESS OF BUTTON 3!!!
        triggername=4;
        trigger=0;
        while ~isequal(triggername,trigger)
            evt = CMUBox('GetEvent', exptdesign.boxHandle, 1);
            trigger = evt.state;
            starttime = evt.time;
        end
        exptdesign.scanStart = starttime;
        exptdesign.responseMapping=responseMapping;
    else
        responseMapping=exptdesign.responseKeyChange;
        drawAndCenterText(w,'Hit Enter to Continue...',1);
        exptdesign.scanStart = GetSecs;
    end
    
    trialCounter=0;

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %		SESSIONS
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    Screen('DrawTexture', w, fixationTexture);
    Screen('Flip',w)
    for sessionNum = 1:length(exptdesign.sessionType);
        sessionSetupStartTime=GetSecs;
   
        % Set up an array to record the number of correct answers
        centCorrectArray = zeros(1,exptdesign.numTrialsPerSession);
        perifCorrectArray = zeros(1,exptdesign.numTrialsPerSession);
        
        %determine whether to display central and/or peripheral task
        if exptdesign.sessionType(sessionNum) == 1
            displayPerif = 0;
            displayCentral = 1;
            cueType=0;
            if exptdesign.responseBox
                drawAndCenterText(w, 'Animals: Animal/No Animal',0,sessionSetupStartTime+10);
            elseif exptdesign.responseKeyChange
                drawAndCenterText(w, 'Animals: Press left for No Animal \n\n Press right for Animal',0,sessionSetupStartTime+10);
            else
                drawAndCenterText(w, 'Animals: Press left for Animal \n\n Press right for No Animal',0,sessionSetupStartTime+10);
            end
        elseif exptdesign.sessionType(sessionNum) == 2
            displayPerif = 1;
            displayCentral = 0;
            cueType=1;
            if exptdesign.responseBox
                drawAndCenterText(w, 'Disk: Red on Left or Right?',0,sessionSetupStartTime+10);
            elseif exptdesign.responseKeyChange
                drawAndCenterText(w, 'Disk: Press 1 for Red on left \n\n Press 2 for Red on right',0,sessionSetupStartTime+10);
            end    
        elseif exptdesign.sessionType(sessionNum) == 3
            displayPerif = 1;
            displayCentral = 1;
            cueType=1;
            if exptdesign.responseBox
                drawAndCenterText(w, 'Disks and Animals simultaneously \n\n First respond to disk (Red on left or right). \n Second respond to Animal/No Animal. \n Always attend to the DISK.',0,sessionSetupStartTime+10);
            elseif exptdesign.responseKeyChange
                drawAndCenterText(w, 'Disks and Animals simultaneously \n\n First respond to disk (Red on left(1) or right(2)). \n Second respond to No Animal(left)/Animal(right). \n Always attend to the DISK.',0,sessionSetupStartTime+10);
            else
                drawAndCenterText(w, 'Disks and Animals simultaneously \n\n First respond to disk (Red on left(1) or right(2)). \n Second respond to Animal(left)/No Animal(right). \n Always attend to the DISK.',0,sessionSetupStartTime+10);
            end
        end
        
        %determine which order to display central/peripheral mask 
	    %uses switch case otherwise below
	    if centSOA < perifSOA
	    	screenOrder=1;
	    elseif centSOA==perifSOA
	    	screenOrder=2;
        else
		    screenOrder=3;
	    end

        % Set up all stimuli, masks, fixation, and blank images
        % PICTURES
        [responseTrial perifallimages, perifstimulustypemarker, perifallimagefiles...
            centallimages, centstimulustypemarker, centallimagefiles] = prepPics(exptdesign,displayPerif,displayCentral);        
        % In practice trials where responses are hard coded, switch when subjects are instructed no animal left/animal right
        if ~exptdesign.responseBox && exptdesign.responseKeyChange
            centstimulustypemarker=double(~centstimulustypemarker);
        end
        
        
        if displayPerif
            % MASK
            [maskimages, maskimagefiles maskorder] = prepPerifMask(exptdesign);
        end
        if displayCentral
            % MASK
            [centmaskimages, centmaskimagefiles] = prepCentMask(exptdesign);
        end
                
        % Tell Netstation to start recording
        if exptdesign.netstationPresent
            [status error] = NetStation('StartRecording');
            if status ==1 % there was an error!
                status;
                error;
                ME = MException('NETSTATION:CouldNotRecord', ['Could not tell Netstation to start recording.  Please check the IP and connection and try again.\n  Error:' error]);
                throw(ME);
            end
            %  Wait for Netstation to Start Recording
            WaitSecs(2);
        end
        
        if GetSecs-sessionSetupStartTime > 12.24 %should make this a varible
            disp('Timing Error: block took longer than 12.24 seconds to load')
        end

        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        %		TRIALS
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        % Set up the output data structure for all trials in this session
        trialOutput(sessionNum).sessionNum = sessionNum;
        trialOutput(sessionNum).cueType=cueType;
        
        for trial = 1:exptdesign.numTrialsPerSession;
            trialCounter=trialCounter+1;
            % Fixation display
            Screen('DrawTexture', w, fixationTexture);
            if exptdesign.netstationPresent
                Screen('FillRect',w,black,[0 0 32 32]);  % This is the stimulus marker block for the photodiode
            end
            [FixationVBLTimestamp FixationOnsetTime FixationFlipTimestamp FixationMissed] = Screen('Flip',w,exptdesign.scanStart + 12.24*sessionNum + 6.12*(trialCounter-1));
            
            %  Set up the trial output data
            trialOutput(sessionNum).trials(trial).trialStartTime= GetSecs;
            trialOutput(sessionNum).trials(trial).numSessions = exptdesign.numSessions;
            trialOutput(sessionNum).trials(trial).sessionIndex = sessionNum;
            trialOutput(sessionNum).trials(trial).numTrials = exptdesign.numTrialsPerSession;
            trialOutput(sessionNum).trials(trial).trialIndex = trial;
            
            [perifLocX, perifLocY] = perifLocation(exptdesign, w);
            
            if exptdesign.responseBox
                %flush event cue
                evt=1;
                while ~isempty(evt)
                    evt = CMUBox('GetEvent', exptdesign.boxHandle);
                end
            end
                        
            %first do the peripheral cue
            if exptdesign.cuePeripheralLocation                
                 %make a cue at the periphery.
                 if cueType
                     Screen('DrawTexture', w, fixationTexture);
                     %Screen('FillOval', w, fixCol,[perifLocX perifLocY perifLocX+fixDotSize perifLocY+fixDotSize]);
                     Screen('DrawTexture', w, cueTexture, [], [perifLocX perifLocY perifLocX+exptdesign.perifWdth perifLocY + exptdesign.perifHt]);
                     [cueVBLTimestamp cueOnsetTime cueFlipTimestamp cueMissed] = Screen('Flip',w, FixationVBLTimestamp + exptdesign.fixationDuration - slack);
                     Screen('DrawTexture', w, fixationTexture);
                     [Fixation2VBLTimestamp Fixation2OnsetTime Fixation2FlipTimestamp Fixation2Missed] = Screen('Flip',w, cueVBLTimestamp + exptdesign.cueDuration - slack);
                 end
                 
            end
            
            if displayCentral && displayPerif %dual task trials
                %put the central AND peripheral up for 2 frames
                correctCentResponse = centstimulustypemarker(trial);
                stimulusTexture = Screen('MakeTexture', w, squeeze(centallimages(trial,:,:,:)));
                Screen('DrawTexture', w, stimulusTexture)
                drawPics(exptdesign, w, perifallimages, trial, perifLocX, perifLocY);
                if exptdesign.cuePeripheralLocation %give stimulus relative to second fixation
                    if cueType
                        [CentStimulusVBLTimestamp CentStimulusOnsetTime CentStimulusFlipTimestamp CentStimulusMissed] = Screen('Flip',w,Fixation2VBLTimestamp + exptdesign.fixation2Duration - slack);
                    end
                else
                    [CentStimulusVBLTimestamp CentStimulusOnsetTime CentStimulusFlipTimestamp CentStimulusMissed] = Screen('Flip',w,FixationVBLTimestamp + exptdesign.fixationDuration - slack);
                end
                PerifStimulusVBLTimestamp = CentStimulusVBLTimestamp;
                PerifStimulusOnsetTime = CentStimulusOnsetTime;
                PerifStimulusFlipTimestamp = CentStimulusFlipTimestamp;
                PerifStimulusMissed = CentStimulusMissed;
                   
                %blank center and peripheral both after perifStimulusDuration (2 frames)
                Screen('DrawTexture', w, blankTexture);
                [BlankPerifVBLTimestamp BlankPerifOnsetTime BlankPerifFlipTimestamp BlankPerifMissed] = Screen('Flip',w,PerifStimulusVBLTimestamp + exptdesign.perifStimulusDuration - slack);

                switch screenOrder
                    case 1 
                        %central mask on after central SOA 
                        stimulusTexture = Screen('MakeTexture', w, squeeze(centmaskimages(trial,:,:,:)));
                        Screen('DrawTexture', w, stimulusTexture)
                        [CentMaskVBLTimestamp CentMaskOnsetTime CentMaskFlipTimestamp CentMaskMissed] = Screen('Flip',w,CentStimulusVBLTimestamp + centSOA - slack);
                
                        %peripheral mask on after peripheral SOA, rewrite Central Mask too
                        drawPerifMask(exptdesign, w, perifLocX, perifLocY, trial, maskimages);
                        stimulusTexture = Screen('MakeTexture', w, squeeze(centmaskimages(trial,:,:,:)));
                        Screen('DrawTexture', w, stimulusTexture)
                        [PerifMaskVBLTimestamp PerifMaskOnsetTime PerifMaskFlipTimestamp PerifMaskMissed] = Screen('Flip',w,PerifStimulusVBLTimestamp + perifSOA - slack);
                    case 2 
                        %central and peripheral masks on at the same time
                        drawPerifMask(exptdesign, w, perifLocX, perifLocY, trial, maskimages);
                        stimulusTexture = Screen('MakeTexture', w, squeeze(centmaskimages(trial,:,:,:)));
                        Screen('DrawTexture', w, stimulusTexture)
                        [PerifMaskVBLTimestamp PerifMaskOnsetTime PerifMaskFlipTimestamp PerifMaskMissed] = Screen('Flip',w,PerifStimulusVBLTimestamp + perifSOA - slack);
                        CentMaskVBLTimestamp=PerifMaskVBLTimestamp;
                        CentMaskOnsetTime=PerifMaskOnsetTime;
                        CentMaskFlipTimestamp=PerifMaskFlipTimestamp;
                        CentMaskMissed=PerifMaskMissed;
                    case 3 
                        %peripheral mask on after peripheral SOA
                        drawPerifMask(exptdesign, w, perifLocX, perifLocY, trial, maskimages);
                        [PerifMaskVBLTimestamp PerifMaskOnsetTime PerifMaskFlipTimestamp PerifMaskMissed] = Screen('Flip',w,PerifStimulusVBLTimestamp + perifSOA - slack);
                        
                        %central mask on after central SOA, rewrite peripheral mask too
                        drawPerifMask(exptdesign, w, perifLocX, perifLocY, trial, maskimages);
                        stimulusTexture = Screen('MakeTexture', w, squeeze(centmaskimages(trial,:,:,:)));
                        Screen('DrawTexture', w, stimulusTexture)
                        [CentMaskVBLTimestamp CentMaskOnsetTime CentMaskFlipTimestamp CentMaskMissed] = Screen('Flip',w,CentStimulusVBLTimestamp + centSOA - slack);
                end
            elseif displayCentral && ~displayPerif %center-only trials
                %put the center for 2 frames
                correctCentResponse = centstimulustypemarker(trial);
                stimulusTexture = Screen('MakeTexture', w, squeeze(centallimages(trial,:,:,:)));
                Screen('DrawTexture', w, stimulusTexture)

                [CentStimulusVBLTimestamp CentStimulusOnsetTime CentStimulusFlipTimestamp CentStimulusMissed] = Screen('Flip',w,FixationVBLTimestamp + exptdesign.fixationDuration + exptdesign.cueDuration + exptdesign.fixation2Duration - slack);
   
                %blank 
                Screen('DrawTexture', w, blankTexture);
                %yes that latency is the perifStimulusDuration (for case of both 2 refreshes)
                [BlankPerifVBLTimestamp BlankPerifOnsetTime BlankPerifFlipTimestamp BlankPerifMissed] = Screen('Flip',w,CentStimulusVBLTimestamp + exptdesign.perifStimulusDuration - slack);

                %central mask on after central SOA 
                stimulusTexture = Screen('MakeTexture', w, squeeze(centmaskimages(trial,:,:,:)));
                Screen('DrawTexture', w, stimulusTexture)
                [CentMaskVBLTimestamp CentMaskOnsetTime CentMaskFlipTimestamp CentMaskMissed] = Screen('Flip',w,CentStimulusVBLTimestamp + centSOA - slack);
                
            elseif ~displayCentral && displayPerif %perif-only trials
                %put peripheral 2 frames
                drawPics(exptdesign, w, perifallimages, trial, perifLocX, perifLocY);
                if exptdesign.cuePeripheralLocation %give stimulus relative to second fixation
                    if cueType
                          [PerifStimulusVBLTimestamp PerifStimulusOnsetTime PerifStimulusFlipTimestamp PerifStimulusMissed] = Screen('Flip',w,Fixation2VBLTimestamp + exptdesign.fixation2Duration - slack);
                    end
                else
                    [PerifStimulusVBLTimestamp PerifStimulusOnsetTime PerifStimulusFlipTimestamp PerifStimulusMissed] = Screen('Flip',w,FixationVBLTimestamp + exptdesign.fixationDuration - slack);
                end
                   
                %blank 
                Screen('DrawTexture', w, blankTexture);
                [BlankPerifVBLTimestamp BlankPerifOnsetTime BlankPerifFlipTimestamp BlankPerifMissed] = Screen('Flip',w,PerifStimulusVBLTimestamp + exptdesign.perifStimulusDuration - slack); %+ perifSOA - slack);

                %peripheral mask
                drawPerifMask(exptdesign, w, perifLocX, perifLocY, trial, maskimages);
                [PerifMaskVBLTimestamp PerifMaskOnsetTime PerifMaskFlipTimestamp PerifMaskMissed] = Screen('Flip',w,PerifStimulusVBLTimestamp + perifSOA - slack);
            end
            
            % get the subjects response if it is a response trial
            if responseTrial(trial)
                % display the response prompt
                responseDotRect = CenterRect([0 0 responseDotSize responseDotSize], windowRect);
                Screen('FillOval', w, [0 0 255], responseDotRect)
                if displayPerif
                    [ResponseCueVBLTimestamp ResponseCueOnsetTime ResponseCueFlipTimestamp ResponseCueMissed] = Screen( 'Flip',w,PerifMaskVBLTimestamp + exptdesign.maskDuration-slack);
                elseif displayCentral
                    [ResponseCueVBLTimestamp ResponseCueOnsetTime ResponseCueFlipTimestamp ResponseCueMissed] = Screen( 'Flip',w,CentMaskVBLTimestamp + perifSOA -centSOA + exptdesign.maskDuration-slack);
                end
                
                % Record the response of the subject
                PerifResponseStartTime = GetSecs;
                if displayPerif
                    if exptdesign.waitForPerifResponse
                        numericalanswerPerif = getPerifResponseWait(exptdesign,responseMapping);
                    else
                        numericalanswerPerif = getPerifResponse(exptdesign.responseDuration,exptdesign,responseMapping);
                    end
                    trialOutput(sessionNum).trials(trial).subjectPerifResponse = numericalanswerPerif;
                end
                PerifResponseFinishedTime = GetSecs;
                
                if displayCentral
                    CentResponseStartTime = GetSecs;
                    if exptdesign.waitForCentResponse
                        numericalanswerCent = getCentResponseWait(exptdesign,responseMapping);
                    else
                        numericalanswerCent = getCentResponse(exptdesign.responseDuration-(PerifResponseFinishedTime-PerifResponseStartTime),exptdesign,responseMapping);
                    end
                    CentResponseFinishedTime = GetSecs;
                    trialOutput(sessionNum).trials(trial).subjectCentResponse = numericalanswerCent;
                end    
            else
                Screen('DrawTexture', w, fixationTexture);
                if displayPerif
                    [FixationNoResponseVBLTimestamp FixationNoResponseOnsetTime FixationNoResponseFlipTimestamp FixationNoResponseMissed] = Screen( 'Flip',w,PerifMaskVBLTimestamp + exptdesign.maskDuration-slack);
                elseif displayCentral
                    [FixationNoResponseVBLTimestamp FixationNoResponseOnsetTime FixationNoResponseFlipTimestamp FixationNoResponseMissed] = Screen( 'Flip',w,CentMaskVBLTimestamp + perifSOA -centSOA + exptdesign.maskDuration-slack);
                end
            end
                        
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            %    TRIAL OUTPUTS
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            %  Record the end time for the trial
            trialOutput(sessionNum).trials(trial).trialEndTime = GetSecs;
            trialOutput(sessionNum).trials(trial).responseTrial = responseTrial(trial);

            if displayPerif
                % PERIPHERAL TASK DATA
                % Record whether the subject got the right answer
                trialOutput(sessionNum).trials(trial).correctPerifResponse = perifstimulustypemarker(trial);
                if responseTrial(trial)
                    trialOutput(sessionNum).trials(trial).subjectHasRightPerifAnswer = trialOutput(sessionNum).trials(trial).correctPerifResponse == trialOutput(sessionNum).trials(trial).subjectPerifResponse;
                    trialOutput(sessionNum).trials(trial).PerifResponseStart = PerifResponseStartTime;
                    trialOutput(sessionNum).trials(trial).PerifResponseFinished = PerifResponseFinishedTime;
                end
                
                trialOutput(sessionNum).trials(trial).fixationDuration = PerifStimulusOnsetTime - FixationOnsetTime;  % record the actual time on screen (just to be accurate)
                
                % Record the filenames used for stimulus and masks
                trialOutput(sessionNum).trials(trial).perifstimulusImageFile = perifallimagefiles(trial).name;
                trialOutput(sessionNum).trials(trial).perifMaskImageFile = maskimagefiles(maskorder(trial)).name;
                trialOutput(sessionNum).trials(trial).perifMaskImageType = maskorder(trial);
                trialOutput(sessionNum).trials(trial).perifXLocation = perifLocX;
                trialOutput(sessionNum).trials(trial).perifYLocation = perifLocY;

                trialOutput(sessionNum).trials(trial).perifStimulusOnset = PerifStimulusOnsetTime;
                trialOutput(sessionNum).trials(trial).perifStimulusDuration = PerifMaskOnsetTime - PerifStimulusOnsetTime;  % record the actual time on the screen (just to be accurate)

                trialOutput(sessionNum).trials(trial).perifStimulusMissed = PerifStimulusMissed;
                trialOutput(sessionNum).trials(trial).perifMaskMissed = PerifMaskMissed;
                trialOutput(sessionNum).trials(trial).blankPerifMissed = BlankPerifMissed;
                

            end
            
            if displayCentral

                % Record the trial type data
                %trialOutput(sessionNum).trials(trial).letterPostions = lettersDrawn;
                %trialOutput(sessionNum).trials(trial).spinAngle = spinAngle;
                %trialOutput(sessionNum).trials(trial).trialType = ltChosen;

                % CENTRAL TASK DATA
                % Record whether the subject got the right answer
                trialOutput(sessionNum).trials(trial).correctCentResponse = correctCentResponse;
                if responseTrial(trial)
                    trialOutput(sessionNum).trials(trial).subjectHasRightCentAnswer = trialOutput(sessionNum).trials(trial).correctCentResponse == trialOutput(sessionNum).trials(trial).subjectCentResponse;
                    trialOutput(sessionNum).trials(trial).CentResponseStart = CentResponseStartTime;
                    trialOutput(sessionNum).trials(trial).CentResponseFinished = CentResponseFinishedTime;
                end
                
                trialOutput(sessionNum).trials(trial).fixationDuration = CentStimulusOnsetTime - FixationOnsetTime;  % record the actual time on screen (just to be accurate)

                trialOutput(sessionNum).trials(trial).centStimulusOnset = CentStimulusOnsetTime;
                trialOutput(sessionNum).trials(trial).centStimulusDuration = CentMaskOnsetTime - CentStimulusOnsetTime;  % record the actual time on screen (just to be accurate)

                trialOutput(sessionNum).trials(trial).centStimulusMissed = CentStimulusMissed;
                trialOutput(sessionNum).trials(trial).centMaskMissed = CentMaskMissed;
                trialOutput(sessionNum).trials(trial).blankPerifMissed = BlankPerifMissed;
                trialOutput(sessionNum).trials(trial).centstimulusImageFile = centallimagefiles(trial).name;
                trialOutput(sessionNum).trials(trial).centMaskImageFile = centmaskimagefiles(trial).name;
            end
            
            % Calculate and record trial timing
            trialOutput(sessionNum).trials(trial).fixationOnset = FixationOnsetTime;
            trialOutput(sessionNum).trials(trial).fixationMissed = FixationMissed;
            trialOutput(sessionNum).trials(trial).centSOA = centSOA;
            trialOutput(sessionNum).trials(trial).perifSOA = perifSOA;
            trialOutput(sessionNum).centSOA=centSOA;
            trialOutput(sessionNum).perifSOA=perifSOA;
            trialOutput(sessionNum).trials(trial).blankPerifOnsetRime = BlankPerifOnsetTime;
            if responseTrial(trial)
                trialOutput(sessionNum).trials(trial).ResponseCueOnsetime = ResponseCueOnsetTime;
                trialOutput(sessionNum).trials(trial).responseCueTiming = ResponseCueOnsetTime - BlankPerifOnsetTime;
            end
                        
            % If the trial is the last one of the session, calculate the percentage of
            % trials the subject answered correctly.
            if trial == exptdesign.numTrialsPerSession
                 numCentCorrect = length(find(centCorrectArray==1));
                 trialOutput(sessionNum).centPerformance = numCentCorrect / exptdesign.numTrialsPerSession
   
                 numPerifCorrect = length(find(perifCorrectArray==1));
                 trialOutput(sessionNum).perifPerformance = numPerifCorrect / exptdesign.numTrialsPerSession
            end           
        end        
        
        if exptdesign.netstationPresent
            %  Tell Netstation to Stop Recording
            [status error] = NetStation('StopRecording');
            if status ==1 % there was an error!
                status;
                error;
                ME = MException('NETSTATION:CouldNotStopRecording', ['Could not tell Netstation to stop recording.  Please check the IP and connection and try again.\n  Error:' error]);
                throw(ME);
            end
        end
 
    end
    Screen('DrawTexture', w, fixationTexture);
    Screen('Flip',w)
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %		END
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    %  Write the trial specific data to the output file.
    tic;
    save(['./Animal_data_inScanner/' exptdesign.subjectName '/' exptdesign.subjectName '.' num2str(exptdesign.run) '.' num2str(trial) '.mat'],'trialOutput','exptdesign');
    toc;

    WaitSecs('UntilTime',exptdesign.scanStart + 12.24*(sessionNum+1) + 6.12*(trialCounter))
    % End of experiment, close window:
    Screen('CloseAll');
    Priority(0);
    % At the end of your code, it is a good idea to restore the old level.
    %     Screen('Preference','SuppressAllWarnings',oldEnableFlag);

    catch
    % This "catch" section executes in case of an error in the "try"
    % section []
    if exptdesign.netstationPresent
        % Tell Netstation to stop recording
        [status error] = NetStation('StopRecording');
        if status ==1 % there was an error!
            status;
            error;
            ME = MException('NETSTATION:CouldNotStopRecord', ['Could not tell Netstation to stop recording.  Please check the IP and connection and try again.\n  Error:' error]);
            %              throw(ME);
            disp('ERROR stopping recoring in Netstation!');
        end

        [status error] = NetStation('Disconnect');
        if status ==1 % there was an error!
            status;
            error;
            ME = MException('NETSTATION:CouldNotStopRecord', ['Could not tell Netstation to stop recording.  Please check the IP and connection and try again.\n  Error:' error]);
            %              throw(ME);
            disp('ERROR disconnecting from Netstation!');

        end
    end
    
    if exptdesign.responseBox
        CMUBox('Close',exptdesign.boxHandle);
    end
    
    % above.  Importantly, it closes the onscreen window if it's open.
    disp('Caught error and closing experiment nicely....');
    Screen('CloseAll');
    Priority(0);
    fclose('all');
    psychrethrow(psychlasterror);

end
end


 
% Loads the images for the peripheral masks
function [maskimages, maskimagefiles, maskorder] = prepPerifMask(exptdesign)

maskimagefiles = dir(exptdesign.maskImages);
if (size(maskimagefiles,1) == 0)
    disp('NO MASK IMAGES!!!!');
    ME = MException('VerifyInput:OutOfBounds', ['NO MASK IMAGES FOUND AT ' exptdesign.cat1Images]);
    throw(ME);
end

% MASKS
%maskimagefiles = maskimagefiles(randperm(size(maskimagefiles,1)));
maskimages = loadimages_png(exptdesign.imageDirectory,maskimagefiles(1:2));
maskimages = repmat(maskimages, [round(exptdesign.numTrialsPerSession/2), 1, 1, 1]);
maskpermute = randperm(size(maskimages,1));
maskorder=repmat([1 2], 1, round(exptdesign.numTrialsPerSession/2));
maskorder=maskorder(maskpermute);
maskimages = maskimages(maskpermute,:,:,:);
end


% Makes and Draws the peripheral mask textures
%
% INPUT:    exptdesign and window are basic information provided by the
%           main function
%           perifLocX - the x coordinate of the peripheral stimulus
%           perifLocY - the y coordinate of the peripheral stimulus
%           trial - the trial number
%           maskimages - a randomly permutated vector of masking images
%
% OUTPUT:   none!!! (the function is used to draw the masking images)
function drawPerifMask(exptdesign, window, perifLocX, perifLocY, trial, maskimages)
%  Make all of the textures and data needed for this trial
maskTexture = Screen('MakeTexture', window, squeeze(maskimages(trial,:,:,:)));

Screen('DrawTexture', window, maskTexture, [], [perifLocX perifLocY perifLocX + exptdesign.perifWdth perifLocY + exptdesign.perifHt])
end


% Makes and draws the letter textures
%
% INPUT:    exptdesign and window are basic variables created by the main
%           function
%           letterT/letterL - the images of the letters loaded using the loadimages
%           function
%           ltChosen - determines whether an L or T s drawn
%           spinAngle - determines the angle that the letter is to be
%           rotated
%           letters - a 5-unit array of 1's and 0's that determines whether
%           a T or L is drawn at a particular location
%           lettersDrawn - determines which 5 of the 9 positions are chosen
%           for the letters
%           (ltChosen, spinAngle, letters, and lettersDrawn are all
%           varialbes that are useed as both inputs and outputs so that the
%           letters can be redrawn later in the same place as before)
%
% OUTPUT:   correctCentResponse - records what the correct response is
function [correctCentResponse, spinAngle, lettersDrawn, ltChosen, different, letters] = drawLetters(exptdesign, window, letterT, letterL, ltChosen, spinAngle,letters,lettersDrawn)
%  Make all of the textures and data needed for this trial
tTexture = Screen('MakeTexture', window, letterT);
lTexture = Screen('MakeTexture', window, letterL);
white = WhiteIndex(window); % pixel value for white

if nargin < 6
    % Add some random degrees to spin the letters...
    spinAngle = [rand*360 rand*360 rand*360 rand*360 rand*360];
end

% Read in the ht/wdth of the letters...
letterDim = exptdesign.letterDim;

% Choose which letters are drawn and whether they are all t's, l's
% or both
if nargin < 8
    lettersDrawn = choose(9,5);
end

% Determine whether (1) all T's, (2) 4 T's and 1 L, (3) 4 L's and 1 T, or
% (4) all L's appear on the screen
if nargin < 5
    different = -1;
    ltChosen = choose(4,1);
    if ltChosen == 1
        letters = zeros(1,5);
        correctCentResponse = 0;

    elseif ltChosen == 2
        letters = zeros(1,5);
        letters(choose(5,1)) = 1;
        different = find(letters == 1);
        correctCentResponse = 1;

    elseif ltChosen == 3
        letters = ones(1,5);
        letters(choose(5,1)) = 0;
        different = find(letters == 0);
        correctCentResponse = 1;

    elseif ltChosen == 4;
        letters = ones(1,5);
        correctCentResponse = 0;
    end
end

%determine whether to draw the five letters to the screen

    % Draw the five letters to the screen
    count = 5;
    while count > 0
        % Use another function to determine the position of the 5 letters
        xPos = findLetterPosition(window, lettersDrawn(count), 0, exptdesign);
        yPos = findLetterPosition(window, lettersDrawn(count), 1, exptdesign);

        % Draw either (1) a T or (2) an L on the screen
        if letters(count) == 0
            Screen('DrawTexture', window, tTexture, [], [xPos yPos xPos+letterDim yPos+letterDim], spinAngle(count))
        elseif letters(count) == 1
            Screen('DrawTexture', window, lTexture, [], [xPos yPos xPos+letterDim yPos+letterDim], spinAngle(count))
        end
        count = count - 1;
    end
%     if exptdesign.netstationPresent
%         Screen('FillRect',window,white,[0 0 32 32]);  % This is the stimulus marker block for the photodiode
%     end

end

function [correctCentResponse, spinAngle, lettersDrawn, ltChosen, different, letters] = generateLetters(ltChosen, spinAngle,letters,lettersDrawn)

if nargin < 2
    % Add some random degrees to spin the letters...
    spinAngle = [rand*360 rand*360 rand*360 rand*360 rand*360];
end

% Choose which letters are drawn and whether they are all t's, l's
% or both
if nargin < 4
    lettersDrawn = choose(9,5);
end

% Determine whether (1) all T's, (2) 4 T's and 1 L, (3) 4 L's and 1 T, or
% (4) all L's appear on the screen
if nargin < 1
    different = -1;
    ltChosen = choose(4,1);
    if ltChosen == 1
        letters = zeros(1,5);
        correctCentResponse = 0;

    elseif ltChosen == 2
        letters = zeros(1,5);
        letters(choose(5,1)) = 1;
        different = find(letters == 1);
        correctCentResponse = 1;

    elseif ltChosen == 3
        letters = ones(1,5);
        letters(choose(5,1)) = 0;
        different = find(letters == 0);
        correctCentResponse = 1;

    elseif ltChosen == 4;
        letters = ones(1,5);
        correctCentResponse = 0;
    end
end

end


% Function takes input from the "drawLetters" function and outputs a
% randomly chosen position for the letter to be drawn in
%
% INPUT:    window and exptdesign are basic variables created by the main function
%           numPos - designates one of the nine possible positions for the
%           letters to appear at
%           xory - determines whether the function finds the x or the y
%           coordinate of the letter to be drawn
%
% OUTPUT:   none!!!
function position = findLetterPosition(window, numPos, xory, exptdesign)
% Read in the ht/wdth of the letters...
letterDim = exptdesign.letterDim;

% Caclulate the radius of the circle to be formed by the
% spinning letters....
rad = sqrt(2*((letterDim/2)^2));

[windowWdth windowHt] = Screen('WindowSize', window);
if xory == 0;
    posArrayX = [windowWdth/2 windowWdth/2 - 1.25*rad windowWdth/2 + 1.25*rad windowWdth/2 + 2.5*rad windowWdth/2 + 2.5*rad windowWdth/2 + 1.25*rad windowWdth/2 - 1.25*rad windowWdth/2 - 2.5*rad windowWdth/2 - 2.5*rad];
    position = posArrayX(numPos);
elseif xory == 1;
    posArrayY = [windowHt/2 windowHt/2 - 2.5*rad windowHt/2 - 2.5*rad windowHt/2 - 1.25*rad windowHt/2 + 1.25*rad windowHt/2 + 2.5*rad windowHt/2 + 2.5*rad windowHt/2 + 1.25*rad windowHt/2 - 1.25*rad];
    position = posArrayY(numPos);
end
end


% Draws the central mask (the letter F) in the same positions and
% orientations as  the stimuli
%
% INPUT:    exptdesign and window are basic variables provided by the main
%           function
%           letterF - the image of the letterF to be used as the masking
%           image
%           spinAngle -  the angles that the original central stimuli were
%           rotated by
%           lettersDrawn -  the 5 positions that the stimuli were drawn at
function drawCentMask(exptdesign, window, letterF, spinAngle, lettersDrawn)
fTexture = Screen('MakeTexture', window, letterF);
% Read in the ht/wdth of the letters...
letterDim = exptdesign.letterDim;

% Draw the five letters to the screen
count = 5;
while count > 0
    xPos = findLetterPosition(window, lettersDrawn(count), 0, exptdesign);
    yPos = findLetterPosition(window, lettersDrawn(count), 1, exptdesign);
    Screen('DrawTexture', window, fTexture, [], [xPos yPos xPos+letterDim yPos+letterDim], spinAngle(count) + 180)
    count = count - 1;
end
end


% Calls another function to load the pictures.  Puts the target and
% distractor images into a vector and mixes the drink.  Outputs a permuted
% list of randomly chosen and ordered targets and distractors.
%
% INPUT:    exptdesign...nuff said
%
% OUTPUT:   perifallimages - the permuted vector of targets and distractors
%           perifstimulustypemarker - tells the function whether each image is a
%           target or a distractor.  
%           centallimages - the permuted vector of targets and distractors
%           centstimulustypemarker - tells the function whether each image is a
%           target or a distractor
 function [responseTrial perifallimages, perifstimulustypemarker, perifallimagefiles...
     centallimages, centstimulustypemarker, centallimagefiles]= prepPics(exptdesign,displayPerif,displayCentral)
 
 perifallimages=[];
 perifstimulustypemarker=[];
 perifallimagefiles=[];
 centallimages=[];
 centstimulustypemarker=[];
 centallimagefiles=[];
 

permutation = randperm(exptdesign.numTrialsPerSession);
if displayPerif
    cat1files = dir(exptdesign.cat1Images);
    if (size(cat1files,1) == 0)
        disp('NO PERIF CATEGORY 1 IMAGES!!!!');
        ME = MException('VerifyInput:OutOfBounds', ['NO CATEGORY 1 IMAGES FOUND AT ' exptdesign.cat1Images]);
        throw(ME);
    end

    cat2files = dir(exptdesign.cat2Images);
    if (size(cat2files,1) == 0)
        disp('NO PERIF CATEGORY 2 IMAGES!!!!');
        ME = MException('VerifyInput:OutOfBounds', ['NO CATEGORY 2 IMAGES FOUND AT ' exptdesign.cat2Images]);
        throw(ME);
    end

    % Load and randomize first images and second category images
    % Peripheral CATEGORY 1
    cat1Images = loadimages_png(exptdesign.cat1Directory,cat1files);
 
    % Peripheral CATEGORY 2
    cat2Images = loadimages_png(exptdesign.cat2Directory,cat2files);

    % Put all the PERIPHERAL CATEGORY 1 and CATEGORY 2 in one vector and permute it
    perifstimulustypemarker = [ones(1,exptdesign.numCat1PerSession) zeros(1,exptdesign.numCat2PerSession)];
    perifstimulustypemarker = perifstimulustypemarker(permutation);

    clear perifallimagefiles;
    clear perifallimages perifallimages2;
    perifallimagefiles(:,1) = repmat(cat1files, 1, exptdesign.numCat1PerSession);
    perifallimagefiles(exptdesign.numCat1PerSession+1:exptdesign.numCat1PerSession+exptdesign.numCat2PerSession,1) = repmat(cat2files, 1, exptdesign.numCat2PerSession);
    perifallimagefiles = perifallimagefiles(permutation,1);

    perifallimages(:,:,:,:) = repmat(cat1Images, [exptdesign.numCat1PerSession, 1, 1, 1]);
    perifallimages2(:,:,:,:) = repmat(cat2Images, [exptdesign.numCat2PerSession, 1, 1, 1]);
    perifallimages = cat(1, perifallimages, perifallimages2);
    perifallimages = perifallimages(permutation,:,:,:);
end

if displayCentral
    ctrCat1files = dir(exptdesign.ctrCat1Images);
    if (size(ctrCat1files,1) == 0)
        disp('NO CENTER CATEGORY 1 IMAGES!!!!');
        ME = MException('VerifyInput:OutOfBounds', ['NO CATEGORY 1 IMAGES FOUND AT ' exptdesign.ctrCat1Images]);
        throw(ME);
    end

    ctrCat2files = dir(exptdesign.ctrCat2Images);
    if (size(ctrCat2files,1) == 0)
        disp('NO CATEGORY 2 IMAGES!!!!');
        ME = MException('VerifyInput:OutOfBounds', ['NO CATEGORY 2 IMAGES FOUND AT ' exptdesign.ctrCat2Images]);
        throw(ME);
    end

    % Load and randomize first images and second category images
    % Central CATEGORY 1
    ctrCat1Images = loadimages(exptdesign.cat1Directory,ctrCat1files(1:exptdesign.numCat1PerSession));
    % Peripheral CATEGORY 2
    ctrCat2Images = loadimages(exptdesign.cat2Directory,ctrCat2files(1:exptdesign.numCat2PerSession));

    %  Put all the PERIPHERAL CATEGORY 1 and CATEGORY 2 in one vector and permute it
    centstimulustypemarker = zeros(1,exptdesign.numTrialsPerSession);
    centstimulustypemarker(1:2:exptdesign.numTrialsPerSession)=1;
    centstimulustypemarker = centstimulustypemarker(permutation);

    clear centallimagefiles;
    clear centallimages;
    centallimagefiles(1:2:exptdesign.numTrialsPerSession,1) = ctrCat1files(1:exptdesign.numCat1PerSession,1);
    centallimagefiles(2:2:exptdesign.numTrialsPerSession,1) = ctrCat2files(1:exptdesign.numCat2PerSession,1);
    centallimagefiles = centallimagefiles(permutation,1);
                     
    centallimages(1:2:exptdesign.numTrialsPerSession,:,:,:) = ctrCat1Images(:,:,:,:);
    centallimages(2:2:exptdesign.numTrialsPerSession,:,:,:) = ctrCat2Images(:,:,:,:);
    centallimages = centallimages(permutation,:,:,:);
end

responseTrial = zeros(1,exptdesign.numTrialsPerSession);
responseTrial([1:exptdesign.numTrialsPerSession/8,exptdesign.numTrialsPerSession/2+1:exptdesign.numTrialsPerSession/2+exptdesign.numTrialsPerSession/8])=1;
responseTrial=responseTrial(permutation);
 end


% Draw the peripheral stimuli to the screen at a random location on an
% imaginary circle surrounding the central stimulus
%
% INPUT:    exptdesign and window are basic variables provided by the
%           function
%           allimages - the permuted vector of target and distractor
%           images
%           trial -  the trial number
%
%OUTPUT:    perifLocX/perifLocY - the X and Y coordinates of the peripheral
%           stimuli
function [perifLocX, perifLocY] = perifLocation(exptdesign, window)
    %for repeat = 1:360;
    windowRect = Screen('Rect',window);

    % Get me the info on the screen...
    [windowWdth windowHt] = Screen('WindowSize', window);

    %  calculate the center of the screen and pic, for later reference
    centerScr = [(windowRect(3)-windowRect(1))/2 (windowRect(4)-windowRect(2))/2];
    centerPic = [exptdesign.perifWdth/2 exptdesign.perifHt/2];

    %rotate = repeat;
    rotate = rand*2*pi;

    perifLocX = centerScr(1) + windowHt/3 * cos(rotate) - centerPic(1);
    perifLocY = centerScr(2) + windowHt/3 * sin(rotate) - centerPic(2);

end


function drawPics(exptdesign, window, perifallimages, trial, perifLocX, perifLocY)

    stimulusTexture = Screen('MakeTexture', window, squeeze(perifallimages(trial,:,:,:)));
    % Draw the peripheral stimuli
    Screen('DrawTexture', window, stimulusTexture, [], [perifLocX perifLocY perifLocX + exptdesign.perifWdth perifLocY + exptdesign.perifHt])
    Screen('Close', stimulusTexture);

end


% Waits for and records the peripheral response of the subject
function numericalanswerPerif = getPerifResponseWait(exptdesign, responseMapping)
numericalanswerPerif = -1;
while numericalanswerPerif == -1
    if exptdesign.responseBox
        evt = CMUBox('GetEvent', exptdesign.boxHandle);
        if ~isempty(evt)
            response=evt.state;
            if response == responseMapping.redLeft
                numericalanswerPerif = 1;
            elseif response == responseMapping.redRight
                numericalanswerPerif = 0;
            else
                numericalanswerPerif = -1;
            end
        end
    else
        [secs, keyCode] = KbPressWait;
        numericalanswerPerif = translateKeyPerifResponse(keyCode);
    end
end
end


% Waits for and records the subject's central response
function numericalanswerCent = getCentResponseWait(exptdesign,responseMapping)
numericalanswerCent = -1;
while numericalanswerCent == -1
    if exptdesign.responseBox
        evt = CMUBox('GetEvent', exptdesign.boxHandle);
        if ~isempty(evt)
            response=evt.state;
            if response == responseMapping.animal
                numericalanswerCent = 1;
            elseif response == responseMapping.noAnimal
                numericalanswerCent = 0;
            else
                numericalanswerCent = -1;
            end
        end
    else
        [secs, keyCode] = KbPressWait;
        numericalanswerCent = translateKeyCentResponse(keyCode);
    end
end
end



% Record the subject's peripheral response if it occurs before waitTime
function numericalanswerPerif = getPerifResponse(waitTime,exptdesign, responseMapping)
%Wait for a response
numericalanswerPerif = -1;
keyPressed = 0;
startWaitingPerif=GetSecs;
while GetSecs-startWaitingPerif < waitTime && keyPressed == 0
   if exptdesign.responseBox
       evt = CMUBox('GetEvent', exptdesign.boxHandle);
       if ~isempty(evt)
           response=evt.state;
            if response == responseMapping.redLeft %Left
                numericalanswerPerif = 1;
                keyPressed = 1;
            elseif response == responseMapping.redRight %Right
                numericalanswerPerif = 0;
                keyPressed = 1;
            else
                numericalanswerPerif = -1;
            end
       end
   else
       %check to see if a button is pressed
       [keyDown,secs,keyCode] = KbCheck;

        %program accepts only LeftArrow or RightArrow as subject responses
        if keyPressed == 0 && keyDown
            numericalanswerPerif = translateKeyPerifResponse(keyCode);
            if numericalanswerPerif ~= -1
                %stop checking for a button press
                keyPressed = 1;
            end
        end
   end
end
% % if numericalanswerPerif == -1
% %     numericalanswerPerif =0;
% % end
end


% Record the subject's central response if it occurs before waitTime
function numericalanswerCent = getCentResponse(waitTime, exptdesign, responseMapping)
%Wait for response
numericalanswerCent = -1;
keyPressed = 0;
startWaitingCent = GetSecs;
while GetSecs - startWaitingCent < waitTime && keyPressed == 0
    if exptdesign.responseBox
        evt = CMUBox('GetEvent', exptdesign.boxHandle);
        if ~isempty(evt)
            response=evt.state;
            if response == responseMapping.animal%animal
                numericalanswerCent = 1;
                keyPressed = 1;
            elseif response == responseMapping.noAnimal %no animal
                numericalanswerCent = 0;
                keyPressed = 1;
            else
                numericalanswerCent = -1;
            end
        end
    else
        %check to see if a button is pressed
        [keyDown,secs,keyCode] = KbCheck;

       %program accepts only RightArrow, LeftArrow and space as subject responses
        if keyPressed == 0 && keyDown
            numericalanswerCent = translateKeyCentResponse(keyCode);
            if numericalanswerCent ~= -1
                %stop checking for a button press
                keyPressed = 1;
            end
        end
    end
end
% % if numericalanswerCent == -1
% %     numericalanswerCent =0;
% % end
end


function [number] = translateKeyCentResponse(keyCode)
keyName = KbName(keyCode);
%         disp(['Pressed key ' keyName]);
if strcmp(keyName,'LeftArrow') || strcmp(keyName,'KP_Left')
    number = 1;
elseif strcmp(keyName,'RightArrow') || strcmp(keyName,'KP_Right')
    number = 0;
else
    number = -1;
end
return;
end


function [number] = translateKeyPerifResponse(keyCode)
keyName = KbName(keyCode);
%         disp(['Pressed key ' keyName]);
if strcmp(keyName, '1!')%strcmp(keyName,'LeftArrow') || strcmp(keyName,'KP_Left')
    number = 1;
elseif strcmp(keyName, '2@')%strcmp(keyName,'RightArrow') || strcmp(keyName,'KP_Right')
    number = 0;
else
    number = -1;
end

return;
end


% Load the specified image
function [images] = loadimages(directory,filenames)
total = size(filenames,1);

for i=1:total
%     disp(filenames(i).name);
    value = imread([directory, filenames(i).name]);
    %try
        %value = rgb2gray(value);
    %catch
    %end
    %images(i,:,:) = value(:,:);
    images(i,:,:,:) = value(:,:,:);

end
end


% Load the specified image
function [images] = loadimages_png(directory,filenames)
total = size(filenames,1);

for i=1:total
%     disp(filenames(i).name);
    value = imread([directory, filenames(i).name], 'png', 'BackgroundColor', [0.5 0.5 0.5]);
    %try
        %value = rgb2gray(value);
    %catch
    %end
    %images(i,:,:) = value(:,:);
    images(i,:,:,:) = value(:,:,:);

end
end


% Draw text in the middle of the screen
function drawAndCenterText(window,message,wait,time)
black = BlackIndex(window);
if nargin < 3
    wait = 1;
end
if nargin < 4
    time = 0;
end

% Now horizontally and vertically centered:
[nx, ny, bbox] = DrawFormattedText(window, message, 'center', 'center', 0);
black = BlackIndex(window); % pixel value for black
% if exptdesign.netstationPresent
%     Screen('FillRect',window,black,[0 0 32 32]);  % This is the stimulus marker block for the photodiode
% end
Screen('Flip',window,time);
%     KbWait;
%     while KbCheck; end;
if wait
    KbPressWait
end
end


% Calls another function to load the pictures.  Puts the target and
% distractor images into a vector and mixes the drink.  Outputs a permuted
% list of randomly chosen and ordered targets and distractors.
%
% INPUT:    exptdesign...nuff said
%
% OUTPUT:   allimages - the permuted vector of targets and distractors
%           stimulustypemarker - tells the function whether each image is a
%           target or a distractor
function [centallimages, centstimulustypemarker, centallimagefiles] = prepCentPics(exptdesign)

cat1files = dir(exptdesign.ctrCat1Images);
if (size(cat1files,1) == 0)
    disp('NO CATEGORY 1 IMAGES!!!!');
    ME = MException('VerifyInput:OutOfBounds', ['NO CATEGORY 1 IMAGES FOUND AT ' exptdesign.cat1Images]);
    throw(ME);
end

cat2files = dir(exptdesign.ctrCat2Images);
if (size(cat2files,1) == 0)
    disp('NO CATEGORY 2 IMAGES!!!!');
    ME = MException('VerifyInput:OutOfBounds', ['NO CATEGORY 2 IMAGES FOUND AT ' exptdesign.cat2Images]);
    throw(ME);
end

%  Load and randomize first images and second category images
%  Peripheral CATEGORY 1
cat1files = cat1files(randperm(size(cat1files,1)));
cat1Images = loadimages(exptdesign.cat1Directory,cat1files(1:exptdesign.numCat1PerSession));
 
%  Peripheral CATEGORY 2
cat2files = cat2files(randperm(size(cat2files,1)));
cat2Images = loadimages(exptdesign.cat2Directory,cat2files(1:exptdesign.numCat2PerSession));

%  Put all the PERIPHERAL CATEGORY 1 and CATEGORY 2 in one vector and permute it
permutation = randperm(exptdesign.numTrialsPerSession);
stimulustypemarker = [ones(1,exptdesign.numCat1PerSession) zeros(1,exptdesign.numCat2PerSession,1)];
centstimulustypemarker = stimulustypemarker(permutation);

clear allimagefiles;
clear allimages;
allimagefiles(:,1) = cat1files(1:exptdesign.numCat1PerSession,1);
allimagefiles(exptdesign.numCat1PerSession+1:exptdesign.numCat1PerSession+exptdesign.numCat2PerSession,1) = cat2files(1:exptdesign.numCat2PerSession,1);
centallimagefiles = allimagefiles(permutation,1);
                     
allimages(:,:,:,:) = cat1Images(:,:,:,:);
allimages(exptdesign.numCat1PerSession+1:exptdesign.numCat1PerSession+exptdesign.numCat2PerSession,:,:,:) = cat2Images(:,:,:,:);
centallimages = allimages(permutation,:,:,:);

end


% Loads the images for the peripheral masks
function [centmaskimages, centmaskimagefiles] = prepCentMask(exptdesign)

maskimagefiles = dir(exptdesign.ctrmaskImages);
if (size(maskimagefiles,1) == 0)
    disp('NO MASK IMAGES!!!!');
    ME = MException('VerifyInput:OutOfBounds', ['NO MASK IMAGES FOUND AT ' exptdesign.cat1Images]);
    throw(ME);
end

% MASKS
centmaskimagefiles = maskimagefiles(randperm(size(maskimagefiles,1)));
centmaskimages = loadimages(exptdesign.imageDirectory,maskimagefiles(1:exptdesign.numTrialsPerSession));
end

