
% row 1 = heed and hid
% 2 = how'd and head
% 3 = who'd and hood
% 4 = hide and hod
% 5 = hoy'd and had
hits = zeros(5,1);
n_pres = zeros(5,1); % number of presentations of each word pair
for t=1:length(trialOutput)
   for s=1:length(trialOutput{t}.stimuli)
      if strcmp(trialOutput{t}.stimuli{s}(1),'heed') || strcmp(trialOutput{t}.stimuli{s}(1),'hid')
          hits(1,1) = hits(1,1) + trialOutput{t}.accuracy(s);
          n_pres(1,1) = n_pres(1,1) + 1;
      elseif strcmp(trialOutput{t}.stimuli{s}(1),'how''d') || strcmp(trialOutput{t}.stimuli{s}(1),'head')
          hits(2,1) = hits(2,1) + trialOutput{t}.accuracy(s);
          n_pres(2,1) = n_pres(2,1) + 1;
      elseif strcmp(trialOutput{t}.stimuli{s}(1),'who''d') || strcmp(trialOutput{t}.stimuli{s}(1),'hood')
          hits(3,1) = hits(3,1) + trialOutput{t}.accuracy(s);
          n_pres(3,1) = n_pres(3,1) + 1;
      elseif strcmp(trialOutput{t}.stimuli{s}(1),'hide') || strcmp(trialOutput{t}.stimuli{s}(1),'hod')
          hits(4,1) = hits(4,1) + trialOutput{t}.accuracy(s);
          n_pres(4,1) = n_pres(4,1) + 1;
      elseif strcmp(trialOutput{t}.stimuli{s}(1),'hoy''d') || strcmp(trialOutput{t}.stimuli{s}(1),'had')
          hits(5,1) = hits(5,1) + trialOutput{t}.accuracy(s);
          n_pres(5,1) = n_pres(1,1) + 1;
      end
   end
end

acc = hits ./ n_pres;