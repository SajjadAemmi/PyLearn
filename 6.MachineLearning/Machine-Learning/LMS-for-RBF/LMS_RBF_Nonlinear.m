clear all;
close all;
clc;

% Read data
nInstances = 400;
nVars = 1;
[x,y] = makeData('regressionNonlinear',nInstances,nVars);
y = y + abs(min(y));
scatter(x, y,'b','Marker','.');
n = size(x ,1);

% Hyper Parameters
M = 10;
alpha = 0.1;
gama = 0.1;
beta = 0.05;

% Initialisation
W = rand(M,1);
Mu = rand(M,size(x,2));
Sigma = rand(M,size(x,2));

U = @(x_k, mu_j, sigma_j)exp(-(norm(x_k - mu_j).^2) ./ sigma_j);

for k = 1 : n
    
    % error
    y_hat(k) = 0;
    for j=1:M
        y_hat(k) = y_hat(k) + W(j) * U(x(k,:), Mu(j,:), Sigma(j,:));
    end
    e = y(k) - y_hat(k);
    
    % update
    for j=1:M
        Mu(j,:) = Mu(j,:) + alpha * ((4 ./ Sigma(j,:)) .* e .* W(j) .* (x(k, :) - Mu(j,:)) .* U(x(k,:), Mu(j,:), Sigma(j,:)));
        Sigma(j,:) = Sigma(j,:) + gama * ((4 * e ./ Sigma(j,:)) .* W(j) .* norm(x(k, :) - Mu(j,:)).^2 .* U(x(k,:), Mu(j,:), Sigma(j,:)));
        W(j) = W(j) + beta * (2 * e .* U(x(k,:), Mu(j,:), Sigma(j,:)));
    end
    
    [x_t, index] = sort(x(1:k));
    y_t = y(index);
    
    % test
    for i = 1 : k
        y_hat_t(i) = 0;
        for j=1:M
            y_hat_t(i) = y_hat_t(i) + W(j) * U(x_t(i,:), Mu(j,:), Sigma(j,:));
        end
        e(i) = y_t(i) - y_hat_t(i);
    end
    
    %plot
    y_hat_t = y_hat_t';
    
    hold off
    scatter(x_t(1:k, 1), y_t(1:k),'b','Marker','.');
    xlim([min(x) max(x)])
    ylim([min(y) max(y)])
    hold on
    plot(x_t(1:k, 1), y_hat_t(1:k),'LineWidth',3,'Color','g')
    xlabel('X')
    ylabel('Y')
    title(strcat('LMS for RBF - Train Data: ', int2str(k),'/',int2str(n)));
    grid on
    drawnow
    pause(0.001);
end