#!/bin/sh
javac -cp weka.jar Build.java
if [ $? -ne 0 ]; then
    echo "javac fails"
    exit 1
fi

java -cp .:weka.jar Build training_set.arff J48Classificator
