%% Soft Margin Support Vector Machine
clear all;  close all;  clc;

trainData = csvread('linear_data_train.csv',1);
n = size(trainData, 1);

X = trainData(:, 1:end-1);
Y = trainData(:, end);

%% Hyper Parameter
C = 100;

%% Quadratic Programming
K = X * X';
H = (Y * Y') .* K;
f = -1 * ones(n,1);
A = [];
b = [];
Aeq = Y';
beq = 0;
lb = zeros(n,1);
ub = C * ones(n,1);

alpha = quadprog(H, f, A, b, Aeq, beq, lb, ub);

%%
nonzero_alpha = find(alpha > 1e-6);
f_out = sum(alpha .* Y .* ones(1 ,n) .* K, 1)';
b = mean(Y(nonzero_alpha) - f_out(nonzero_alpha));
w = sum(repmat(alpha.*Y,1,2).*X,1);

%% Plot

hold on
xlim([-0.2 1.2])
ylim([-0.4 1])
scatter(X(Y == 1, 1), X(Y == 1, 2),'.r')
scatter(X(Y == -1, 1), X(Y == -1, 2),'.b')

scatter(X(nonzero_alpha ,1), X(nonzero_alpha,2),'.r','markeredgecolor',[0.6 0.6 0.6]);

%Seperating hyperplane
p = plotpc(w(1:2),b);   set(p, 'Color', 'k');

%Margin
p = plotpc(w(1:2),b+1); set(p, 'Color', 'g');
p = plotpc(w(1:2),b-1); set(p, 'Color', 'g');

%% Test
testData = csvread('linear_data_test.csv',1);

X = testData(:,1:end-1);
Y = testData(:,end);

hold on
scatter(X(Y == 1, 1), X(Y == 1, 2),'.m')
scatter(X(Y == -1, 1), X(Y == -1, 2),'.c')