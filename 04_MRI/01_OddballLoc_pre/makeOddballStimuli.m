function [stimuliShuffled, oddball] = makeOddballStimuli(numRuns, response)

    if response == 0
        position = [1 3 5 9 11 13];
    elseif response == 1
        position = [2 4 6 10 12 14];
    end

    %creat category prototype frequncies 
    f1 = 2^(0+log2(25));
    f2 = 2^(2+log2(25));
    
    for i = 1:length(position)/2
        pairF1P1{i,:} = [f1; position(i)];
        pairF2P1{i,:} = [f2; position(i)];
    end
    
    for i = 4:length(position)
        pairF1P2{i,:} = [f1; position(i)];
        pairF2P2{i,:} = [f2; position(i)];
    end
    
    %delete empyt cells because could not start at 0
    pairF1P2 = pairF1P2(~cellfun(@isempty,pairF1P2));
    pairF2P2 = pairF2P2(~cellfun(@isempty,pairF2P2));
    
    
    %replicate 6 times for total number of stimuli 
    pairF1P1 = repmat(pairF1P1,1,6);
    pairF2P1 = repmat(pairF2P1,1,6);
    pairF1P2 = repmat(pairF1P2,1,6);
    pairF2P2 = repmat(pairF2P2,1,6); 

    for i = 1:numRuns
        stimuli = [pairF1P1; pairF2P1; pairF1P2; pairF2P2...
               ; pairF1P1; pairF2P1; pairF1P2; pairF2P2];  
           
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