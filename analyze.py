def analyze(filename):
     data = numpy.loadtxt(fname=filename, delimiter=',')
     fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))
     axes1 = fig.add_subplot(1, 3, 1)
     axes2 = fig.add_subplot(1, 3, 2)
     axes3 = fig.add_subplot(1, 3, 3)
     axes1.set_ylabel('average')
     axes1.plot(data.mean(axis=0))
     axes2.set_ylabel('max')
     axes2.plot(data.max(axis=0))
     axes3.set_ylabel('min')
     axes3.plot(data.min(axis=0))
     fig.tight_layout()
     matplotlib.pyplot.show(fig)


def detectProblems(filename):
     data = numpy.loadtxt(fname=filename, delimiter=',')
     if data.max(axis=0)[0] == 0 and data.max(axis=0)[20] == 20:
         print 'Suspicious looking maxima!'
     elif data.min(axis=0).sum() == 0:
         print 'Minima add up to zero!'
     else:
         print 'Seems OK!'
