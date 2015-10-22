%vibrotactile oddball for localizer! called by VToddball
%Courtney A Sprouse cs1471@georgetown.edu

function VToddballExperiment(name, exptdesign)
    
%     %initialize the serial port -- JUST RUN TESTCONTIN FIRST
    stimGenPTB('CloseAll');
    stimGenPTB('open','COM1')

    %Open a screen and display instructions
    screens=Screen('Screens');
    screenNumber=0;

    % Open window with default settings:
    [w windowRect] =Screen('OpenWindow', screenNumber,[128 128 128]);
%        [w windowRect] = Screen('OpenWindow', screenNumber,[128 128 128], [0 0 800 800]); %for debugging
    white = WhiteIndex(w); % pixel value for white
    gray = GrayIndex(w); % pixel value for gray
    black = BlackIndex(w); % pixel value for black
    HideCursor;
    
    %calculate the slack allowed during a flip interval
    refresh = Screen('GetFlipInterval',w);
    slack = refresh/2;
    
%     load images
    fixationImage = imread(exptdesign.fixationImage);
    % BLANK IMAGE
    blankImage = imread(exptdesign.blankImage);
    
    %load the images and pngs     
    fixationTexture=Screen('MakeTexture', w, double(fixationImage));
    blankTexture=Screen('MakeTexture', w, double(blankImage));


    %Display experiment instructions
    drawAndCenterText(w,['\nOn each trial, you will feel 6 vibrations \n'...
             'You will indicate the vibration that felt different from the other 5 vibrations\n'...
             'by pushing the button.'  ],1)
         
   
   response = exptdesign.response;

    %load training stimuli
    [stimuli] = makeStimuli(response);
  
    %generate a correctResponse map
    for i = 1:size(stimuli,2)
        for j = 1:size(stimuli,1)
            if (size(stimuli{j,i},2) > 1)
                correctResponse(j,i) = 1;
            else
                correctResponse(j,i) = 0;
            end
        end
    end
    
    for iBlock=1:size(stimuli,1)%how many blocks to run this training session
        stimulusTracking=[];
%         drawAndCenterText(w,['Block #' num2str(iBlock) ' of ' num2str(exptdesign.numSessions) '\n\n\n\n'],1); 
        
        stimuliBlock = [stimuli{iBlock,:}];
        
        %iterate over trials
        for iTrial=1:size(stimuli,2)
            
            %clear event responses stored in cue
            while ~isempty(evt)
                evt = CMUBox('GetEvent', exptdesign.boxHandle);
            end
           
           
           
           %draw fixation
           Screen('DrawTexture', w, fixationTexture);
           [FixationVBLTimestamp FixationOnsetTime FixationFlipTimestamp FixationMissed] = Screen('Flip',w);
           
           %after 700 ms, present the vibrotactile stimulus
           wait1 = .7;
           WaitSecs(wait1);
%            constructStimuli(stimuliBlock(:, iTrial));
           
           drawAndCenterText(w, 'Break /n/n/n Press button if felt unique vibration pattern',1)
           [RespVBLTimestamp RespOnsetTime RespFlipTimestamp RespMissed] = Screen('Flip', w, wait1);
           
           %record response start time
           responseStartTime=GetSecs;
           %record subject responses
           numericalAnswer(responseMapping);
           %record end time of response
           responseFinishedTime=GetSecs;
          
           %record parameters for the trial
           trialOutput(iBlock).responseStartTime(iTrial)=responseStartTime;
           trialOutput(iBlock).responseFinishedTime(iTrial)=responseFinishedTime;
           trialOutput(iBlock).RT(iTrial)=responseFinishedTime-responseStartTime;
           trialOutput(iBlock).sResp(iTrial)=sResp;
           trialOutput(iBlock).wait1(iTrial)=wait1;
           
           %save stimulus presentation timestamps
           [FixationVBLTimestamp FixationOnsetTime FixationFlipTimestamp FixationMissed]
           [RespVBLTimestamp RespOnsetTime RespFlipTimestamp RespMissed]
           %
           trialOutput(iBlock).FixationVBLTimestamp(iTrial)=FixationVBLTimestamp;
           trialOutput(iBlock).FixationOnsetTime(iTrial)=FixationOnsetTime;
           trialOutput(iBlock).FixationFlipTimestamp(iTrial)=FixationFlipTimestamp;
           trialOutput(iBlock).FixationMissed(iTrial)=FixationMissed;
           trialOutput(iBlock).RespVBLTimestamp(iTrial)=RespVBLTimestamp;
           trialOutput(iBlock).RespOnsetTime(iTrial)=RespOnsetTime;
           trialOutput(iBlock).RespFlipTimestamp(iTrial)=RespFlipTimestamp;
           trialOutput(iBlock).RespMissed(iTrial)=RespMissed;

           if iTrial==exptdesign.numTrialsPerSession && iBlock == exptdesign.numSessions
               
               Screen('CloseAll')
           end
         
           
        end
        %record parameters for the block
        %stimuli, order
        trialOutput.stimuli=stimuli;
        
        %save the session data in the data directory
        save(['./data/' exptdesign.number '/' datestr(now, 'yyyymmdd_HHMM') '-' exptdesign.subjectName '_block' num2str(iBlock) '.mat'], 'trialOutput', 'exptdesign');
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
    
    %KbWait(1) waits for a button press to continue
    KbWait([],2);
