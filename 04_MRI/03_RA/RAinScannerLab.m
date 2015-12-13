% get subject info
number = input('\n\nEnter Subject ID:\n\n','s');
exptdesign.number = number;
if isempty(number)
    name = [datestr(now,'yyyy-mm-dd-') 'MR000'];
else
    name = [datestr(now,'yyyy-mm-dd-') number];
end
WaitSecs(0.25);

%check if subject has data on file
if ~exist(['./data_RAscan/' number],'dir')
    mkdir(['./data_RAscan/' number])
end

exptdesign.subjectName = name;

%Trial/Block/Run lengths
exptdesign.numBlocks = 1;              
exptdesign.numTrialsPerSession = 240;    
exptdesign.refresh = 0.016679454248257;
exptdesign.numRuns = 1;

%fixation location/duration         
exptdesign.fixationImage = 'imgsscaled/fixation.bmp';  
exptdesign.imageDirectory = 'imgsscaled/';  
exptdesign.interStimuliDuration = .4;

% Decide which response mapping you are using
exptdesign.response = input('\n\nEnter response key profile (option 0 or 1):\n\n');
exptdesign.responseDuration = 3.08;                % amount of time to allow for a response in seconds
exptdesign.responseBox = 0;             % Controls whether we are using the keyboard or the response box for subj. responses.
exptdesign.usespace=0;                  % use space bar to start each trial?
exptdesign.scannerOrlab='l';

%open com3 port for button boxes
if exptdesign.responseBox == 1
    % Ensure button-box configuration is correct
    disp('Ensure dip switches are set to E-PRIME and 5+');
    input('Hit Enter to Continue...');
    exptdesign.boxHandle = CMUBox('Open', 'pst', 'COM3', 'norelease');
end

%open com2 port for stimulator
stimGenPTB('open')

%run all 6 runs right after the last 
for iRuns = 1:exptdesign.numRuns
    exptdesign.iRuns=iRuns;
    [trialOutput] = RAinScannerExperiment2(name,exptdesign);
end

%close com3 port
if exptdesign.responseBox ==1
    CMUBox('Close',exptdesign.boxHandle);
    disp('Ensure dip switches are set back to 4');
end

%close com2 port 
stimGenPTB('close')