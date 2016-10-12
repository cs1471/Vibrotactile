VTspeechStim_labels = {'ada1';'ada2';'aza1';'aza2';'aba1';'aba2';'ata1';'ata2';'ana1';'ana2';...
    'ama1';'ama2';'asa1';'asa2';'apa1';'apa2';'ava1';'ava2';'afa1';'afa2';'aga1';...
    'aga2';'aka1';'aka2'};

VTspeechStim = cell(2,24);

for i=1:length(VTspeechStim_labels)
    load(['sampledPulseFiles/volume_2point25_outputGain_50/' VTspeechStim_labels{i}]);
    tm = tactStim{1}{1};
    ch = tactStim{1}{2};
    ch = remapChan(ch);
    VTspeechStim{1,i} = tm;
    VTspeechStim{2,i} = ch;
    clear tactStim tm ch
end

save('VTspeechStim','VTspeechStim','VTspeechStim_labels');