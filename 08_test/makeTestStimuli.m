response = input(['\n\nGenerating stimuli for channel testing (enter 0)\n\n'...
    'Generating stimuli for categ practice (enter 1):\n\n'],'s');

f1=2.^((0:.1:2)+log2(25));

%generate frequencies
frequency = f1(20);

frequencyCateg=[f1(1:4) f1(18:21); f1(18:21) f1(1:4)]; %frequency combos (8 total)

%generate positions based on response profile
channels = [2 1 4 3 6 5 10 9 12 11 14 13];


%find possible stimulator combinations (8 combos total)
stimulator = [1 2 5 6 1 2 5 6;
    9 10 13 14 10 9 14 13];
    
%generate frequencies to be compared with all possible positions
if response == '0'
    stimuli = [repmat(frequency,1,12); channels];
else
    stimuli = [repmat(frequencyCateg, 1, 2);
               repmat(stimulator, 1, 2)];
end
        

% populate trial structure with 2 instances of the same stimulus
if response == '0'
    save ('testStimuli.mat','stimuli')
else
    save ('testStimuliCateg.mat','stimuli')
end