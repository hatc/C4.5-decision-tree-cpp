# C4.5 decision tree builder for C++ with Weka
* Uses Weka to build classifier for training set and generate Java source code.
* Parse and translate Java source code to C++ with ANTLR 3
* Generated C++ classifier supports data in csv format

## Requirements
* Python 2.6+
* Java 1.6+
* GCC or any other C++03 compiler

## Installation:

download/fork repository in some folder
download and unpack weka.jar from [weka-3-6-8.zip][1] to same folder

## Usage
>simple Makefile provided for build C++ classifier from randomly generated training_set.arff

1) Build classifier for training set
```
java -cp weka.jar;. Build <training_set>.arff [<X>] [<classifier class name>]
```

where &lt;X&gt; is class index, i.e. index of attribute used for build decision tree, defaults for number of attributes - 1
and &lt;classifier class name&gt; defaults to WekaJ48Classifier

>produce: WekaJ48Classifier.java

2) Translate java source code to c++
```
python java.weka.parser.py WekaJ48Classifier.java [-cn <classifier java class name>] [-o <cpp file name>]
```

where &lt;classifier java class name&gt; defaults to Java source file name
and &lt;cpp file name&gt; defaults to main.cpp

>produce: main.cpp

3) Compile c++ source code
```
g++ /I./include main.cpp -o classifier
```

4) Classify some data:
```
./classifier data.csv
```

## Test:

1) Generate training_set.arff 
```
./data.py -t training_set.arff
```

2) Build classifier
```
java -cp .:weka.jar Build training_set.arff
```

>produce WekaJ48Classifier.java

3) Translate java source code to c++
```
./java.weka.parser.py WekaJ48Classifier.java
```

>produce main.cpp

4) Compile C++ source code 
```
g++ -I./include main.cpp -o classifier
```

5) Generate data.csv
```
./data.py data.csv
```

6) Classify data.csv
```
./classifier data.csv>cpp_results
```

7) Convert data.csv to data.arff
```
./data.py -c data.csv data.arff
```

8) Build java classifier
```
javac -cp weka.jar -Xlint:unchecked TestClassifier.java IterableEnumeration.java WekaJ48Classifier.java
```

8) Classify data.csv
```
java -cp weka.jar;. TestClassifier data.arff>java_results
```

9) Compare results
diff -q cpp_results java_results

  [1]: http://sourceforge.net/projects/weka/files/weka-3-6/3.6.8/weka-3-6-8.zip/download
