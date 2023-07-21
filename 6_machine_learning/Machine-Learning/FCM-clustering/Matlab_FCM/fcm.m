clear all;
close all;
clc;
%% Hyper Parameters
C = 3;  m = 1.1;  iteration = 50;

%%
X = csvread('xclara.csv',1);
n = size(X, 1);
dimension = size(X, 2);

U = rand(n, C);

%%
for k = 1 : iteration
    
    for i = 1:n
        U(i,:) = U(i,:) / sum(U(i,:));
    end
    for j = 1:C
        mu(j, :) = (sum((U(:,j).^m) .* X(:, :))) ./ (sum(U(:,j) .^ m));
    end
    
    for i = 1:n
        for j = 1:C
              U(i,j) = 1 ./ sum((d(X(i,:),mu(j,:))) ./ d( X(i,:),mu(:,:)))^(1/(m-1));  
        end
    end
    
    hold off;
    scatter(X(:, 1), X(:, 2),'k','Marker','.');
    hold on;
    scatter(mu(:,1), mu(:,2) ,140, 'filled','d','MarkerEdgeColor', [0 , 0 , 0],'MarkerFaceColor',[1,1,0],'LineWidth',2);
    drawnow;
end

%%
for i = 1:size(U,1)
   [~, U_crisp(i)] = max(U(i,:)); 
end

colors = [1,0,0;0,1,0;0,0,1;1,0,1];

for i = 1:C
    scatter(X(U_crisp == i, 1), X(U_crisp == i, 2), 'filled', 'MarkerEdgeColor', [0 , 0 , 0], 'MarkerFaceColor',colors(i,:));
    hold on;
end    

scatter(mu(:,1), mu(:,2) ,140, 'filled','d','MarkerEdgeColor', [0 , 0 , 0],'MarkerFaceColor',[1,1,0],'LineWidth',2);

function distance = d(x, y)
for i = 1:size(y, 1)
    distance(i) = norm(x - y(i,:));
end
end