function [stimuliShuffled, oddball] = makeOddballStimuli(numRuns, response)

numRuns=6
response=0
    if response == 0
        s1=[1 3 5];
        s2=[9 11 13];
        position = [s1; s2];
    elseif response == 1
        s1=[2 4 6];
        s2=[10 12 14];
        position =[s1; s2];
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

    for i = 1:numRuns
        
        %replicate 2X6 times for total number of stimuli 
        stimuli = repmat(stimulator,2,6); 
           
        odds = zeros(1,size(stimuli,1));
        odds(1,2:7) = ones;   
           
        oddsIndex = randperm(length(odds));
        odds = odds(oddsIndex);
%        
%         for j = 1:size(stimuli,1)
%             if odds(j) == 1
%                 if (stimuli{j,1}(1) == f1) && (stimuli{j,1}(2) == position(1) || position(2) || position(3))
%                     stimuli{j,6}= [repmat(f2,1,3); position(4:6)];
%                 elseif (stimuli{j,1}(1)== f2) && (stimuli{j,1}(2) == position(1) || position(2) || position(3))
%                     stimuli{j,6} = [repmat(f1,1,3); position(4:6)];
%                 elseif (stimuli{j,1}(1)== f1) && (stimuli{j,1}(2) == position(4) || position(5) || position(6))
%                      pairF1P2{j,col} = [repmat(f2,1,3); position(1:3)];
%                 elseif (stimuli{j,1}(1)== f2) && (stimuli{j,1}(2) == position(4) || position(5) || position(6))
%                     pairF1P2{j,col} = [repmat(f1,1,3); position(1:3)];
%                 end
%             end
%         end
%         
        stimuli = shake(stimuli,2);

        ind = randperm(numel(stimuli(:,1)))'; %// random permutation
        stimuliShuffled(:,:,i) = stimuli(ind,:);
        clear stimuli
    end
    save stimuliShuffled.mat stimuliShuffled
end