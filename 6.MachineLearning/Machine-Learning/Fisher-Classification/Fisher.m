clear all;  close all;  clc;

%% Set Data
X = [randn(200,2) * 2; 
    (randn(200,2)+[6, -4]) * 2];

Y = [repmat(-1,200,1); repmat(1,200,1)];

%% Processing Data
m1 = mean(X(find(Y==1), :), 1);
m2 = mean(X(find(Y==-1), :), 1);

cov1 = cov(X(find(Y==1), :));
cov2 = cov(X(find(Y==-1), :));

Sw = cov1 + cov2;

w = inv(Sw) * (m1 - m2)';

mu1 = m1 * w;
mu2 = m2 * w;

b = -(mu1 + mu2) / 2;

x = -20:20;
y = (w(2) * x) / w(1);

%% Plot
figure;
hold on

xlim([-10 20])
ylim([-20 10])

scatter(X(Y==1,1),X(Y==1,2),'.','markerfacecolor','b');
scatter(X(Y==-1,1),X(Y==-1,2),'.','markerfacecolor','r');

scatter(m1(1),m1(2),'o','markerfacecolor','b');
scatter(m2(1),m2(2),'o','markerfacecolor','r');

plot(x,y,'g');
p = plotpc(w', b);  set(p, 'Color', 'm');