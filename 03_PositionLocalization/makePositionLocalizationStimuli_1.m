f1=2.^([0:.1:2]+log2(25));

frequency = [f1(2) f1(20)];

channels = [2 4 6 10; 6 10 12 14];
pair1 = [repmat(2,1,4), repmat(4,1,4), repmat(6,1,4), repmat(10,1,4), repmat(12,1,4), repmat(14,1,4),...
         repmat(2,1,4), repmat(4,1,4), repmat(6,1,4), repmat(10,1,4), repmat(12,1,4), repmat(14,1,4);
         repmat(frequency(1),1,24), repmat(frequency(2),1,24)];
         
pair2 = [repmat(channels(1,:),1,3), repmat(channels(2,:),1,3),...
         repmat(channels(1,:),1,3), repmat(channels(2,:),1,3);
         repmat(frequency(1),1,24), repmat(frequency(2),1,24)];   
    
%combine frequency combinations with position pairs 
stimuli = [pair1; pair2];
stimuli = [repmat(stimuli,1,3)]; 

% populate trial structure with 2 instances of the same stimulus
save ('positionLocalizationStimuli_1.mat','stimuli')