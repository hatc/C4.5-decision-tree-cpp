// C4.5 decision tree generator with Weka
// usage: java -classpath .;weka.jar Build [<class index of the training set>] [<classifier class name>] [<options for weka.classifiers.trees.J48>]
// Copyright (C) 2012-2013 Yuri Agafonov
// All rights reserved.
// 
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are met:
// 
// 1. Redistributions of source code must retain the above copyright notice, this
// list of conditions and the following disclaimer.
// 2. Redistributions in binary form must reproduce the above copyright notice,
// this list of conditions and the following disclaimer in the documentation
// and/or other materials provided with the distribution.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
// ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
// WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
// DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
// ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
// (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
// LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
// ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
// SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import java.io.*;

import weka.core.Instances;
import weka.classifiers.trees.J48;

class Build {
	static Instances loadData(String file_path, Integer class_index) {
		Instances r = null;
		BufferedReader reader = null;
		try {
			reader = new BufferedReader(new FileReader(file_path));
			r = new Instances(reader);
			if (class_index != null)
				r.setClassIndex(class_index.intValue());
			else
				r.setClassIndex(r.numAttributes() - 1);
		} catch (FileNotFoundException e) {
			System.out.println("can't find file: '" + file_path + "'");
		} catch (IOException e) {
			e.printStackTrace(System.out);
		} finally {
			try {
				if (reader != null)
					reader.close();
			} catch (IOException e) {}
		}
		return r;
	}
	static void writeText(String file_path, String text) {
		FileWriter writer = null;
		try {
			writer = new FileWriter(file_path);
			writer.write(text);
		} catch (IOException e) {
			e.printStackTrace(System.out);
		} finally {
			try {
				if (writer != null)
					writer.close();
			} catch (IOException e) {}
		}
	}
	
	public static void main(String[] args) throws Exception {
		if (args.length < 1) {
			System.out.println("path to the ARFF data file required");
			System.out.println("usage: java -cp .;weka.jar <training set>.arff [<class index of the training set>] [<classifier class name>]");
			System.out.println("<class index of the training set> defaults to number of attributes - 1");
			System.out.println("<classifier class name> defaults to WekaJ48Classifier");
			System.out.println("output: ./<classifier class name>.java");
			return;
		}
		Integer class_index = null;
		String java_class_name = "WekaJ48Classifier";
		String[] tree_options = null;
		if (args.length > 1) {
			int i = 1;
			if (args[i].charAt(0) != '-') {
				String arg = args[i++];
				try {
					class_index = Integer.valueOf(arg, 10);
				} catch (NumberFormatException e) {
					java_class_name = arg;
				}
				if (i < args.length) {
					if ((class_index != null) && (args[i].charAt(0) != '-'))
						java_class_name = args[i++];
				}
			}
			if (args.length - i > 0) {
				tree_options = new String[args.length - i];
				System.arraycopy(args, i, tree_options, 0, args.length - i);
			}			
		}
		
		Instances data = loadData(args[0], class_index);
		if (data == null)
			return;
		
		J48 tree = new J48();  
		if (tree_options != null)
			tree.setOptions(tree_options);
		// tree.setOptions(new String[] { "-U" }); // unpruned tree
		tree.buildClassifier(data);
		
		writeText(String.format("./%s.java", java_class_name), tree.toSource(java_class_name));
		
		/*Instances test = loadData(args[1]);
		weka.classifiers.Evaluation eval = new weka.classifiers.Evaluation(data);
		eval.evaluateModel(tree, test);
		System.out.println(eval.toSummaryString("\nResults\n======\n", false));*/
	}
}
