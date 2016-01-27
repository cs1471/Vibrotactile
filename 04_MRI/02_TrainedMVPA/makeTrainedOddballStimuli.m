function [stimuliAllRuns, f1, oddChannels] = makeTrainedOddballStimuli(numRuns, response)

if (nargin < 1)
    numRuns=6;
    response=0;
end

    if response == 0
        s1=[1 3 5];
        s2=[9 11 13];
        position = [s1; s2];
        oddChannels = [1 7 13];
    elseif response == 1
        s1=[2 4 6];
        s2=[10 12 14];
        position =[s1; s2];
        oddChannels = [2 8 14];
    end

    %creat category prototype frequncies 
    f1=2.^([0:.1:2]+log2(25)); 
    f2=fliplr(f1);
    frequency = [f1(2), f1(8), f1(14), f1(20);...
                 f2(2), f2(8), f2(14), f2(20)...
                 ];
    
    f_permutation = length(frequency) * length(position) +1;
    permutation = 1;
    
    while permutation ~= f_permutation
        for j = 1:length(frequency)
            for i = 1:length(position)
                stimulator{permutation,:} = [frequency(:,j); position(:,i)];
                permutation = permutation +1;
            end
        end
    end

    for iRun = 1:numRuns
        
        %replicate 2X6 times for total number of stimuli 
        stimuli = repmat(stimulator,2,6); 
           
        odds = zeros(1,size(stimuli,1));
        odds(1,2:7) = ones;   
           
        oddsIndex = randperm(length(odds));
        odds = odds(oddsIndex);
        
          stimuliAllRuns{iRun} = stimuli;
          
          
    end
end