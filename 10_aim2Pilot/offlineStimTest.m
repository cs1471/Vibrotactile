stimGenPTB('open');
load('asa1');
tm = tactStim{1}{1};
ch = tactStim{1}{2};
stimGenPTB('load',remapChan(ch),tm);
stimGenPTB('start');