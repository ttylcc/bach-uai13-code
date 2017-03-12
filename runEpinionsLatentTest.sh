#!/bin/sh

echo "Compiling..."
mvn compile > /dev/null
mvn dependency:build-classpath -Dmdep.outputFile=classpath.out > /dev/null
mkdir output > /dev/null

echo "Running HL-MRF-Q on wiki..."
java -Xmx1g -cp ./target/classes:`cat classpath.out` edu.umd.cs.bachuai13.WikiLatentTest quad > output/WikiLatentTest.hlmrf-q.out
echo "Running HL-MRF-L on wiki..."
java -Xmx1g -cp ./target/classes:`cat classpath.out` edu.umd.cs.bachuai13.WikiLatentTest linear > output/WikiLatentTest.hlmrf-l.out
echo "Running MRF on wiki..."
java -Xmx1g -cp ./target/classes:`cat classpath.out` edu.umd.cs.bachuai13.WikiLatentTest bool > output/WikiLatentTest.mrf.out

echo "Processing results..."
# cd src/main/matlab
# matlab -nodesktop -nosplash -r parse_wiki
