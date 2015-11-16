f1=2.^([0:.1:2]+log2(25));

frequency = [f1(2) f1(8) f1(14) f1(20)];

channels = [1 7 13];
% channels = [2 8 14];

pair1 = [repmat(frequency(1),1,3);
         repmat(channels,1,1)];
     
pair2 = [repmat(frequency(2),1,3);
         repmat(channels,1,1)];
     
pair3 = [repmat(frequency(3),1,3);
         repmat(channels,1,1)];
     
pair4 = [repmat(frequency(4),1,3);
         repmat(channels,1,1)];

stimulator = [pair1 pair2 pair3 pair4];
  
%combine frequency combinations with position pairs 
stimuli = [repmat(stimulator,1,4);stimulator, pair2, pair3, pair4, pair1, pair3, pair4, pair1, pair2, pair4, pair1, pair2, pair3];

stimuli = repmat(stimuli,1,3);

% populate trial structure with 2 instances of the same stimulus
save ('frequencyDiscrimStimuli_0.mat','stimuli')

% save ('frequencyDiscrimStimuli_1.mat','stimuli')