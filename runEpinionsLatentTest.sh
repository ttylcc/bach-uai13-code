#!/bin/sh

echo "Compiling..."
mvn compile > /dev/null
mvn dependency:build-classpath -Dmdep.outputFile=classpath.out > /dev/null
mkdir output > /dev/null

echo "Running HL-MRF-Q on Epinions..."
java -Xmx1g -cp ./target/classes:`cat classpath.out` edu.umd.cs.bachuai13.EpinionsLatentTest quad > output/epinionsLatentTest.hlmrf-q.out
echo "Running HL-MRF-L on Epinions..."
java -Xmx1g -cp ./target/classes:`cat classpath.out` edu.umd.cs.bachuai13.EpinionsLatentTest linear > output/epinionsLatentTest.hlmrf-l.out
echo "Running MRF on Epinions..."
java -Xmx1g -cp ./target/classes:`cat classpath.out` edu.umd.cs.bachuai13.EpinionsLatentTest bool > output/epinionsLatentTest.mrf.out

echo "Processing results..."
# cd src/main/matlab
# matlab -nodesktop -nosplash -r parse_epinions
