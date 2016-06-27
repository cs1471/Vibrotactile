
% row 1 = apa and ata
% 2 = aba and aga
% 3 = ava and aza
% 4 = afa and asa
% 5 = ama and ana
hits = zeros(5,1);
n_pres = zeros(5,1); % number of presentations of each word pair
for t=1:length(trialOutput)
   for s=1:length(trialOutput{t}.stimuli)
      if strcmp(trialOutput{t}.stimuli{s}(1),'apa') || strcmp(trialOutput{t}.stimuli{s}(1),'ata')
          hits(1,1) = hits(1,1) + trialOutput{t}.accuracy(s);
          n_pres(1,1) = n_pres(1,1) + 1;
      elseif strcmp(trialOutput{t}.stimuli{s}(1),'aba') || strcmp(trialOutput{t}.stimuli{s}(1),'aga')
          hits(2,1) = hits(2,1) + trialOutput{t}.accuracy(s);
          n_pres(2,1) = n_pres(2,1) + 1;
      elseif strcmp(trialOutput{t}.stimuli{s}(1),'ava') || strcmp(trialOutput{t}.stimuli{s}(1),'aza')
          hits(3,1) = hits(3,1) + trialOutput{t}.accuracy(s);
          n_pres(3,1) = n_pres(3,1) + 1;
      elseif strcmp(trialOutput{t}.stimuli{s}(1),'afa') || strcmp(trialOutput{t}.stimuli{s}(1),'asa')
          hits(4,1) = hits(4,1) + trialOutput{t}.accuracy(s);
          n_pres(4,1) = n_pres(4,1) + 1;
      elseif strcmp(trialOutput{t}.stimuli{s}(1),'ama') || strcmp(trialOutput{t}.stimuli{s}(1),'ana')
          hits(5,1) = hits(5,1) + trialOutput{t}.accuracy(s);
          n_pres(5,1) = n_pres(5,1) + 1;
      end
   end
end

acc = hits ./ n_pres;