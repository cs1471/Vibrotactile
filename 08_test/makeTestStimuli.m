f1=2.^((0:.1:2)+log2(25));

%generate frequencies
frequency = f1(20);

%generate positions based on response profile
channels = [3 5 7 9];
    
%generate frequencies to be compared with all possible positions
stimuli = [repmat(frequency,1,4); channels];     

% populate trial structure with 2 instances of the same stimulus
save ('testStimuli.mat','stimuli')
