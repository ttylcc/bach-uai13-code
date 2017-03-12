#!/bin/sh

echo "Compiling..."
mvn compile > /dev/null
mvn dependency:build-classpath -Dmdep.outputFile=classpath.out > /dev/null
mkdir output > /dev/null

echo "Running HL-MRF-Q on Wiki..."
java -Xmx8g -cp ./target/classes:`cat classpath.out` edu.umd.cs.bachuai13.Wiki quad > output/Wiki.hlmrf-q.out
# echo "Running HL-MRF-L on wiki..."
# java -Xmx1g -cp ./target/classes:`cat classpath.out` edu.umd.cs.bachuai13.Wiki linear > output/Wiki.hlmrf-l.out
# echo "Running MRF on wiki..."
# java -Xmx1g -cp ./target/classes:`cat classpath.out` edu.umd.cs.bachuai13.Wiki bool > output/Wiki.mrf.out

echo "Processing results..."
# cd src/main/matlab
# matlab -nodesktop -nosplash -r parse_wiki
