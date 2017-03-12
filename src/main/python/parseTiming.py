#!/usr/bin/python

import sys, re

def getTime(method):
	return  str(round(sum(times[method]) / len(times[method]), 2))

# Defines files to read from
files = {}
files['epinions.hlmrf-q'] = 'output/timing.epinions.hlmrf-q.out'
files['epinions.hlmrf-l'] = 'output/timing.epinions.hlmrf-l.out'
files['epinions.mrf'] = 'output/timing.epinions.mrf.out'

# Defines lists of times for each method,problem pair
times = {}
for method in files:
	times[method] = []
	
startRegex = re.compile(r'(\d+) \[main\] INFO  edu.umd.cs.psl.application.inference.MPEInference  - Beginning inference.')
endRegex = re.compile(r'(\d+) \[main\] INFO  edu.umd.cs.psl.application.inference.MPEInference  - Inference complete. Writing results to Database.')

for method, timeList in times.iteritems():
	f = open(files[method],'r')
	line = f.readline()
	method = ''
	startTime = 0
	while line != '':
		matches = startRegex.search(line)
		if matches != None:
			# found start time
			if startTime != 0:
				print 'ERROR: Found two consecutive start times without end time in between.'
				exit()
			startTime = long(matches.group(1))
		matches = endRegex.search(line)
		if matches != None:
			# found end time
			if startTime == 0:
				print 'ERROR: Found end time without matching start time.'
				exit()
			endTime = long(matches.group(1))
			elapsed = endTime - startTime
			# add to results
			timeList.append(0.001 * elapsed)
			# Resets state
			startTime = 0
		line = f.readline()
	f.close()

# output
print 'BEGIN TIMING RESULTS TABLE'
print
print '\\begin{tabular}{lrrr}'
print '\\toprule'
print ' & Epinions & Epinions & Epinions \\\\'
print '\midrule'
print 'HL-MRF-Q & ' + getTime('epinions.hlmrf-q') + ' & ' + getTime('epinions.hlmrf-q') + ' & ' + getTime('epinions.hlmrf-q') + ' \\\\'
print 'HL-MRF-L & ' + getTime('epinions.hlmrf-l') + ' & ' + getTime('epinions.hlmrf-l') + ' & ' + getTime('epinions.hlmrf-l') + ' \\\\'
print 'MRF & ' + getTime('epinions.mrf') + ' & ' + getTime('epinions.mrf') + ' & ' + getTime('epinions.mrf') + ' \\\\'
print '\\bottomrule'
print '\\end{tabular}'
print
print 'END TIMING RESULTS TABLE'
