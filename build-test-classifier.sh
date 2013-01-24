#!/bin/sh
javac -cp weka.jar -Xlint:unchecked TestClassifier.java IterableEnumeration.java J48Classificator.java
if [ $? -ne 0 ]; then
    echo "javac fails"
    exit 1
fi

java -cp .:weka.jar TestClassifier data.arff
