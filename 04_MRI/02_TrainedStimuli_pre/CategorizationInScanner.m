fprintf('distance to screen must be 120 cm\n');

rng('shuffle');%added 6/30/2015 pc

% get subject info
name = input('\n\nEnter Subject ID:\n\n','s');
number = name;
exptdesign.number = number;
if isempty(name)
    name = [datestr(now,'yyyy-mm-dd-') 'MR000'];
else
    name = [datestr(now,'yyyy-mm-dd-') name];
end
WaitSecs(0.25);

%check if subject has data on file
if exist(['./data/' number],'dir')
else
    mkdir(['./data/' number])
end

exptdesign.subjectName = name;
exptdesign.netstationPresent = 0;       % Controls whether or not Netstation is present
exptdesign.netstationIP = '10.0.0.45';  % IP address of the Netstation Computer
exptdesign.netstationSyncLimit = 2;     % Limit under which to sync the Netstation Computer and the Psychtoolbox IN MILLISECONDS

exptdesign.numSessions = 6;              % number of blocks (160 trials each) to complete this training session
exptdesign.numTrialsPerSession = 128;    % number of trials per block, could also pull this from dim2 of trainingStimuli
exptdesign.refresh = 0.016679454248257;
exptdesign.responseBox = 1;             % Controls whether we are using the keyboard or the response box for subj. responses.

exptdesign.responseCueTime = 1.2;
exptdesign.responseCueDuration = 4.0;

exptdesign.fixationDuration =0.500;             % amount of time to display the fixation point (secs)
exptdesign.fixation2Duration=exptdesign.refresh*2;

exptdesign.fixationImage = 'imgsscaled_resized/fixation.bmp';  % image for the fixation cross
exptdesign.blankImage = 'imgsscaled_resized/blank.bmp';        % image for the blank screen

exptdesign.imageDirectory = 'imgsscaled/';   

% Decide which response mapping you are using
exptdesign.responseKeyChange = input('\n\nEnter response key profile (option 0 or 1):\n\n');

% Data on the pictures to be displayed in the periphery -- For Cars,
% exptdesign.perifWdth = 320;             % Width of the pic
% exptdesign.perifHt = 320;               %Height of aforementioned pic
%For Animals
exptdesign.ctrWdth = 189;             % Width of the pic
exptdesign.ctrHt = 292;               %Height of aforementioned pic

exptdesign.responseDuration = 4.0;                % amount of time to allow for a response in seconds

%give a peripheral cue?
exptdesign.cueLocation=1;
exptdesign.cueImage = 'imgsscaled_resized/corners.png';
%with what probability? (.5, 1.0...)
exptdesign.cueProbability=1.0;

exptdesign.percentCat1 = 0.5;                % number of times to select first category vs. second category
exptdesign.numCat1PerSession = round(exptdesign.percentCat1 * exptdesign.numTrialsPerSession);
exptdesign.numCat2PerSession = exptdesign.numTrialsPerSession - exptdesign.numCat1PerSession;
exptdesign.numCentralCue = round(exptdesign.cueProbability * exptdesign.numTrialsPerSession);

exptdesign.replacement = 1;             % controls whether or not the chosen images are ever used again within a trial
exptdesign.waitForCentResponse = 0;     % controls whether we wait for a correctly entered peripheral response or continue on
exptdesign.usespace=0;                  % use space bar to start each trial?
exptdesign.giveFeedback=0;

if exptdesign.responseBox
    % Ensure button-box configuration is correct
    disp('Ensure dip switches are set to E-PRIME and 5+');
    input('Hit Enter to Continue...');
    exptdesign.boxHandle = CMUBox('Open', 'pst', 'COM1', 'norelease');
end

%randomize the stimuli for this level
order=randperm(exptdesign.numTrialsPerSession);
stimuli=squeeze(trainingStimuli(:,order,level));
%lower and upper limit of fixation before stimulus is presented
ll=.3;
ul=.8;

if exptdesign.responseBox
    CMUBox('Close',exptdesign.boxHandle);
    disp('Ensure dip switches are set back to 4');
end

[trialoutput] = VTinScannerExperiment2(name,exptdesign);