% get subject info
exptdesign.debugmode = 0; % Does not work for now. keep this commented.
if exptdesign.debugmode
    number = '0000'
    WARN = input('YOU ARE IN DEBUG MODE. ARE YOU SURE THIS IS RIGHT?');
else
    number = input('\n\nEnter Subject ID:\n\n','s');
end
%name = '915';
%number = name;
exptdesign.number = number;
if isempty(number)
    name = [datestr(now,'yyyy-mm-dd-HH-MM') 'MR000'];
else
    name = [datestr(now,'yyyy-mm-dd-HH-MM') number];
end
WaitSecs(0.25);

%check if subject has data on file
exptdesign.saveDir = ['./data_Untrained_Localizer/' name];
if ~exist(exptdesign.saveDir,'dir')
    mkdir(exptdesign.saveDir)
end

%Trial/Block/Run lengths
exptdesign.subjectName = name;
exptdesign.iBlocks = 24;              
exptdesign.numTrialsPerSession = 6;    
exptdesign.refresh = 0.016679454248257;
exptdesign.numRuns = 6;

%fixation location/duration
exptdesign.fixationDuration =0.700;             
exptdesign.fixationImage = 'imgsscaled/fixation.bmp'; 
exptdesign.imageDirectory = 'imgsscaled/';   

% Decide which response mapping you are using
if exptdesign.debugmode
    exptdesign.response = 1;
    exptdesign.responseBox = 0;
    exptdesign.boxHandle = 2; % we still need this variable in the debug mode. 
else
    exptdesign.response = input('\n\nEnter response key profile (option 0 or 1):\n\n');
    exptdesign.responseBox = 1;             % Controls whether we are using the keyboard or the response box for subj. responses.
end
exptdesign.responseDuration = 0.7;                % amount of time to allow for a response in seconds
exptdesign.usespace=0;                  % use space bar to start each trial?

%open com3 port for button boxes
if exptdesign.responseBox
    % Ensure button-box configuration is correct
    disp('Ensure dip switches are set to E-PRIME and 5+');
    input('Hit Enter to Continue...');
    exptdesign.boxHandle = CMUBox('Open', 'pst', 'COM3', 'norelease');
end

%open com2 port for stimulator
stimGenPTB('open')

for iRuns = 1:exptdesign.numRuns
    exptdesign.iRuns=iRuns;
    [trialOutput.runs] = untrainedOddballinScannerExperiment(name,exptdesign);
end

%close com3 port
if exptdesign.responseBox
    CMUBox('Close',exptdesign.boxHandle);
    disp('Ensure dip switches are set back to 4');
end

%close com2 port 
stimGenPTB('close')