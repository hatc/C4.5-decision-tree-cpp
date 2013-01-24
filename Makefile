CXXFLAGS := -I./include $(CXXFLAGS)
HEADERS = $(addprefix ./include/,basic.h csv_reader.hpp file_stream.hpp iterator_adapter.hpp scoped_buf.hpp string_piece.hpp)

classifier: main.cpp $(HEADERS)
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) -o classifier main.cpp

main.cpp: WekaJ48Classifier.java java.weka.parser.py
	./java.weka.parser.py WekaJ48Classifier.java

WekaJ48Classifier.java: Build.class training_set.arff
	java -cp .:weka.jar Build training_set.arff

Build.class: Build.java
	javac -cp weka.jar Build.java

training_set.arff: data.py
	./data.py -t training_set.arff

.PHONY: clean cleanall test

clean:
	rm -f WekaJ48Classifier.java training_set.arff main.cpp

cleanall: clean
	rm -f TestClassifier.class data.arff data.csv classifier java_results cpp_results IterableEnumeration*.class

test: java_results cpp_results
	diff -q java_results cpp_results

java_results: TestClassifier data.arff
	java -cp .:weka.jar TestClassifier data.arff>java_results

cpp_results: classifier data.csv
	./classifier data.csv>cpp_results

data.arff: data.csv
	./data.py -c data.csv data.arff

data.csv:
	./data.py data.csv

TestClassifier: WekaJ48Classifier.java
	javac -cp weka.jar -Xlint:unchecked TestClassifier.java IterableEnumeration.java WekaJ48Classifier.java
