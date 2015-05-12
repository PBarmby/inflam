function detectProblems(filename)

data = csvread(filename);

mindata = min(data,[],1);
maxdata = max(data,[],1);

if (mindata(1)==0 && maxdata(20)==20)
    disp('Suspicious looking maxima!');
elseif sum(mindata)==0
    disp('Minima add up to zero!');
else
    disp('Seems OK!');
end

end