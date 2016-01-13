f1=2.^([0:.1:2]+log2(25));

frequency = [f1(1) f1(8) f1(14) f1(21)];

channels = [1 10 5 14];

% generate 4 prototype stimuli (see Josh/Clara poster)
proto1 = [frequency(1) frequency(4) channels(1) channels(2)]';   
proto2 = [frequency(2) frequency(3) channels(1) channels(2)]';    
proto3 = [frequency(3) frequency(2) channels(1) channels(2)]';     
proto4 = [frequency(4) frequency(1) channels(1) channels(2)]';
proto5 = [frequency(1) frequency(4) channels(3) channels(4)]';   
proto6 = [frequency(2) frequency(3) channels(3) channels(4)]';    
proto7 = [frequency(3) frequency(2) channels(3) channels(4)]';     
proto8 = [frequency(4) frequency(1) channels(3) channels(4)]';
  
%generate same and different stimuli 
stimuliSame = [repmat(proto1,1,3), repmat(proto2,1,3), repmat(proto3,1,3), repmat(proto4,1,3) , repmat(proto5,1,3), repmat(proto6,1,3), repmat(proto7,1,3), repmat(proto8,1,3); 
               repmat(proto1,1,3), repmat(proto2,1,3), repmat(proto3,1,3), repmat(proto4,1,3),  repmat(proto5,1,3), repmat(proto6,1,3), repmat(proto7,1,3), repmat(proto8,1,3)];

stimuliDifferent = [repmat(proto1,1,3),        repmat(proto2,1,3),        repmat(proto3,1,3),        repmat(proto4,1,3),      repmat(proto5,1,3),        repmat(proto6,1,3),        repmat(proto7,1,3),        repmat(proto8,1,3);
                    proto2, proto3, proto4,    proto1, proto3, proto4,    proto1, proto2, proto4     proto1, proto2, proto3,  proto6, proto7, proto8,    proto5, proto7, proto8,    proto5, proto6, proto8     proto5, proto6, proto7];
                 
stimuli = [stimuliSame, stimuliDifferent];
stimuli = repmat(stimuli,1,3);

save ('frequencyDiscrimStimuli2.mat','stimuli')