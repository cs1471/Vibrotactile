%Wrapper For Categoziation Training for generating sigmoidal categorization
%curve. No feedback, positions 4 and 10 included for testing generalization
%April 11 2016
%PSM pmalone333@gmail.com

input('\nDid you pull from Git? Hit Enter when "Yes."\n');
input('\nIs white noise playing? Hit Enter when "Yes."\n');
input('\nDoes participant have ear plugs? Hit Enter when "Yes."\n');
input('\nIs the driver machine on? Hit Enter when "Yes."\n');

%get subject info
number = input('\n\nEnter Subject NUMBER:\n\n','s');
name = number;
if isempty(name)
    name = 'MR000';
else
    name = ['MR' name];
end
exptdesign.subNumber = number; 
exptdesign.subName = name;
WaitSecs(0.25);
%check if the subject has a directory in data.  If not, make it.
if exist(['./data/' number],'dir')
else
    mkdir(['./data/' number])
end

pause(2)

% exptdesign.level=exptdesign.training.lastLevelPassed;

exptdesign.numSessions = 6;              % number of blocks (160 trials each) to complete this training session

% if/else statement to set the number of trials for the level
exptdesign.numTrialsPerSession = 144;    % number of trials per block for level 5

exptdesign.fixationImage = 'imgsscaled/fixation.bmp';  % image for the fixation cross
exptdesign.blankImage = 'imgsscaled/blank.bmp';        % image for the blank screen

exptdesign.cat1label='imgsscaled/labelsGarkTrelp.png'; 
exptdesign.cat2label='imgsscaled/labelsTrelpGark.png'; 

exptdesign.imageDirectory = 'imgsscaled/';

%open COM1 port
try
    stimGenPTB('open','COM1')
    vtCategorizationTrainingExperimentSigmoidalNoFB(name,exptdesign);
catch
     disp('Closing all screens and closing the Com Port')
     stimGenPTB('close');
     Screen('CloseAll');
 end

 handle = errordlg('Please ensure the driver box is turned off');
 disp(handle);

