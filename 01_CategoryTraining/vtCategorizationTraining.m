%Wrapper For Categoziation Training
%June 15 2015
%CAS cas243@georgetown.edu
% dbstop if error;
%prompt experimenter to check white noise, ear plubs
% diary('log_file.log'); % this will write all the output of the commanr
% line in a file. Useful if some errors occurred.
input('\n\nIs white noise playing? Hit Enter when "Yes."\n');
input('\n\nDoes participant have ear plugs? Hit Enter when "Yes."\n');
input('\n\nIs the driver machine on? Hit Enter when "Yes."\n');

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

%check if the subject has a saved level matrix.  If not, make it with
%starting levels.
%LOAD SUBJECT'S FILE TO APPEND
if exist(['./history/SUBJ' number 'training.mat'], 'file')
    exptdesign.training=load(['./history/SUBJ' number 'training.mat']);
    fprintf(['Subject has been here before, starting at level ' num2str(exptdesign.training.lastLevelPassed)])
else
    level=1;
    fprintf('Subject has not been entered before, starting at level 1')
    exptdesign.training.lastLevelPassed=1; %changed this to one cas 08/10/15
    exptdesign.training.history=[];
end
pause(2)

exptdesign.level=exptdesign.training.lastLevelPassed;

exptdesign.numSessions = 6;              % number of blocks (160 trials each) to complete this training session

% if/else statement to set the number of trials for the level
if exptdesign.level >= 5
    exptdesign.numTrialsPerSession = 144;    % number of trials per block for level 5
else 
    exptdesign.numTrialsPerSession = 128;  % numbeer of trials per block for levels 1,2,3 and 4
end

exptdesign.fixationImage = 'imgsscaled/fixation.bmp';  % image for the fixation cross
exptdesign.blankImage = 'imgsscaled/blank.bmp';        % image for the blank screen
exptdesign.maxLevel = 13;

exptdesign.giveFeedback=1;
exptdesign.cat1label='imgsscaled/labelsGarkTrelp.png'; 
exptdesign.cat2label='imgsscaled/labelsTrelpGark.png'; 

%feedback for incorrect answers == 4 possibilities
%edit 6/22/15 -- there will be no feedback for correct answers (advance
%immediatley to next trial)
exptdesign.fb1='imgsscaled/labelsWordSet1_wrong1.png';
exptdesign.fb2='imgsscaled/labelsWordSet1_wrong2.png';
exptdesign.fb3='imgsscaled/labelsWordSet2_wrong1.png';
exptdesign.fb4='imgsscaled/labelsWordSet2_wrong2.png';

%show correct answers
exptdesign.correct1='imgsscaled/replayGark.png';
exptdesign.correct2='imgsscaled/replayTrelp.png';

exptdesign.imageDirectory = 'imgsscaled/';

handle = errordlg(['Did you remember to pull from Git repo?!\n'...
                   'Because I know for a fact Courtney will eat\n'
                   'your grandbabies if you didnt!']);
disp(handle);

%open COM1 port
try
    stimGenPTB('open','COM1')
    vtCategorizationTrainingExperiment5(name,exptdesign);
catch
    disp('Closing all screens and closing the comport')
    stimGenPTB('close');
    Screen('CloseAll');
end

 handle = errordlg('Please ensure the driver box is turned off');
 disp(handle);

