%rng('shuffle');%added 6/30/2015 pc

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

exptdesign.numBlocks = 24;              % number of blocks (160 trials each) to complete this training session
exptdesign.numTrialsPerSession = 6;    % number of trials per block, could also pull this from dim2 of trainingStimuli
exptdesign.refresh = 0.016679454248257;
exptdesign.responseBox = 1;             % Controls whether we are using the keyboard or the response box for subj. responses.
exptdesign.numRuns = 6;

exptdesign.fixationDuration =0.700;             % amount of time to display the fixation point (secs)

exptdesign.fixationImage = 'imgsscaled/fixation.bmp';  % image for the fixation cross

exptdesign.imageDirectory = 'imgsscaled/';   

% Decide which response mapping you are using
exptdesign.response = input('\n\nEnter response key profile (option 0 or 1):\n\n');

exptdesign.responseDuration = 0.7;                % amount of time to allow for a response in seconds

exptdesign.usespace=0;                  % use space bar to start each trial?

if exptdesign.responseBox
    % Ensure button-box configuration is correct
    disp('Ensure dip switches are set to E-PRIME and 5+');
    input('Hit Enter to Continue...');
    exptdesign.boxHandle = CMUBox('Open', 'pst', 'COM3', 'norelease');
end

%loop over runs here 
[trialoutput] = OddballinScannerExperiment(name,exptdesign);

if exptdesign.responseBox
    CMUBox('Close',exptdesign.boxHandle);
    disp('Ensure dip switches are set back to 4');
end