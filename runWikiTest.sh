#!/bin/sh

echo "Compiling..."
mvn compile > /dev/null
mvn dependency:build-classpath -Dmdep.outputFile=classpath.out > /dev/null
mkdir output > /dev/null

echo "Running HL-MRF-Q on Wiki..."
java -Xmx8g -cp ./target/classes:`cat classpath.out` cs249.Wiki quad > output/Wiki.hlmrf-q.out

echo "Store output files..."
