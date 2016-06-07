
% row 1 = hod and hood
% 2 = had and hid
hits = zeros(2,1);
n_pres = zeros(2,1); % number of presentations of each word pair
for t=1:length(trialOutput)
   for s=1:24%length(trialOutput{t}.stimuli)
      if strcmp(trialOutput{t}.stimuli{s}(1),'hod') || strcmp(trialOutput{t}.stimuli{s}(1),'hood')
          hits(1,1) = hits(1,1) + trialOutput{t}.accuracy(s);
          n_pres(1,1) = n_pres(1,1) + 1;
      elseif strcmp(trialOutput{t}.stimuli{s}(1),'had') || strcmp(trialOutput{t}.stimuli{s}(1),'hid')
          hits(2,1) = hits(2,1) + trialOutput{t}.accuracy(s);
          n_pres(2,1) = n_pres(2,1) + 1;
      end
   end
end

acc = hits ./ n_pres;