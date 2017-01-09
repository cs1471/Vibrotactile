%
function xypoints = vibplot(file, timeoffset)
if exist('timeoffset','var') == 0
    timeoffset = 0.0;
end

%lookupf = [150.0,300.0,450.0,600.0,750.0,900.0,1050.0,1200.0,1350.0,1500.0,1650.0,1800.0,3115.0,3565.0];
%lookupf = [294,416,543,676,760,935,1074,1247,1410,1615,2062,2415,2766,4000];
lookupf = [260,392,525,660,791,925,1060,1225,1390,1590,1820,2080,2380,5000]; % freqs for GUEq vocoder algorithm 
map = [11,4,13,6,12,5,14,7,1,8,3,10,2,9];
load(file);
timepoints = tactStim{1}{1};
channels = tactStim{1}{2};

xypoints = zeros(2000,2);
numOut = 0;
numSamps = numel(timepoints);

for i = 1:numSamps
    tm = timeoffset + (double(timepoints(i))/1000.0);
    chan = channels(i);
    for b=1:14
        bt = map(b);
        if bitget(chan,bt) == 1
            numOut = numOut + 1;
            xypoints(numOut,1) = tm;
            xypoints(numOut,2) = lookupf(b);
        end
    end
end

xypoints = xypoints(1:numOut,:);
end % function
