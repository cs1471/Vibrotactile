% SpatialLocalizationWrapper
% Wrapper, calls PositionLocalizationExperiment.m
% Patrick Malone pmalone333@gmail.com && Courtney Sprouse
% cs1471@georgetown.edu && Levan Bokeria levan.bokeria@georgetown.edu

%prompt experimenter to check white noise, ear plugs
input('\n\nIs white noise playing? Hit Enter when "Yes."\n');
input('\n\nDoes participant have ear plugs? Hit Enter when "Yes."\n')

%get subject info
name = input('\n\nEnter Subject NUMBER:\n\n','s');
number=name;
exptdesign.number=number;
preOrPostTrain = input('\n\nIs this pre or post-training? Enter 1 for pre-training, 2 for post-training:\n\n','s');
exptdesign.preOrPostTrain = preOrPostTrain; % 1 for pre, 2 for post
response = input('\n\nPlease enter the response profile');
exptdesign.response = response;
if isempty(name)
    name = ['MR000'];
else
    name = ['MR' name];
end
WaitSecs(0.25);
%check if the subject has a directory in data.  If not, make it.
if exist(['./data/' number],'dir')
else
    mkdir(['./data/' number])
end

exptdesign.numBlocks = 2;              % number of blocks
exptdesign.numTrialsperSession = 144;

exptdesign.refresh = 0.016679454248257; 

exptdesign.fixationImage = 'imgsscaled/fixation.bmp';  % image for the fixation cross
exptdesign.imageDirectory = 'imgsscaled/';

spatialLocalizationExperiment(name,exptdesign);
