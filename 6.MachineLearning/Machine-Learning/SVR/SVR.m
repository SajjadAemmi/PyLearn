clc;
clear all;
close all;

%% Set Data
n = 500;
X = rand(n,1) * 100 + randn;
W = rand * 2;
Y = X * W + rand(n,1)*10;
outliers = rand(n,1) < 0.2;
Y(outliers) = Y(outliers) + randn(sum(outliers),1)*25;
Y = Y + randn * 10;
%% Hyper Parameter
C = 10;

%% Quadratic Programming
K = X * X';
H = K;
f = -Y;
A = [];
b = [];
Aeq = ones(1,n);
beq = 0;
lb = -C * ones(n,1);
ub = C * ones(n,1);

beta = quadprog(H, f, A, b, Aeq, beq, lb, ub);

%%
f_out = sum(beta .*  K)';
b = mean(Y - f_out);
w = sum(beta .* X);

%% Plot
c = linspace(1,10,length(X));
scatter(X, Y,10,c);
xlim([0 100])
ylim([-10 100])

hold on;
y = (w * X) + b;
plot(X,y,'k','LineWidth',2);
y1 = y + b;
plot(X,y1,'r');
y2 = y - b;
plot(X,y2,'r');