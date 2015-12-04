function spatialLocalizationExperiment(name,exptdesign)

    % spatialLocalization
    % Patrick Malone pmalone333@gmail.com, Courtney Sprouse
    % cs1471@georgetown.edu, Levan Bokeria levan.bokeria@georgetown.edu
    
    % Open a screen and display instructions
    screens=Screen('Screens');
    screenNumber=0;
    
    % Open window with default settings:
    [w windowRect] =Screen('OpenWindow', screenNumber,[128 128 128]);
    white = WhiteIndex(w); % pixel value for white
    gray = GrayIndex(w); % pixel value for gray
    black = BlackIndex(w); % pixel value for black
    HideCursor;
    %load images
    fixationImage = imread(exptdesign.fixationImage);
    
    fixationTexture=Screen('MakeTexture', w, double(fixationImage));
    
    %load training stimuli
    if exptdesign.response == 0
        load('spatialLocalizationStimuli_0.mat');
    else
        load('spatialLocalizationStimuli_1.mat');
    end
    
    for iBlock=1:exptdesign.numBlocks
        %randomize the stimuli for this level
        order=randperm(size(stimuli,2));
        stimuli=stimuli(:, order);
        %lower and upper limit of fixation before stimulus is presented
        ll=.3;
        ul=.8;
        
        if mod(iBlock,2)
            drawAndCenterText(w, ['Please review instructions \n Click the mouse to continue\n'...
                'Please click a mouse button to advance'],1)
            
            drawAndCenterText(w,['\n On each trial, you will feel 2 vibrations, one after the other. \n'...
                'Indicate whether the vibrations are the same or different.\n\n'...
                'LEFT mouse button = "SAME"\n\n'... 
                'RIGHT = "DIFFERENT".\n\n'...
                'Please click the mouse to continue\n'],1)
        else
            drawAndCenterText(w, ['Please review instructions \n Click the mouse to continue\n'...
                'Please click a mouse button to advance'],1)
                        
            drawAndCenterText(w,['\nOn each trial, you will feel 2 vibrations, one after the other. \n'...
                'Indicate whether the vibrations are the same or different.\n\n'...
                'RIGHT mouse button = "SAME"\n\n'... 
                'LEFT = "DIFFERENT".\n\n'...
                'Please click the mouse to continue\n'],1)
             
        end
        
        drawAndCenterText(w,['Block #' num2str(iBlock) ' of ' num2str(exptdesign.numBlocks) '\n\n\n\n'...
            'Click the mouse to continue'],1);
        %WaitSecs(1);
        
        for iTrial=1:exptdesign.numTrialsPerSession
           Screen('DrawTexture', w, fixationTexture);
               [FixationVBLTimestamp FixationOnsetTime FixationFlipTimestamp FixationMissed] = Screen('Flip',w);
               
           wait1 = ll + (ul-ll).*rand(1);
           wait2 = .4;
           WaitSecs(wait1);
           constructStimuli(stimuli(1:2,iTrial)); % present stim 1
           % copied this wait code from above; 
           WaitSecs(wait2);
           constructStimuli(stimuli(3:4,iTrial)); % present stim 2
           
            if isequal(stimuli(1:2, iTrial),stimuli(3:4,iTrial))
               if mod(iBlock,2) % if stimuli same
                   correctResponse=1;
               else 
                   correctResponse=2;
               end
           elseif ~isequal(stimuli(1:2, iTrial),stimuli(3:4,iTrial)) 
               if mod(iBlock,2) % if stimuli different
                   correctResponse=2;
               else 
                   correctResponse=1;
               end
            end
            
           
           drawAndCenterText(w,'Were the vibrations the same or different? \n',0)
           responseStartTime=GetSecs;
           sResp=getResponseMouse(1.5);
           responseFinishedTime=GetSecs;
          
           %score the answer -- is sResp(iTrial)==correctResponse?
           if sResp==correctResponse
               accuracy=1;
           else
               accuracy=0;
           end
           
           %record parameters for the trial
           trialOutput(iBlock).responseStartTime(iTrial)=responseStartTime;
           trialOutput(iBlock).responseFinishedTime(iTrial)=responseFinishedTime;
           trialOutput(iBlock).RT(iTrial)=responseFinishedTime-responseStartTime;
           trialOutput(iBlock).sResp(iTrial)=sResp;
           trialOutput(iBlock).accuracy(iTrial)=accuracy;
           trialOutput(iBlock).correctResponse(iTrial)=correctResponse;
           trialOutput(iBlock).preOrPostTrain = exptdesign.preOrPostTrain;
           trialOutput(iBlock).FixationVBLTimestamp(iTrial)=FixationVBLTimestamp;
           trialOutput(iBlock).FixationOnsetTime(iTrial)=FixationOnsetTime;
           trialOutput(iBlock).FixationFlipTimestamp(iTrial)=FixationFlipTimestamp;
           trialOutput(iBlock).FixationMissed(iTrial)=FixationMissed;
           trialOutput(iBlock).order=order;
           trialOutput(iBlock).stimuli=stimuli;
           
           %tell subject how they did on last block
           if iTrial==exptdesign.numTrialsPerSession && iBlock < exptdesign.numBlocks
               %calculate accuracy
               accuracyForLevel=mean(trialOutput(iBlock).accuracy);
               drawAndCenterText(w, ['Your accuracy was ' num2str(round(accuracyForLevel.*100)) '%\n\n\n'...
                    'Click mouse to continue' ],1)
               %WaitSecs(2);
           elseif iTrial==numTrialsPerSession && iBlock == exptdesign.numBlocks
               %calculate accuracy
               accuracyForLevel=mean(trialOutput(iBlock).accuracy);
               drawAndCenterText(w, ['Your accuracy was ' num2str(round(accuracyForLevel.*100)) '%\n\n\n'...
                   'You have completed this training session.  Great job!' ],1)
               %WaitSecs(2);
               Screen('CloseAll')
           end
           
           clear correctResponse correctionTexture;
        end  

        %record parameters for the block
        %stimuli, order
        
        
        %save the session data in the data directory
        save(['./data/' name '/' name '_block' num2str(iBlock) '.' num2str(iTrial) '.mat'], 'trialOutput', 'exptdesign');
        %save the history data (stimuli, last level passed)
        
        
    end
    
    ShowCursor;
    
