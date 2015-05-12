function analyse(filename)

data = csvread(filename);

figure('position',[7   716   846   233]);
subplot(1,3,1)
plot(mean(data))
ylabel('AVERAGE')
subplot(1,3,2)
plot(min(data,[],1))
subplot(1,3,3)
plot(max(data,[],1))

end