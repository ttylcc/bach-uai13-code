#!/bin/sh

echo "Compiling..."
mvn compile > /dev/null
mvn dependency:build-classpath -Dmdep.outputFile=classpath.out > /dev/null
mkdir output > /dev/null

echo "Running HL-MRF-Q on Epinions..."
java -Xmx1g -cp ./target/classes:`cat classpath.out` edu.umd.cs.bachuai13.timing.Epinions quad > output/timing.epinions.hlmrf-q.out
echo "Running HL-MRF-L on Epinions..."
java -Xmx1g -cp ./target/classes:`cat classpath.out` edu.umd.cs.bachuai13.timing.Epinions linear > output/timing.epinions.hlmrf-l.out
echo "Running MRF on Epinions..."
java -Xmx1g -cp ./target/classes:`cat classpath.out` edu.umd.cs.bachuai13.timing.Epinions bool > output/timing.epinions.mrf.out

echo "Processing results..."
src/main/python/parseTiming.py
