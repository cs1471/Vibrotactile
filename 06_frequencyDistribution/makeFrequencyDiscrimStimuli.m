f1=2.^([0:.1:2]+log2(25));

frequency = [f1(2) f1(8) f1(20) f1(14); f1(20) f1(14) f1(2) f1(8)];

channels = [1 1 9 11;3 5 13 13];
channels2 = [1 1 5 5; 9 9 13 13];

freqPair = [repmat(frequency(:,1),1,4), repmat(frequency(:,2),1,4), repmat(frequency(:,3),1,4), repmat(frequency(:,4),1,4)];

pair1 = [repmat(freqPair,1,2), repmat(frequency,1,2);
         repmat(channels,1,4), repmat(channels,1,4), repmat(channels2(:,1),1,4), repmat(channels2(:,4),1,4)];
pair2 = [repmat(freqPair,1,2), repmat(frequency,1,2);
         repmat(channels2,1,4), repmat(channels,1,4), repmat(channels2(:,1),1,4), repmat(channels2(:,4),1,4)];

stimulator = [pair1; pair2];
  
%combine frequency combinations with position pairs 
stimuli = [pair1; pair2];
stimuli = [repmat(stimuli,1,3)]; 

% populate trial structure with 2 instances of the same stimulus
save ('frequencyDiscrimStimuli_0.mat','stimuli')