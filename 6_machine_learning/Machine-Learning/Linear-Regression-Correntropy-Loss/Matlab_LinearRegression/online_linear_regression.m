clear all;
close all;
clc;

%% Read data
% x = csvread('Housing.csv');
% y = x(:, 2);

nInstances = 800;
nVars = 1;
[x,y] = makeData('regressionOutliers',nInstances,nVars);
%y = -y;
x(:,2) = 1; %for bias

%% online correntropy loss function

% Hyper Parameters
mu = 1;
sigma = 50;

% weights initialisation
W = rand(size(x,2),1);

for k = 1 : size(x ,1)
    
    e = y(k) - (x(k, :) * W);
    
    W = W + ((((2 * mu) / sigma) * e) .* x(k, :)' * exp((-(e^2)) / sigma));
   
    %% plot
    hold off;
    scatter(x(1:k, 1), y(1:k),'r','Marker','.');
    y_hat = x * W;
    
    hold on
    plot(x(:, 1), y_hat,'LineWidth',3,'Color','b')
    xlabel('Size')
    ylabel('Price')
    title('Linear Regression')
    grid on
    drawnow;
    pause(0.0001);
end