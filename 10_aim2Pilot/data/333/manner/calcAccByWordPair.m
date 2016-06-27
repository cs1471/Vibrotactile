
% row 1 = ada and aza
% 2 = aza and ana
% 3 = aba and ama
% 4 = ada and ana
% 5 = ata and asa
hits = zeros(5,1);
n_pres = zeros(5,1); % number of presentations of each word pair
for t=1:length(trialOutput)
   for s=1:length(trialOutput{t}.stimuli)
      if (strcmp(trialOutput{t}.stimuli{s}(1),'ada') && strcmp(trialOutput{t}.stimuli{s}(2),'aza')) || (strcmp(trialOutput{t}.stimuli{s}(1),'aza') && strcmp(trialOutput{t}.stimuli{s}(2),'ada'))
          hits(1,1) = hits(1,1) + trialOutput{t}.accuracy(s);
          n_pres(1,1) = n_pres(1,1) + 1;
      elseif (strcmp(trialOutput{t}.stimuli{s}(1),'aza') && strcmp(trialOutput{t}.stimuli{s}(2),'ana')) || (strcmp(trialOutput{t}.stimuli{s}(1),'ana') && strcmp(trialOutput{t}.stimuli{s}(2),'aza'))
          hits(2,1) = hits(2,1) + trialOutput{t}.accuracy(s);
          n_pres(2,1) = n_pres(2,1) + 1;
      elseif strcmp(trialOutput{t}.stimuli{s}(1),'aba') || strcmp(trialOutput{t}.stimuli{s}(1),'ama')
          hits(3,1) = hits(3,1) + trialOutput{t}.accuracy(s);
          n_pres(3,1) = n_pres(3,1) + 1;
      elseif (strcmp(trialOutput{t}.stimuli{s}(1),'ada') && strcmp(trialOutput{t}.stimuli{s}(2),'ana')) || (strcmp(trialOutput{t}.stimuli{s}(1),'ana') && strcmp(trialOutput{t}.stimuli{s}(2),'ada'))
          hits(4,1) = hits(4,1) + trialOutput{t}.accuracy(s);
          n_pres(4,1) = n_pres(4,1) + 1;
      elseif strcmp(trialOutput{t}.stimuli{s}(1),'ata') || strcmp(trialOutput{t}.stimuli{s}(1),'asa')
          hits(5,1) = hits(5,1) + trialOutput{t}.accuracy(s);
          n_pres(5,1) = n_pres(5,1) + 1;
      end
   end
end

acc = hits ./ n_pres;