%     WaitSecs(0.2); %this is necessary on the windows XP machine to wait for mouse response -- DOES delay timing!
end



function sResp = numericalAnswer(responseMapping)
if exptdesign.responseBox
        evt = CMUBox('GetEvent', exptdesign.boxHandle);
        if ~isempty(evt)
            response=KbPress;
            if response == KbPress
                sResp = 1;
            else
                sResp = 0;
            end
        end
end
end

function [stimuli, oddball] = makeStimuli(response)

if response == 0
    position = [1 3 5 9 11 13];
elseif response == 1
    position = [2 4 6 10 12 14];
end

    %creat category prototype frequncies 
    f1 = 2^(0+log2(25));
    f2 = 2^(2+log2(25));
    
    for i = 1:length(position)/2
        pairF1P1{i,:} = [f1; position(i)];
        pairF2P1{i,:} = [f2; position(i)];
    end
    
    for i = 4:length(position)
        pairF1P2{i,:} = [f1; position(i)];
        pairF2P2{i,:} = [f2; position(i)];
    end
    
    pairF1P2 = pairF1P2(~cellfun(@isempty,pairF1P2));
    pairF2P2 = pairF2P2(~cellfun(@isempty,pairF2P2));
    
    pairF1P1 = repmat(pairF1P1,1,5);
    pairF2P1 = repmat(pairF2P1,1,5);
    pairF1P2 = repmat(pairF1P2,1,5);
    pairF2P2 = repmat(pairF2P2,1,5);
    
    %combine frequencies and stimulator combinations into stimuli
    
    col = size(pairF1P1,2)+1;
    for i = 1:3
        pairF1P1{i,col} = [repmat(f2,1,3); position(4:6)];
        pairF2P1{i,col} = [repmat(f1,1,3); position(4:6)];
        pairF1P2{i,col} = [repmat(f2,1,3); position(1:3)];
        pairF2P2{i,col} = [repmat(f1,1,3); position(1:3)];
    end
    
    stimuli = [pairF1P1; pairF2P1; pairF1P2; pairF2P2];  
    oddball = stimuli{:,6};

    for i = 1:numRuns
        stimuli = shake(stimuli,2);

        rng('shuffle')
        ind = randperm(numel(stimuli(:,1)))'; %// random permutation
        stimuliShuffled(:,:,i) = stimuli(ind,:);
    end
    save stimuliShuffled.mat stimuliShuffled
end

function constructStimuli(stimuliBlock)
    f = stimuliBlock(1,:);
    p = stimuliBlock(2,:);

    if size(stimuliBlock,2) > 1
        constructOddStimuli(stimuliBlock)
    else
        stim = {...
            {'fixed',f,1,300},...
            {'fixchan',p},...
            };
        
        [t,s]=buildTSM_nomap(stim);
        
        stimGen('load',s,t);
        rtn=-1;
        while rtn==-1
            rtn=stimGen('start');
        end
    end
end

function constructOddStimuli(stimuliBlock)
   f = stimuliBlock(1,:);
   p = stimuliBlock(2,:);
    
    stim = {...
            {'fixed',f(1),1,300},...
            {'durchannel',p(1),1, 90},...
            {'fixed',f(1),1,300},...
            {'durchannel',p(2), 100,190},...
            {'fixed',f(1),1,300},...
            {'durchannel',p(3), 200,290},...
           };

    [t,s]=buildTSM_nomap(stim);    
       
    stimGenPTB('load',s,t);
    rtn=-1;
    while rtn==-1
        rtn = stimGen('start');
    end
    
end