end
    
function drawAndCenterText(window,message,wait)
    if nargin < 3
        wait = 1;
    end
    
    % Now horizontally and vertically centered:
    [nx, ny, bbox] = DrawFormattedText(window, message, 'center', 'center', 0);
    black = BlackIndex(window); % pixel value for black               
    Screen('Flip',window);
    %KbWait(1) waits for a MOUSE click to continue
    if wait, KbWait(1); end
    WaitSecs(0.2); %this is necessary on the windows XP machine to wait for mouse response -- DOES delay timing!
end

function numericalanswer = getResponseMouse(waitTime)

  %Wait for a response
  numericalanswer = -1;
  mousePressed = 0;
  startWaiting=clock;
  while etime(clock,startWaiting) < waitTime && mousePressed == 0
      %check to see if a button is pressed
       [x,y,buttons] = GetMouse();
       if (~buttons(1) && ~buttons(3))
           continue;
       else
           if buttons(1)
               numericalanswer = 1;
           elseif buttons(3)
               numericalanswer = 2;
           else
               numericalanswer = 0;
           end
           if numericalanswer ~= -1
              %stop checking for a button press
              mousePressed = 1;
           end
       end

  end
  if numericalanswer == -1
      numericalanswer =0;
  end
end

function constructStimuli(stimulus)
    f = stimulus(1);
    p = stimulus(2);

    stim = {...
        {'fixed',f,1,300},...
        {'fixchan',p},...
        };

    [t,s]=buildTSM_nomap(stim);

    stimGenPTB('load',s,t);
    rtn=-1;
    while rtn==-1
        rtn=stimGenPTB('start');
    end
end
