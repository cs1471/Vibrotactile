clear;
f1=2.^([0:.1:2]+log2(25));

rng('shuffle')

order_cond = [load('/Users/courtney/Desktop/erraruns/forCourtney-1.txt'),...
              load('/Users/courtney/Desktop/erraruns/forCourtney-2.txt'),...
              load('/Users/courtney/Desktop/erraruns/forCourtney-3.txt'),...
              load('/Users/courtney/Desktop/erraruns/forCourtney-4.txt')];

order_cond = vertcat(order_cond(:,1), order_cond(:,2), order_cond(:,3), order_cond(:,4))';

%generate frequency pairs 5,35,65,95% steps along the morph line
frequency = [f1(2) f1(8) f1(14) f1(20); f1(20) f1(14) f1(8) f1(2)];

%generate stimulator channel pairs
s1=[1 2 3 4 5 6 1 2 3 4 5 6];
s2=[9 10 11 12 13 14 10 9 12 11 14 13];
stimulator=[s1; s2]; 

% define the stimuli
m0 = [repmat(frequency(:,1),1,42) repmat(frequency(:,2),1,10) repmat(frequency(:,3),1,10) repmat(frequency(:,4),1,42);
      repmat(frequency(:,1),1,42) repmat(frequency(:,2),1,10) repmat(frequency(:,3),1,10) repmat(frequency(:,4),1,42)];
m3w = [repmat(frequency(:,1),1,52) repmat(frequency(:,4),1,52);
       repmat(frequency(:,2),1,52) repmat(frequency(:,3),1,52)];
m3b = [repmat(frequency(:,2),1,100);
       repmat(frequency(:,3),1,100)];
m6 = [repmat(frequency(:,1),1,50) repmat(frequency(:,4),1,50);
      repmat(frequency(:,3),1,50) repmat(frequency(:,2),1,50)];
null = zeros(4,100);
  
%randomly shuffle stimuli
nCond1 = find(order_cond == 1);
nCond2 = find(order_cond == 2);
nCond3 = find(order_cond == 3);
nCond4 = find(order_cond == 4);
nNull = find(order_cond == 5);

nCond1 = randperm(size(nCond1,2));
nCond2 = randperm(size(nCond2,2));
nCond3 = randperm(size(nCond3,2));
nCond4 = randperm(size(nCond4,2));
nNull = randperm(size(nNull,2));


m0 = m0(:,nCond1);
m3w = m3w(:,nCond2);
m3b = m3b(:,nCond3);
m6 = m6(:,nCond4);
null = null(:,nNull);




