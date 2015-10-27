fprintf('distance to screen must be 120 cm\n');

rng('shuffle');%added 6/30/2015 pc

% get subject and date info
name = input('\n\nEnter Subject ID:\n\n','s');
if isempty(name)
    name = [datestr(now,'yyyy-mm-dd-') 'MR000'];
else
    name = [datestr(now,'yyyy-mm-dd-') name];
end
WaitSecs(0.25);
if ~exist(['./Animal_data_inScanner/' name],'dir')
    mkdir(['./Animal_data_inScanner/' name])
end

exptdesign.subjectName = name;
exptdesign.responseCueTime = 1.2;
exptdesign.responseCueDuration = 4.0;
exptdesign.responseBox = 1;             % Controls whether we are using the keyboard or the response box for subj. responses.
exptdesign.netstationPresent = 0;       % Controls whether or not Netstation is present
exptdesign.netstationIP = '10.0.0.45';  % IP address of the Netstation Computer
exptdesign.netstationSyncLimit = 2;     % Limit under which to sync the Netstation Computer and the Psychtoolbox IN MILLISECONDS

exptdesign.numSessions = 18;              % number of sessions to repeat the experiment
% sessionType 1 = single central; 2 = single peripheral; 3 = Dual
exptdesign.sessionTypes=[1 2 3; 2 3 1; 3 2 1; 2 1 3; 3 1 2; 1 3 2];
exptdesign.numTrialsPerSession = 32;     % number of trials per session (each session is roughly 5 minutes)
exptdesign.refresh = 0.016679454248257;

%give a peripheral cue?
exptdesign.cuePeripheralLocation=1;
exptdesign.cueImage = 'imgsscaled_resized/corners.png';
%with what probability? (.5, 1.0...)
exptdesign.cueProbability=1.0;

exptdesign.fixationDuration =0.500;             % amount of time to display the fixation point (secs)
exptdesign.cueDuration=exptdesign.refresh*2;
exptdesign.fixation2Duration=exptdesign.refresh*2;

exptdesign.fixationImage = 'imgsscaled_resized/fixation.bmp';  % image for the fixation cross
exptdesign.blankImage = 'imgsscaled_resized/blank.bmp';        % image for the blank screen
exptdesign.cueImage = 'imgsscaled_resized/corners.png';

% % % exptdesign.centPerifInterval = exptdesign.refresh;    % Time between the appearance of the central and peripheral stimuli(secs)
% % % exptdesign.cent2Perif = exptdesign.refresh*1;         % Time between the onset of the central stimulus and the peripheral stimulus

% exptdesign.centSOADurations = exptdesign.refresh*2;    
% exptdesign.perifSOADurations = exptdesign.refresh*7;
centSOA = input('\n\nEnter central SOA:\n\n');
perifSOA = input('\n\nEnter peripheral SOA:\n\n');
exptdesign.centSOADurations = exptdesign.refresh*centSOA;    
exptdesign.perifSOADurations = exptdesign.refresh*perifSOA;

% Decide which response mapping you are using
exptdesign.responseKeyChange = input('\n\nEnter response key profile (option 0 or 1):\n\n');

% Data on the pictures to be displayed in the periphery -- For Cars,
% exptdesign.perifWdth = 320;             % Width of the pic
% exptdesign.perifHt = 320;               %Height of aforementioned pic
%For Animals
exptdesign.ctrWdth = 189;             % Width of the pic
exptdesign.ctrHt = 292;               %Height of aforementioned pic
%For Letters 
% exptdesign.perifWdth = 89;             % Width of the pic
% exptdesign.perifHt = 89;  
%for discs
exptdesign.perifWdth = 70;
exptdesign.perifHt = 70;

exptdesign.maskDuration = 0.300;                           % amount of time to display the mask in seconds

exptdesign.perifStimulusDuration = exptdesign.refresh*2;       % Time to display the perif stimuli (secs)
exptdesign.responseDuration = 4.0;                % amount of time to allow for a response in seconds

exptdesign.percentCat1 = 0.5;                % number of times to select first category vs. second category
exptdesign.numCat1PerSession = round(exptdesign.percentCat1 * exptdesign.numTrialsPerSession);
exptdesign.numCat2PerSession = exptdesign.numTrialsPerSession - exptdesign.numCat1PerSession;
exptdesign.numPerifCue=round(exptdesign.cueProbability * exptdesign.numTrialsPerSession);
exptdesign.numCentralCue = exptdesign.numTrialsPerSession - exptdesign.numPerifCue;

exptdesign.randomMask = 1;              % controls whether a random mask is chosen
exptdesign.maskType = 1;                % controls the type of mask used if not randomly chosen (0=small, 1=med, 2=large)
exptdesign.replacement = 1;             % controls whether or not the chosen images are ever used again within a trial
exptdesign.waitForPerifResponse = 0;    % controls whether we wait for a correctly entered peripheral response or continue on
exptdesign.waitForCentResponse = 0;     %    "       "      "  "    "  "    "         "    central       "      "     "     "
exptdesign.usespace=0;                  % use space bar to start each trial?
exptdesign.giveFeedback=0;
exptdesign.animOrCar = 2;               % 0 = animals, 1 = cars, 2 = colored disk

% exptdesign.cat1Images = 'Category1/f*';         % car images to use as the first category
% exptdesign.cat2Images = 'Category2/f*';         % car images to use as the second category
% exptdesign.cat1Images = 'Category1/Xanim*';            % animal images to use as the first category
% exptdesign.cat2Images = 'Category2/Xno*';              % animal images to use as the second category

exptdesign.ctrCat1Images = 'Category1_resized/Xanim*';
exptdesign.ctrCat2Images = 'Category2_resized/Xno*';
exptdesign.ctrmaskImages = 'imgsscaled_resized/Xmask*';

exptdesign.maskImages = 'imgsscaled_resized/circleMask*';          % car mask images to use as the masks
exptdesign.imageDirectory = 'imgsscaled_resized/';

exptdesign.cat1Images = 'Category1_resized/redGreen_70.png';          % circle images to use as the first category 
exptdesign.cat2Images = 'Category2_resized/greenRed_70.png';          % circle images to use as the second category
% exptdesign.maskImages = 'Circles/RedGreenMaskGray*';    % circle mask images to use as the masks
% exptdesign.imageDirectory = 'Circles/';

exptdesign.cat1Directory = 'Category1_resized/';
exptdesign.cat2Directory = 'Category2_resized/';

% make sure subject can see peripheral stim in scanner.
% testPerifVisibility(exptdesign)

if exptdesign.responseBox
    % Ensure button-box configuration is correct
    disp('Ensure dip switches are set to E-PRIME and 5+');
    input('Hit Enter to Continue...');
    exptdesign.boxHandle = CMUBox('Open', 'pst', 'COM1', 'norelease');
end

% make sure subject can see peripheral stim in scanner.
testPerifVisibility(exptdesign)

randomizeRuns=randperm(size(exptdesign.sessionTypes,1));
for run = 1:size(exptdesign.sessionTypes,1)
    exptdesign.sessionType=exptdesign.sessionTypes(randomizeRuns(run),:);
    exptdesign.run=run;
    [trialoutput] = diskAnimalsExperiment_inScanner20150630(name,exptdesign);
end

if exptdesign.responseBox
    CMUBox('Close',exptdesign.boxHandle);
    disp('Ensure dip switches are set back to 4');
end
