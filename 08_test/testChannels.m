% FrequencyDiscrimWrapper
% Wrapper, calls frequencyDiscrimExperiment.m
% Courtney Sprouse cs1471@georgetown.edu && Patrick Malone pmalone333@gmail.com && 
% Levan Bokeria levan.bokeria@georgetown.edu

% %prompt experimenter to check white noise, ear plugs
input('\n\nIs white noise playing? Hit Enter when "Yes."\n');
input('\n\nDoes participant have ear plugs? Hit Enter when "Yes."\n')

%debug info 
% exptdesign.number = '915';
% number = '915';
% exptdesign.practiceType = 1;
% exptdesign.subjectName = ['MR' exptdesign.number];


%get subject info
number = input('\n\nEnter Subject NUMBER:\n\n','s');
exptdesign.number = number;

exptdesign.practiceType = input(['\n\nIs this for category training practice or channel testing?'...
    'Enter 0 for category training practice, 1 for channel testing:\n\n'],'s');

if isempty(number)
    name = 'MR000';
else
    name = ['MR' number];
end
WaitSecs(0.25);

exptdesign.subjectName = name;

%check if the subject has a directory in data.  If not, make it.
if exist(['./data/' number],'dir')
else
    mkdir(['./data/' number])
end

exptdesign.numBlocks = 1;              % number of blocks
exptdesign.numTrialsPerSession = 12;
if practiceType == '0'
    exptdesign.StimPresentationWindow = .3;
else
    exptdesign.StimPresentationWindow = .5;
end

exptdesign.fixationImage  = 'imgScaled/fixation.bmp';  % image for the fixation cross
exptdesign.stimBoardImages = dir('imgScaled/stimBoard*.bmp');

stimGenPTB('open')
testChannelsExperiment(exptdesign);
stimGenPTB('close')