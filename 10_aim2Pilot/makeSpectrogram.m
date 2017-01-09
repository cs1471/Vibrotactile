vcv_cfg;

%load audio
[y,fs] = wavread(audio_filename);
wavedata = y';
window = hamming(512); % window size of 512 points
noverlap = 256; % number of points for repeating window 
nfft=1024; % size of fft
lookupf = [260,392,525,660,791,925,1060,1225,1390,1590,1820,2080,2380,5000]; % freqs for GUEq vocoder algorithm
offsets = [.6 .94 .8 .475 .47 .7 .87 .67 .535 .625 .485 .775 .79 .87 .59 .64 ...
   .71 .64 .64 .4 1.03 .65 .76 .865]; % time offsets for beginning of vcv stimuli
%found by manual inspection of the spectrum; corresponds entry-by-entry to
%list_words
volAndGainSettings = 'volume1.5, gain100';
volAndGainSettingsFileName = 'volume1point5_gain100';

for i=1:2:length(list_words)-1
        vcv_label1 = [list_words{i} '1'];
        vcv_plot1 = vibplot(vcv_label1,offsets(i));
        startSamp1 = list_startSamples(i);
        numSamps1 = list_numSamples(i);
        
        awave1 = wavedata(1, startSamp1:startSamp1+numSamps1);
        subplot(2,1,1);
        [S,F,T,P] = spectrogram(awave1,window,noverlap,nfft,fs,'yaxis');
        surf(T,F,10*log10(P),'edgecolor','none'); axis tight; view(0,90);
        colormap(hot);
        set(gca,'clim',[-80 -30]);
        set(gca,'ylim',[0 8000]);
        set(gca,'xlim',[offsets(i)-.1 offsets(i)+.9]);
        xlabel('time (s)'); ylabel = ('Hz');
        hold on;
        scatter(vcv_plot1(:,1),vcv_plot1(:,2),10,'w')
        for h=1:length(lookupf)
           hline = refline([0 lookupf(h)]);
        end
        title([vcv_label1 ' - ' volAndGainSettings]);
        
        vcv_label2 = [list_words{i} '2'];
        vcv_plot2 = vibplot(vcv_label2,offsets(i+1));
        startSamp2 = list_startSamples(i+1);
        numSamps2 = list_numSamples(i+1);
        
        awave2 = wavedata(1, startSamp2:startSamp2+numSamps2);
        subplot(2,1,2);
        [S2,F2,T2,P2] = spectrogram(awave2,window,noverlap,nfft,fs,'yaxis');
        surf(T2,F2,10*log10(P2),'edgecolor','none'); axis tight; view(0,90);
        colormap(hot);
        set(gca,'clim',[-80 -30]);
        set(gca,'ylim',[0 8000]);
        set(gca,'xlim',[offsets(i+1)-.1 offsets(i+1)+.9]);
        xlabel('time (s)'); ylabel = ('Hz');
        hold on;
        scatter(vcv_plot2(:,1),vcv_plot2(:,2),10,'w')
        for h=1:length(lookupf)
           hline = refline([0 lookupf(h)]);
        end
        title([vcv_label2 ' - ' volAndGainSettings]);
        set(gcf, 'PaperUnits', 'inches');
        x_width=7;y_width=11;
        set(gcf, 'PaperPosition', [0 0 x_width y_width]); %
        saveas(gcf,[list_words{i} '_' volAndGainSettingsFileName '.pdf'])
        close all
        
        clear awave1 awave2 S F T P S2 F2 T2 P2 vcv_plot1 vcv_plot2 startSamp1 startSamp2 numSamps1 numSamps2
end