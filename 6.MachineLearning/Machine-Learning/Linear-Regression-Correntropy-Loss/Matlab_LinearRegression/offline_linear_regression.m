clear all;
close all;
clc;

%% Read data
X = csvread('Housing.csv');

x(:,2) = X(:, 1);
x(:,1) = 1; %for bias
y = X(:, 2);

%% Correntropy loss function

% Hyper Parameters
eta = 0.001;  iteration = 30;

% weights initialisation
W = rand(size(x,2),1);

for k = 1 : iteration
    
    e = y - (x * W);
    mu = exp(-eta .* e.^2);
    
    R = x' * (x .* mu);
    P = x' * (y .* mu);
    W = inv(R) * P;
   
    %% plot
    hold off;
    scatter(x(:, 2), y,'b','Marker','.');
    y_hat = x * W;
    
    hold on
    plot(x(:, 2), y_hat,'LineWidth',3,'Color','g')
    xlabel('Size')
    ylabel('Price')
    title('Linear Regression')
    grid on
    drawnow;
    pause(0.1);
end

%% Square loss function
W = inv(x' * x) * (x' * y);
y_hat = x*W;
    
%% plot
hold on
plot(x(:, 2), y_hat,'LineWidth',3,'Color','r')
